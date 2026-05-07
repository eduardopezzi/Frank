import bpy
import os
import sys
import json

def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    for block in bpy.data.meshes:
        if block.users == 0: bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        if block.users == 0: bpy.data.materials.remove(block)
    for block in bpy.data.images:
        if block.users == 0: bpy.data.images.remove(block)

def _import_skp(filepath):
    import addon_utils
    addon_module = "sketchup_importer"
    addon_path = "/usr/local/blender/4.0/scripts/addons"
    if addon_path not in sys.path: sys.path.insert(0, addon_path)
    addon_utils.modules(refresh=True)
    if not addon_utils.check(addon_module)[0]:
        bpy.ops.preferences.addon_enable(module=addon_module)
    bpy.ops.import_scene.skp(filepath=filepath)

def main():
    argv = sys.argv
    if "--" not in argv: return
    args = argv[argv.index("--") + 1:]
    input_file = args[0]
    output_file = args[1]

    clean_scene()
    
    ext = os.path.splitext(input_file)[1].lower()
    if ext == ".skp":
        _import_skp(input_file)
    elif ext == ".obj":
        bpy.ops.wm.obj_import(filepath=input_file)
    elif ext == ".dae":
        bpy.ops.wm.collada_import(filepath=input_file)
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=input_file, use_custom_normals=True)
        # Clean up non-mesh objects imported from FBX
        for obj in bpy.context.scene.objects:
            if obj.type in ['CAMERA', 'LIGHT', 'ARMATURE']:
                bpy.data.objects.remove(obj, do_unlink=True)
    
    sanitize_materials()

def sanitize_materials():
    """Remove nodes with missing images to avoid magenta (pink) materials."""
    for mat in bpy.data.materials:
        if not mat.use_nodes: continue
        nodes = mat.node_tree.nodes
        for node in nodes:
            if node.type == 'TEX_IMAGE':
                if not node.image or not os.path.exists(bpy.path.abspath(node.image.filepath)):
                    print(f"[Frank] Removing missing texture node from material: {mat.name}")
                    nodes.remove(node)
    
    # Export as GLB for browser
    bpy.ops.export_scene.gltf(
        filepath=output_file,
        export_format='GLB',
        export_apply=True,
        export_images='EMBED'
    )
    print(f"Exported to {output_file}")

if __name__ == "__main__":
    main()
