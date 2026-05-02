"""
Blender Cycles render script for glTF/GLB models.

This script is executed by Blender via CLI:
    blender -b --factory-startup -P render_gltf.py -- input.glb output.png settings.json

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
    settings_json = args[2] if len(args) > 2 else "{}"

    try:
        render_settings = json.loads(settings_json)
    except json.JSONDecodeError:
        print(f"[Cycles] Warning: Could not parse settings JSON, using defaults")
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
    
    print("[Cycles] Scene cleaned (objects, meshes, materials, images, lights, cameras)")


def main():
    """Main render pipeline."""
    print("[Cycles] ========================================")
    print("[Cycles] Cycles Rendering Engine — render_gltf.py")
    print("[Cycles] ========================================")

    # Parse arguments
    input_file, output_file, render_settings = parse_arguments()
    print(f"[Cycles] Input:  {input_file}")
    print(f"[Cycles] Output: {output_file}")
    print(f"[Cycles] Settings: {json.dumps(render_settings, indent=2)}")

    # Validate input file
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    # ─── 1. Clean scene manually (without resetting factory settings) ────
    print("[Cycles] Step 1: Cleaning scene...")
    clean_scene()

    # ─── 2. Import model (.glb, .gltf only) ─────────────────────────
    print(f"[Cycles] Step 2: Importing model from {input_file}...")
    
    ext = os.path.splitext(input_file)[1].lower()
    abs_path = os.path.abspath(input_file)
    
    # Validar formato do arquivo
    if ext not in [".glb", ".gltf", ".obj", ".dae", ".skp"]:
        raise RuntimeError(
            f"Unsupported file format: {ext}. "
            f"Please convert your file to .glb, .gltf, .obj, or .dae format before uploading."
        )
    
    # Importar arquivo baseado na extensão
    if ext in [".glb", ".gltf"]:
        print(f"[Cycles] Importing {ext.upper()} file...")
        bpy.ops.import_scene.gltf(filepath=abs_path)
        print(f"[Cycles] Successfully imported {ext.upper()} file")
    elif ext == ".obj":
        print(f"[Cycles] Importing OBJ file...")
        bpy.ops.wm.obj_import(filepath=abs_path)
        print(f"[Cycles] Successfully imported OBJ file")
    elif ext == ".dae":
        print(f"[Cycles] Importing DAE (Collada) file...")
        bpy.ops.wm.collada_import(filepath=abs_path)
        print(f"[Cycles] Successfully imported DAE file")
    elif ext == ".skp":
        raise RuntimeError(
            "SKP files are not directly supported by Blender. "
            "Please convert your SketchUp file to .glb, .gltf, .obj, or .dae format before uploading. "
            "\n\nHow to convert:\n"
            "1. Open your .skp file in SketchUp\n"
            "2. Go to File > Export > 3D Model\n"
            "3. Select 'glTF 2.0 (.glb)' format\n"
            "4. Save and upload the .glb file\n\n"
            "Alternative: Use online converters like convertio.co or AnyConv"
        )

    # Count imported objects
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
    print(f"[Cycles] Imported {len(mesh_objects)} mesh objects")

    if not mesh_objects:
        raise RuntimeError("No mesh objects found in the imported file")

    # ─── 3. Configure render engine ─────────────────────────────────
    print("[Cycles] Step 3: Configuring Cycles engine...")
    scene = bpy.context.scene

    device = render_settings.get("device", "CPU")
    samples = render_settings.get("samples", 64)
    configure_render_engine(scene, device=device, samples=samples)

    # ─── 4. Set resolution ──────────────────────────────────────────
    print("[Cycles] Step 4: Setting resolution...")
    resolution_x = render_settings.get("resolution_x", 1920)
    resolution_y = render_settings.get("resolution_y", 1080)

    scene.render.resolution_x = resolution_x
    scene.render.resolution_y = resolution_y
    scene.render.resolution_percentage = 100

    # Output format
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"

    print(f"[Cycles] Resolution: {resolution_x}x{resolution_y}")

    # ─── 5. Setup camera ───────────────────────────────────────────
    print("[Cycles] Step 5: Setting up camera...")
    camera_angle = render_settings.get("camera_angle", "auto")
    auto_frame_camera(scene, camera_angle=camera_angle)

    # ─── 6. Setup lighting ──────────────────────────────────────────
    print("[Cycles] Step 6: Setting up lighting...")
    center, dimensions = get_scene_bounds(mesh_objects)
    max_dim = max(dimensions.x, dimensions.y, dimensions.z)
    setup_three_point_lighting(scene, center, max_dim)

    # ─── 7. Setup environment ───────────────────────────────────────
    print("[Cycles] Step 7: Setting up environment...")
    setup_environment(scene, use_gradient=True)

    # ─── 8. Apply material overrides ────────────────────────────────
    material_overrides = render_settings.get("material_overrides")
    if material_overrides:
        print(f"[Cycles] Step 8: Applying {len(material_overrides)} material overrides...")
        apply_pbr_materials(material_overrides)
    else:
        print("[Cycles] Step 8: No material overrides (using imported materials)")

    # ─── 9. Render ──────────────────────────────────────────────────
    print("[Cycles] Step 9: Rendering...")
    print(f"[Cycles] Samples: {samples} | Device: {scene.cycles.device}")

    # Set output path
    abs_output = os.path.abspath(output_file)
    scene.render.filepath = abs_output
    scene.render.use_file_extension = False  # Don't add .png again if it's already there

    print(f"[Cycles] Target path: {abs_output}")

    # Execute render
    bpy.ops.render.render(write_still=True)

    # ─── 10. Verify output ──────────────────────────────────────────
    if os.path.exists(output_file):
        size = os.path.getsize(output_file)
        print(f"[Cycles] ✅ Render complete! Output: {output_file} ({size} bytes)")
    else:
        raise RuntimeError(f"Render did not produce output file: {output_file}")

    print("[Cycles] ========================================")
    print("[Cycles] Done!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[Cycles] ❌ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
