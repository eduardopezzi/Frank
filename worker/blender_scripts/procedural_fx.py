"""
Blender script for procedural material enhancements.
Handles tiling variation, dirt, and edge wear.
"""
import bpy
import math

def add_tiling_variation(mat, scale=5.0, factor=0.1):
    """
    Adds a subtle noise overlay to break repeating tiling patterns.
    """
    if not mat.use_nodes:
        mat.use_nodes = True
    
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Find Principled BSDF
    principled = None
    for n in nodes:
        if n.type == 'BSDF_PRINCIPLED':
            principled = n
            break
            
    if not principled:
        return

    # Create Noise and Mix nodes
    node_noise = nodes.new('ShaderNodeTexNoise')
    node_noise.inputs['Scale'].default_value = scale
    node_noise.inputs['Detail'].default_value = 15.0
    
    node_mix = nodes.new('ShaderNodeMix')
    node_mix.data_type = 'RGBA'
    node_mix.blend_type = 'OVERLAY'
    node_mix.inputs['Factor'].default_value = factor

    # Handle existing Base Color link
    base_color_input = principled.inputs['Base Color']
    if base_color_input.links:
        old_link = base_color_input.links[0]
        source_socket = old_link.from_socket
        
        links.new(source_socket, node_mix.inputs['A'])
        links.new(node_noise.outputs['Color'], node_mix.inputs['B'])
        links.new(node_mix.outputs['Result'], base_color_input)
    else:
        # If no texture, just vary the default color
        node_mix.inputs['A'].default_value = base_color_input.default_value
        links.new(node_noise.outputs['Color'], node_mix.inputs['B'])
        links.new(node_mix.outputs['Result'], base_color_input)

def add_dirt_and_wear(mat, dirt_color=(0.05, 0.03, 0.01, 1.0), intensity=0.5):
    """
    Uses Ambient Occlusion to add procedural dirt in corners.
    """
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    principled = next(n for n in nodes if n.type == 'BSDF_PRINCIPLED')
    
    node_ao = nodes.new('ShaderNodeAmbientOcclusion')
    node_ao.inputs['Distance'].default_value = 0.2
    
    node_ramp = nodes.new('ShaderNodeValToRGB')
    node_ramp.color_ramp.elements[0].position = 0.4
    node_ramp.color_ramp.elements[1].position = 0.7
    
    node_mix = nodes.new('ShaderNodeMix')
    node_mix.data_type = 'RGBA'
    node_mix.blend_type = 'MULTIPLY'
    node_mix.inputs['Factor'].default_value = intensity
    
    links.new(node_ao.outputs['Color'], node_ramp.inputs['Fac'])
    
    base_color_input = principled.inputs['Base Color']
    if base_color_input.links:
        source_socket = base_color_input.links[0].from_socket
        links.new(source_socket, node_mix.inputs['A'])
        links.new(node_ramp.outputs['Color'], node_mix.inputs['B'])
        links.new(node_mix.outputs['Result'], base_color_input)

def auto_scale_uv(obj, target_density=1.0):
    """
    Adjusts UV scale based on object bounding box to maintain consistent texture density.
    """
    if obj.type != 'MESH':
        return
        
    dims = obj.dimensions
    scale_factor = max(dims.x, dims.y, dims.z) * target_density
    
    for slot in obj.material_slots:
        mat = slot.material
        if not mat or not mat.use_nodes: continue
        
        nodes = mat.node_tree.nodes
        mapping = next((n for n in nodes if n.type == 'MAPPING'), None)
        
        if not mapping:
            # Create Mapping and Texture Coordinate if missing
            tex_coord = nodes.new('ShaderNodeTexCoord')
            mapping = nodes.new('ShaderNodeMapping')
            links = mat.node_tree.links
            links.new(tex_coord.outputs['UV'], mapping.inputs['Vector'])
            
            # Connect mapping to all images
            for n in nodes:
                if n.type == 'TEX_IMAGE':
                    links.new(mapping.outputs['Vector'], n.inputs['Vector'])
        
        mapping.inputs['Scale'].default_value = (scale_factor, scale_factor, scale_factor)

# Integration with main pipeline
def apply_advanced_realism(obj_list):
    for obj in obj_list:
        auto_scale_uv(obj)
        for slot in obj.material_slots:
            if slot.material:
                add_tiling_variation(slot.material)
                add_dirt_and_wear(slot.material)
