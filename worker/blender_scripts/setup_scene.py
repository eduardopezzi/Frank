"""
Blender scene setup helpers.

These functions are designed to run inside Blender's Python environment (bpy).
They handle camera auto-framing, professional lighting, and PBR material application.

IMPORTANT: This file is executed by Blender's embedded Python interpreter,
not by the system Python. It has access to the `bpy` module.
"""

import math


def get_scene_bounds(objects):
    """
    Calculate the bounding box that encompasses all mesh objects in the scene.
    Returns (center, dimensions) as Vector-like tuples.
    """
    import bpy
    from mathutils import Vector

    min_coord = Vector((float("inf"), float("inf"), float("inf")))
    max_coord = Vector((float("-inf"), float("-inf"), float("-inf")))

    has_geometry = False

    for obj in objects:
        if obj.type != "MESH":
            continue
        has_geometry = True

        # Get world-space bounding box corners
        for corner in obj.bound_box:
            world_corner = obj.matrix_world @ Vector(corner)
            min_coord.x = min(min_coord.x, world_corner.x)
            min_coord.y = min(min_coord.y, world_corner.y)
            min_coord.z = min(min_coord.z, world_corner.z)
            max_coord.x = max(max_coord.x, world_corner.x)
            max_coord.y = max(max_coord.y, world_corner.y)
            max_coord.z = max(max_coord.z, world_corner.z)

    if not has_geometry:
        return Vector((0, 0, 0)), Vector((2, 2, 2))

    center = (min_coord + max_coord) / 2
    dimensions = max_coord - min_coord

    return center, dimensions


def auto_frame_camera(scene, camera_angle="auto"):
    """
    Position the camera to frame all objects in the scene.
    Uses the bounding box to calculate the optimal distance and angle.

    Args:
        scene: bpy.context.scene
        camera_angle: Preset string (auto, front, top, side, perspective)
    """
    import bpy
    from mathutils import Vector

    objects = [obj for obj in scene.objects if obj.type == "MESH"]
    center, dimensions = get_scene_bounds(objects)

    # Calculate the maximum dimension for framing distance
    max_dim = max(dimensions.x, dimensions.y, dimensions.z)
    if max_dim == 0:
        max_dim = 2.0

    # Distance multiplier to ensure the model fits in frame
    distance = max_dim * 2.0

    # Camera angle presets
    angle_presets = {
        "front": (0, -distance, center.z),
        "top": (center.x, center.y, distance * 1.5),
        "side": (distance, 0, center.z),
        "perspective": (distance * 0.8, -distance * 0.8, distance * 0.6),
        "auto": (distance * 0.7, -distance * 0.7, distance * 0.5 + center.z),
    }

    # Create camera
    cam_data = bpy.data.cameras.new("RenderCamera")
    cam_data.lens = 50  # 50mm lens (standard)
    cam_data.clip_start = 0.1
    cam_data.clip_end = max_dim * 10

    cam_obj = bpy.data.objects.new("RenderCamera", cam_data)
    scene.collection.objects.link(cam_obj)
    scene.camera = cam_obj

    # Position camera
    preset = camera_angle if camera_angle in angle_presets else "auto"
    cam_obj.location = Vector(angle_presets[preset])

    # Point camera at center of scene
    direction = center - cam_obj.location
    rot_quat = direction.to_track_quat("-Z", "Y")
    cam_obj.rotation_euler = rot_quat.to_euler()

    return cam_obj


def setup_custom_camera(scene, position, target, fov=60):
    """
    Create camera with exact position and look-at target from Three.js viewer.
    
    The position and target are already in Blender coordinates (Z-up),
    converted from Three.js (Y-up) by the frontend.

    Args:
        scene: bpy.context.scene
        position: [x, y, z] camera position in Blender coordinates
        target: [x, y, z] look-at target in Blender coordinates
        fov: Field of view in degrees
    """
    import bpy
    from mathutils import Vector

    # Calculate scene bounds for clipping planes
    objects = [obj for obj in scene.objects if obj.type == "MESH"]
    _, dimensions = get_scene_bounds(objects)
    max_dim = max(dimensions.x, dimensions.y, dimensions.z)
    if max_dim == 0:
        max_dim = 2.0

    # Create camera with FOV
    cam_data = bpy.data.cameras.new("FrankCamera")
    cam_data.lens_unit = 'FOV'
    cam_data.angle = math.radians(fov)
    cam_data.clip_start = max_dim * 0.001
    cam_data.clip_end = max_dim * 100

    cam_obj = bpy.data.objects.new("FrankCamera", cam_data)
    scene.collection.objects.link(cam_obj)
    scene.camera = cam_obj

    # Set position
    cam_obj.location = Vector(position)

    # Point camera at target using track_quat (same approach as auto_frame_camera)
    target_vec = Vector(target)
    direction = target_vec - cam_obj.location
    rot_quat = direction.to_track_quat("-Z", "Y")
    cam_obj.rotation_euler = rot_quat.to_euler()

    print(f"[Frank] Custom camera: pos={position}, target={target}, fov={fov}°")

    return cam_obj


def setup_three_point_lighting(scene, center, max_dim):
    """
    Create a professional 3-point lighting setup.

    - Key light: Main light, slightly above and to the side
    - Fill light: Softer, opposite side, fills shadows
    - Rim light: Behind the subject, creates edge separation

    Args:
        scene: bpy.context.scene
        center: Center of the scene objects
        max_dim: Maximum dimension of the scene for scaling
    """
    import bpy
    from mathutils import Vector

    distance = max_dim * 2.5
    lights = []

    # Key Light — warm, strong, 45° above and to the right
    key_data = bpy.data.lights.new(name="KeyLight", type="AREA")
    key_data.energy = max_dim * 200
    key_data.size = max_dim * 0.8
    key_data.color = (1.0, 0.95, 0.9)  # Slightly warm

    key_obj = bpy.data.objects.new("KeyLight", key_data)
    scene.collection.objects.link(key_obj)
    key_obj.location = Vector((
        center.x + distance * 0.7,
        center.y - distance * 0.5,
        center.z + distance * 0.8,
    ))
    # Point at center
    direction = center - key_obj.location
    key_obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    lights.append(key_obj)

    # Fill Light — cooler, softer, opposite side
    fill_data = bpy.data.lights.new(name="FillLight", type="AREA")
    fill_data.energy = max_dim * 80
    fill_data.size = max_dim * 1.2
    fill_data.color = (0.9, 0.93, 1.0)  # Slightly cool

    fill_obj = bpy.data.objects.new("FillLight", fill_data)
    scene.collection.objects.link(fill_obj)
    fill_obj.location = Vector((
        center.x - distance * 0.6,
        center.y - distance * 0.3,
        center.z + distance * 0.4,
    ))
    direction = center - fill_obj.location
    fill_obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    lights.append(fill_obj)

    # Rim Light — behind and above, for edge separation
    rim_data = bpy.data.lights.new(name="RimLight", type="AREA")
    rim_data.energy = max_dim * 120
    rim_data.size = max_dim * 0.5
    rim_data.color = (1.0, 1.0, 1.0)

    rim_obj = bpy.data.objects.new("RimLight", rim_data)
    scene.collection.objects.link(rim_obj)
    rim_obj.location = Vector((
        center.x - distance * 0.3,
        center.y + distance * 0.6,
        center.z + distance * 0.9,
    ))
    direction = center - rim_obj.location
    rim_obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    lights.append(rim_obj)

    # Global Top Light — ensures interiors aren't pitch black
    global_data = bpy.data.lights.new(name="GlobalTopLight", type="AREA")
    global_data.energy = max_dim * 50
    global_data.size = max_dim * 2.0
    global_data.color = (1.0, 1.0, 1.0)
    
    global_obj = bpy.data.objects.new("GlobalTopLight", global_data)
    scene.collection.objects.link(global_obj)
    global_obj.location = Vector((center.x, center.y, center.z + distance * 1.5))
    global_obj.rotation_euler = (0, 0, 0) # Point straight down
    lights.append(global_obj)

    return lights


def setup_environment(scene, use_gradient=True):
    """
    Set up the world environment for rendering.
    Uses Nishita Sky by default for architectural realism.
    """
    import bpy

    world = bpy.data.worlds.new("RenderWorld")
    scene.world = world
    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links

    # Clear default nodes
    nodes.clear()

    output_node = nodes.new("ShaderNodeOutputWorld")
    background = nodes.new("ShaderNodeBackground")
    background.inputs["Strength"].default_value = 1.0
    
    # --- Nishita Sky (Better for Architecture) ---
    sky = nodes.new("ShaderNodeTexSky")
    sky.sky_type = 'NISHITA'
    sky.sun_size = 0.545 # Real sun size in deg
    sky.sun_intensity = 1.0
    sky.sun_elevation = 0.45 # Golden hour look
    sky.sun_rotation = 1.57
    sky.altitude = 0.0
    sky.air_density = 1.0
    sky.dust_density = 1.0
    sky.ozone_density = 1.0
    
    links.new(sky.outputs["Color"], background.inputs["Color"])
    links.new(background.outputs["Background"], output_node.inputs["Surface"])
    
    # High Quality Engine Settings
    if scene.render.engine == 'CYCLES':
        scene.cycles.use_fast_gi = True
        scene.cycles.fast_gi_method = 'ADD'
        scene.cycles.ao_bounces = 2
        scene.cycles.max_bounces = 12
        scene.cycles.diffuse_bounces = 4
        scene.cycles.glossy_bounces = 4
        scene.cycles.transparent_max_bounces = 8
    else: # EEVEE
        scene.eevee.use_gtao = True
        scene.eevee.gtao_distance = 2.0
        scene.eevee.use_ssr = True # Screen Space Reflections
        scene.eevee.use_bloom = True


def apply_pbr_materials(materials_data):
    """
    Apply PBR material overrides from the catalog JSON.

    Args:
        materials_data: List of material dicts with PBR properties.
                        Each should have 'name' or 'sketchup_material_name'
                        to match existing materials in the scene.
    """
    import bpy

    # Global fix: reduce bump strength/distance for all bump nodes that were auto-generated by importers.
    # The default OBJ importer often leaves Distance at 1.0 (1 meter), causing pitch-black rendering artifacts
    # when an sRGB diffuse texture is improperly used as a bump map by older CAD/SketchUp exporters.
    for m in bpy.data.materials:
        if m.use_nodes:
            for node in m.node_tree.nodes:
                if node.type == "BUMP":
                    if node.inputs["Distance"].default_value >= 1.0:
                        node.inputs["Distance"].default_value = 0.02
                        node.inputs["Strength"].default_value = 0.5

    for mat_data in materials_data:
        pbr = mat_data.get("pbr_properties", {})
        target_names = []

        # Try to match by SketchUp material name first
        if mat_data.get("sketchup_material_name"):
            target_names.append(mat_data["sketchup_material_name"])
        if mat_data.get("name"):
            target_names.append(mat_data["name"])
        if mat_data.get("material_id"):
            target_names.append(mat_data["material_id"])

        for mat_name in target_names:
            mat = bpy.data.materials.get(mat_name)
            if mat is None:
                continue

            # Ensure material uses nodes
            mat.use_nodes = True
            nodes = mat.node_tree.nodes

            # Find or create Principled BSDF
            principled = None
            for node in nodes:
                if node.type == "BSDF_PRINCIPLED":
                    principled = node
                    break

            if principled is None:
                principled = nodes.new("ShaderNodeBsdfPrincipled")

            def clear_socket_links(socket_name):
                if socket_name in principled.inputs:
                    socket = principled.inputs[socket_name]
                    for link in list(mat.node_tree.links):
                        if link.to_socket == socket:
                            mat.node_tree.links.remove(link)

            # Apply PBR properties
            if "base_color" in pbr:
                color = pbr["base_color"]
                if len(color) == 3:
                    color = (*color, 1.0)
                principled.inputs["Base Color"].default_value = color

            if "metallic" in pbr:
                clear_socket_links("Metallic")
                principled.inputs["Metallic"].default_value = pbr["metallic"]

            if "roughness" in pbr:
                clear_socket_links("Roughness")
                principled.inputs["Roughness"].default_value = pbr["roughness"]

            if "emission" in pbr and pbr["emission"] > 0:
                if "emission_color" in pbr:
                    ec = pbr["emission_color"]
                    principled.inputs["Emission Color"].default_value = (*ec, 1.0)
                principled.inputs["Emission Strength"].default_value = pbr["emission"]

            if "alpha" in pbr and pbr["alpha"] < 1.0:
                clear_socket_links("Alpha")
                principled.inputs["Alpha"].default_value = pbr["alpha"]
                mat.blend_method = "HASHED"

            if "transmission" in pbr and pbr["transmission"] > 0:
                clear_socket_links("Transmission Weight")
                principled.inputs["Transmission Weight"].default_value = pbr["transmission"]

            if "ior" in pbr:
                principled.inputs["IOR"].default_value = pbr["ior"]

            break  # Found and applied, move to next material


def configure_render_engine(scene, device="CPU", samples=64):
    """
    Configure the Cycles render engine with optimal settings.
    Falls back to CPU if GPU is requested but not available.

    Args:
        scene: bpy.context.scene
        device: "CPU" or "GPU"
        samples: Number of render samples
    """
    import bpy

    scene.render.engine = "CYCLES"
    scene.cycles.samples = samples
    scene.cycles.use_denoising = True
    scene.cycles.preview_samples = max(16, samples // 4)

    # Transparent background (useful for compositing)
    scene.render.film_transparent = False

    # Color management
    scene.view_settings.view_transform = "Filmic"
    scene.view_settings.look = "Medium Contrast"

    if device == "GPU":
        try:
            prefs = bpy.context.preferences.addons["cycles"].preferences

            # Try CUDA first, then OptiX, then Metal (macOS)
            for compute_type in ["OPTIX", "CUDA", "METAL", "HIP"]:
                try:
                    prefs.compute_device_type = compute_type
                    prefs.get_devices()

                    # Enable all available devices
                    for dev in prefs.devices:
                        dev.use = True

                    scene.cycles.device = "GPU"
                    print(f"[Frank] Using GPU with {compute_type}")
                    return
                except Exception:
                    continue

            # Fallback to CPU
            print("[Frank] No GPU available, falling back to CPU")
            scene.cycles.device = "CPU"
        except Exception as e:
            print(f"[Frank] GPU setup failed: {e}, using CPU")
            scene.cycles.device = "CPU"
    else:
        scene.cycles.device = "CPU"
        print("[Frank] Using CPU rendering")
