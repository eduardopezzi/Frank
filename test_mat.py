import bpy
import sys

bpy.ops.wm.obj_import(filepath="/app/uploads/medieval-house-2.obj")
mat = bpy.data.materials.get("Wood__Wood_jpg")
if not mat:
    print("Material not found!")
    sys.exit()

nodes = mat.node_tree.nodes
principled = next((n for n in nodes if n.type == "BSDF_PRINCIPLED"), None)
if principled:
    for link in mat.node_tree.links:
        if link.to_node == principled:
            print(f"{link.from_node.name} ({link.from_node.type}) -> Principled BSDF [{link.to_socket.name}]")
            if link.from_node.type == "BUMP":
                bump = link.from_node
                print(f"Bump Distance: {bump.inputs['Distance'].default_value}")
                print(f"Bump Strength: {bump.inputs['Strength'].default_value}")
