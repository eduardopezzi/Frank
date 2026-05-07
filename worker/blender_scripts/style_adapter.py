"""
Blender script to adapt scene lighting and mood based on reference analysis.
Sets HDRI, Sun, Exposure and Color Management.
"""
import bpy
import math

def apply_style_profile(profile):
    """
    Applies extracted style parameters to the Blender scene.
    
    Args:
        profile: Dict containing palette, lighting, and style_tags.
    """
    scene = bpy.context.scene
    lighting = profile.get("lighting", {})
    palette = profile.get("palette", [])
    
    # 1. Color Management (Filmic/AgX)
    scene.view_settings.view_transform = 'Filmic'
    
    l_type = lighting.get("type", "overcast")
    if l_type == "sunny":
        scene.view_settings.look = 'High Contrast'
        scene.view_settings.exposure = -1.0 # Bright sun needs lower exposure
    elif l_type == "warm/golden":
        scene.view_settings.look = 'Medium High Contrast'
        scene.view_settings.exposure = 0.5
    else:
        scene.view_settings.look = 'Medium Contrast'
        scene.view_settings.exposure = 0.0

    # 2. Lighting Setup
    if l_type == "sunny":
        setup_sun(strength=5.0, elevation=45.0)
    elif l_type == "warm/golden":
        setup_sun(strength=3.0, elevation=15.0, color=palette[0] if palette else None)
    else:
        setup_sun(strength=1.0, elevation=90.0)

    # 3. Global Color Tint (Optional - using dominant color in post-processing)
    if palette:
        main_color = palette[0] # [R, G, B]
        # Normalize to 0-1
        col = [c/255.0 for c in main_color]
        # Apply to a global mix or specific lights
        # (Implementation depends on scene structure)

def setup_sun(strength=1.0, elevation=45.0, color=None):
    """
    Creates or updates a Sun light.
    """
    sun_obj = bpy.data.objects.get("StyleSun")
    if not sun_obj:
        sun_data = bpy.data.lights.new(name="StyleSun", type='SUN')
        sun_obj = bpy.data.objects.new(name="StyleSun", object_data=sun_data)
        bpy.context.collection.objects.link(sun_obj)
    
    sun_obj.data.energy = strength
    if color:
        # Convert RGB to sRGB for Blender
        sun_obj.data.color = [color[0]/255.0, color[1]/255.0, color[2]/255.0]
        
    # Set rotation based on elevation
    # Elevation 0 = horizontal, 90 = vertical
    angle = math.radians(90 - elevation)
    sun_obj.rotation_euler = (angle, 0, 0)

def match_hdri_category(lighting_type):
    """
    Logic to select HDRI path based on extracted mood.
    (Stub for integration with HDRI catalog)
    """
    categories = {
        "sunny": "clear_sky",
        "overcast": "cloudy",
        "night/dark": "night",
        "warm/golden": "sunset"
    }
    return categories.get(lighting_type, "overcast")
