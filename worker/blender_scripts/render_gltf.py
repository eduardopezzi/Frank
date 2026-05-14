"""
Frank render script for glTF/GLB models — uses Blender Cycles engine.

This script is executed by Blender via CLI:
    blender -b -P render_gltf.py -- input.glb output.png settings.json

It imports the model, sets up scene (camera, lighting, environment),
applies render settings, and outputs a PNG image.

IMPORTANT: Runs inside Blender's Python — has access to `bpy`.
"""

import json
import os
import sys

# Blender's Python environment
import bpy

# Add parent directory to path so we can import setup_scene
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from setup_scene import (
    auto_frame_camera,
    apply_pbr_materials,
    configure_render_engine,
    get_scene_bounds,
    setup_custom_camera,
    setup_environment,
    setup_three_point_lighting,
)


def parse_arguments():
    """Parse command-line arguments passed after '--'."""
    argv = sys.argv
    if "--" not in argv:
        raise RuntimeError(
            "No arguments provided. Usage: blender -b -P render_gltf.py -- "
            "input.glb output.png '{settings_json}'"
        )

    args = argv[argv.index("--") + 1:]
    if len(args) < 2:
        raise RuntimeError("At least input_file and output_file are required")

    input_file = args[0]
    output_file = args[1]
    settings_arg = args[2] if len(args) > 2 else "{}"

    try:
        # Check if the argument is a file path or raw JSON
        if os.path.exists(settings_arg):
            with open(settings_arg, "r") as f:
                render_settings = json.load(f)
        else:
            render_settings = json.loads(settings_arg)
    except (json.JSONDecodeError, OSError):
        print(f"[Frank] Warning: Could not parse settings from '{settings_arg[:50]}...', using defaults")
        render_settings = {}

    return input_file, output_file, render_settings


def clean_scene():
    """Clean the scene manually without resetting factory settings (preserves addons)."""
    import bpy
    
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    
    # Select and delete all objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Remove all mesh data blocks
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
    
    # Remove all materials
    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)
    
    # Remove all textures/images
    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)
    
    # Remove all lights
    for block in bpy.data.lights:
        if block.users == 0:
            bpy.data.lights.remove(block)
    
    # Remove all cameras
    for block in bpy.data.cameras:
        if block.users == 0:
            bpy.data.cameras.remove(block)
    
    print("[Frank] Scene cleaned (objects, meshes, materials, images, lights, cameras)")


def _import_skp(filepath):
    """
    Import a SketchUp (.skp) file into Blender.
    
    Uses the sketchup_importer addon with a multi-layer loading strategy:
      1. Standard addon enable via addon_utils (with refresh)
      2. Fallback: direct import via importlib + manual register
    """
    import addon_utils
    import importlib
    
    addon_module = "sketchup_importer"
    addon_path = "/usr/local/blender/4.0/scripts/addons"
    
    # ─── Camada 1: Método padrão com addon_utils ───────────────────
    try:
        if addon_path not in sys.path:
            sys.path.insert(0, addon_path)
            print(f"[Frank] Added {addon_path} to sys.path")
        
        # Forçar rediscovery dos addons
        addon_utils.modules(refresh=True)
        print("[Frank] Refreshed addon modules")
        
        # Verificar se o addon já está ativo
        is_loaded = addon_utils.check(addon_module)[0]
        if not is_loaded:
            print(f"[Frank] Enabling {addon_module} addon...")
            bpy.ops.preferences.addon_enable(module=addon_module)
            print(f"[Frank] {addon_module} addon enabled")
        else:
            print(f"[Frank] {addon_module} already loaded")
    
    except Exception as e:
        print(f"[Frank] Camada 1 falhou: {e}")
        
        # ─── Camada 2: Import direto via importlib ─────────────────
        try:
            print(f"[Frank] Tentando import direto de {addon_module}...")
            skp_module = importlib.import_module(addon_module)
            
            if hasattr(skp_module, 'register'):
                skp_module.register()
                print(f"[Frank] {addon_module} registrado manualmente")
            else:
                print(f"[Frank] Módulo {addon_module} não tem função register()")
        except ImportError as ie:
            raise RuntimeError(
                f"SKP Import failed: Could not load '{addon_module}' addon.\n"
                f"addon_utils error: {e}\n"
                f"importlib error: {ie}\n"
                f"Ensure the SketchUp importer addon is installed in {addon_path}"
            )
    
    # ─── Executar importação SKP ────────────────────────────────────
    try:
        bpy.ops.import_scene.skp(filepath=filepath)
        print(f"[Frank] SKP file imported successfully: {filepath}")
    except AttributeError:
        # Fallback: tentar outros nomes de operador possíveis
        try:
            bpy.ops.wm.skp_import(filepath=filepath)
        except AttributeError:
            raise RuntimeError(
                "SKP import operator not found. The sketchup_importer addon "
                "may not be correctly installed or compatible with this Blender version."
            )


def _load_materials_catalog():
    """Load materials catalog from JSON file."""
    catalog_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "catalog", "materials.json"
    )
    try:
        with open(catalog_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[Frank] Warning: Materials catalog not found at {catalog_path}")
        return []


# Path to textures in the Docker container
TEXTURES_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "catalog", "textures"
)

def _add_texture_node(mat, input_name, filename, color_space='sRGB', textures_dir=None):
    """Helper to add an image texture node and connect it to a Principled BSDF input."""
    if not filename:
        return None
        
    # Use provided textures_dir or fallback to global constant
    base_dir = textures_dir or TEXTURES_DIR
    img_path = os.path.join(base_dir, filename)
    
    if not os.path.exists(img_path):
        print(f"[Frank] Warning: Texture file not found at: {img_path}")
        return None
        
    try:
        img = bpy.data.images.load(img_path)
        img.colorspace_settings.name = color_space
    except Exception as e:
        print(f"[Frank] Error loading image {filename} from {img_path}: {e}")
        return None

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Find Principled BSDF
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    if not principled:
        return None

    # Create texture node
    tex_node = nodes.new('ShaderNodeTexImage')
    tex_node.image = img
    
    # Connect based on input name
    if input_name == "Base Color":
        links.new(tex_node.outputs["Color"], principled.inputs["Base Color"])
    elif input_name == "Roughness":
        links.new(tex_node.outputs["Color"], principled.inputs["Roughness"])
    elif input_name == "Metallic":
        links.new(tex_node.outputs["Color"], principled.inputs["Metallic"])
    elif input_name == "Normal":
        # Normal maps need a Normal Map node
        norm_map_node = nodes.new('ShaderNodeNormalMap')
        links.new(tex_node.outputs["Color"], norm_map_node.inputs["Color"])
        links.new(norm_map_node.outputs["Normal"], principled.inputs["Normal"])
    elif input_name == "Displacement":
        # Simplified displacement via Bump node if connected to Normal
        # Or real displacement if connected to Material Output
        bump_node = nodes.new('ShaderNodeBump')
        links.new(tex_node.outputs["Color"], bump_node.inputs["Height"])
        # If there's already a normal map, we need to chain them
        current_norm = principled.inputs["Normal"].links
        if current_norm:
            prev_node = current_norm[0].from_node
            links.new(prev_node.outputs["Normal"], bump_node.inputs["Normal"])
        links.new(bump_node.outputs["Normal"], principled.inputs["Normal"])

    return tex_node

def _create_pbr_material(mat_data, mat_name="FrankMaterial", textures_dir=None):
    """Create a Blender PBR material from catalog data, including textures."""
    mat = bpy.data.materials.new(name=mat_name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Clear default nodes to ensure a clean start
    nodes.clear()
    
    output = nodes.new("ShaderNodeOutputMaterial")
    principled = nodes.new("ShaderNodeBsdfPrincipled")
    links.new(principled.outputs["BSDF"], output.inputs["Surface"])

    pbr = mat_data.get("pbr_properties", {})

    # 1. Basic Properties
    if "base_color" in pbr:
        color = pbr["base_color"]
        if len(color) == 3:
            color = (*color, 1.0)
        principled.inputs["Base Color"].default_value = color

    if "metallic" in pbr:
        principled.inputs["Metallic"].default_value = pbr["metallic"]

    if "roughness" in pbr:
        principled.inputs["Roughness"].default_value = pbr["roughness"]

    if "emission" in pbr and pbr["emission"] > 0:
        if "emission_color" in pbr:
            ec = pbr["emission_color"]
            principled.inputs["Emission Color"].default_value = (*ec, 1.0)
        principled.inputs["Emission Strength"].default_value = pbr["emission"]

    if "alpha" in pbr and pbr["alpha"] < 1.0:
        principled.inputs["Alpha"].default_value = pbr["alpha"]
        mat.blend_method = "HASHED"

    if "transmission" in pbr and pbr["transmission"] > 0:
        principled.inputs["Transmission Weight"].default_value = pbr["transmission"]

    if "ior" in pbr:
        principled.inputs["IOR"].default_value = pbr["ior"]

    # 2. Texture Maps
    _add_texture_node(mat, "Base Color", pbr.get("base_color_map"), 'sRGB', textures_dir)
    _add_texture_node(mat, "Roughness", pbr.get("roughness_map"), 'Non-Color', textures_dir)
    _add_texture_node(mat, "Metallic", pbr.get("metallic_map"), 'Non-Color', textures_dir)
    _add_texture_node(mat, "Normal", pbr.get("normal_map"), 'Non-Color', textures_dir)
    _add_texture_node(mat, "Displacement", pbr.get("displacement_map"), 'Non-Color', textures_dir)

    return mat


def _apply_material_overrides(overrides, textures_dir=None):
    """
    Apply material overrides to the scene.
    overrides can be:
    - list[str]: List of material IDs to apply globally (first valid wins)
    - dict[str, str]: Mapping of {mesh_name: material_id}
    """
    catalog = _load_materials_catalog()
    if not catalog:
        print("[Frank] Warning: Empty materials catalog, skipping material override")
        return

    # Cache created materials to avoid duplicate work
    material_cache = {}

    def get_blender_material(mid):
        if mid in material_cache:
            return material_cache[mid]
        
        # Find in catalog
        mat_data = next((m for m in catalog if m.get("material_id") == mid), None)
        if not mat_data:
            return None
        
        mat = _create_pbr_material(mat_data, mat_data["name"], textures_dir=textures_dir)
        material_cache[mid] = mat
        return mat

    count = 0

    if isinstance(overrides, dict):
        # Case 1: Granular mapping {mesh_name: material_id}
        print(f"[Frank] Applying granular material mapping: {overrides}")
        for mesh_name, mid in overrides.items():
            blender_mat = get_blender_material(mid)
            if not blender_mat:
                continue
            
            # Match exact or case-insensitive or partial
            for o in bpy.context.scene.objects:
                if o.type == "MESH":
                    clean_name = o.name.split('.')[0]
                    if o.name == mesh_name or o.name.lower() == mesh_name.lower() or \
                       clean_name.lower() == mesh_name.lower():
                        o.data.materials.clear()
                        o.data.materials.append(blender_mat)
                        print(f"[Frank] Applied {mid} to {o.name}")
                        count += 1

    elif isinstance(overrides, list):
        # Case 2: Global application (legacy)
        print(f"[Frank] Applying global material override from list: {overrides}")
        blender_mat = None
        for mid in overrides:
            blender_mat = get_blender_material(mid)
            if blender_mat:
                break
        
        if blender_mat:
            for obj in bpy.context.scene.objects:
                if obj.type == "MESH":
                    obj.data.materials.clear()
                    obj.data.materials.append(blender_mat)
                    count += 1
    
    print(f"[Frank] Applied material overrides to {count} objects")


def _apply_default_material_if_needed():
    """
    Auto-material: if any mesh has no materials, create a default white PBR
    and apply to all un-materialized meshes.
    """
    needs_material = []
    for obj in bpy.context.scene.objects:
        if obj.type == "MESH" and len(obj.data.materials) == 0:
            needs_material.append(obj)

    if not needs_material:
        print("[Frank] Step 8: All meshes have materials, no auto-material needed")
        return

    print(f"[Frank] Step 8: {len(needs_material)} meshes without materials — applying auto-material")

    # Create a clean white PBR material
    default_mat = bpy.data.materials.new(name="FrankDefaultMaterial")
    default_mat.use_nodes = True
    nodes = default_mat.node_tree.nodes

    principled = None
    for node in nodes:
        if node.type == "BSDF_PRINCIPLED":
            principled = node
            break
    if principled is None:
        principled = nodes.new("ShaderNodeBsdfPrincipled")

    principled.inputs["Base Color"].default_value = (0.85, 0.85, 0.88, 1.0)
    principled.inputs["Roughness"].default_value = 0.5
    principled.inputs["Metallic"].default_value = 0.0

    for obj in needs_material:
        obj.data.materials.append(default_mat)

    print(f"[Frank] Auto-material applied to {len(needs_material)} meshes")


def main():
    """Main render pipeline."""
    print("[Frank] ========================================")
    print("[Frank] Frank Rendering Engine — render_gltf.py")
    print("[Frank] ========================================")

    # Parse arguments
    input_file, output_file, render_settings = parse_arguments()
    print(f"[Frank] Input:  {input_file}")
    print(f"[Frank] Output: {output_file}")
    print(f"[Frank] Settings: {json.dumps(render_settings, indent=2)}")

    # Validate input file
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    # ─── 1. Clean scene manually (without resetting factory settings) ────
    print("[Frank] Step 1: Cleaning scene...")
    clean_scene()

    # ─── 2. Import model (.glb, .gltf only) ─────────────────────────
    print(f"[Frank] Step 2: Importing model from {input_file}...")
    
    ext = os.path.splitext(input_file)[1].lower()
    abs_path = os.path.abspath(input_file)
    
    # Validar formato do arquivo
    if ext not in [".glb", ".gltf", ".obj", ".dae", ".skp"]:
        raise RuntimeError(
            f"Unsupported file format: {ext}. "
            f"Please convert your file to .glb, .gltf, .obj, or .dae format before uploading."
        )
    
    # Salva o CWD atual e muda para a pasta de uploads temporários
    old_cwd = os.getcwd()
    os.chdir(os.path.dirname(abs_path))
    
    try:
        # Importar arquivo baseado na extensão
        if ext in [".glb", ".gltf"]:
            print(f"[Frank] Importing {ext.upper()} file...")
            bpy.ops.import_scene.gltf(filepath=abs_path)
            print(f"[Frank] Successfully imported {ext.upper()} file")
        elif ext == ".obj":
            print(f"[Frank] Importing OBJ file...")
            bpy.ops.wm.obj_import(filepath=abs_path)
            print(f"[Frank] Successfully imported OBJ file")
        elif ext == ".dae":
            print(f"[Frank] Importing DAE (Collada) file...")
            bpy.ops.wm.collada_import(filepath=abs_path)
            print(f"[Frank] Successfully imported DAE file")
        elif ext == ".skp":
            print("[Frank] Importing SKP (SketchUp) file...")
            _import_skp(abs_path)
            print("[Frank] Successfully imported SKP file")
    finally:
        os.chdir(old_cwd)

    # Count imported objects
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    print(f"[Frank] Imported {len(mesh_objects)} mesh objects")

    if not mesh_objects:
        raise RuntimeError("No mesh objects found in the imported file")

    # ─── 3. Configure render engine ─────────────────────────────────
    print("[Frank] Step 3: Configuring Cycles engine...")
    scene = bpy.context.scene

    device = render_settings.get("device", "CPU")
    samples = render_settings.get("samples", 64)
    engine = render_settings.get("engine", "CYCLES")
    configure_render_engine(scene, device=device, samples=samples, engine=engine)

    # ─── 4. Set resolution ──────────────────────────────────────────
    print("[Frank] Step 4: Setting resolution...")
    resolution_x = render_settings.get("resolution_x", 1920)
    resolution_y = render_settings.get("resolution_y", 1080)

    scene.render.resolution_x = resolution_x
    scene.render.resolution_y = resolution_y
    scene.render.resolution_percentage = 100

    # Output format
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"

    print(f"[Frank] Resolution: {resolution_x}x{resolution_y}")

    # ─── 5. Setup camera ───────────────────────────────────────────
    print("[Frank] Step 5: Setting up camera...")
    camera_position = render_settings.get("camera_position")
    camera_target = render_settings.get("camera_target")
    camera_angle = render_settings.get("camera_angle", "auto")

    if camera_position and camera_target:
        # Custom camera from 3D preview viewer
        camera_fov = render_settings.get("camera_fov", 60)
        print(f"[Frank] Using custom camera from 3D preview")
        setup_custom_camera(
            scene,
            position=camera_position,
            target=camera_target,
            fov=camera_fov,
        )
    else:
        # Preset camera angle (auto, front, top, side, perspective)
        auto_frame_camera(scene, camera_angle=camera_angle)

    # ─── 6. Setup lighting ──────────────────────────────────────────
    print("[Frank] Step 6: Setting up lighting...")
    center, dimensions = get_scene_bounds(mesh_objects)
    max_dim = max(dimensions.x, dimensions.y, dimensions.z)
    setup_three_point_lighting(scene, center, max_dim)

    # ─── 7. Setup environment ───────────────────────────────────────
    print("[Frank] Step 7: Setting up environment...")
    setup_environment(scene, use_gradient=True)

    # ─── 8. Apply material overrides / auto-material ─────────────────
    material_overrides = render_settings.get("material_overrides")
    textures_dir = render_settings.get("textures_dir")
    
    if material_overrides:
        print(f"[Frank] Step 8: Applying material override(s): {material_overrides}")
        _apply_material_overrides(material_overrides, textures_dir=textures_dir)
    else:
        # Auto-material: if meshes have no materials, apply a default PBR
        _apply_default_material_if_needed()

    # ─── 9. Render ──────────────────────────────────────────────────
    print("[Frank] Step 9: Rendering...")
    print(f"[Frank] Samples: {samples} | Device: {scene.cycles.device}")

    # Set output path
    abs_output = os.path.abspath(output_file)
    scene.render.filepath = abs_output
    scene.render.use_file_extension = False  # Don't add .png again if it's already there

    print(f"[Frank] Target path: {abs_output}")

    # Execute render
    bpy.ops.render.render(write_still=True)

    # ─── 10. Verify output ──────────────────────────────────────────
    if os.path.exists(output_file):
        size = os.path.getsize(output_file)
        print(f"[Frank] ✅ Render complete! Output: {output_file} ({size} bytes)")
    else:
        raise RuntimeError(f"Render did not produce output file: {output_file}")

    print("[Frank] ========================================")
    print("[Frank] Done!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[Frank] ❌ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)