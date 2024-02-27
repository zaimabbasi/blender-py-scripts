import bpy

# Set the scale factor
scale_factor = 100

# Find the armature by its name
armature = bpy.data.objects.get("Armature")

# Select the armature
#bpy.ops.object.select_all(action='DESELECT') # Unwanted line I guess
armature.select_set(True)
bpy.context.view_layer.objects.active = armature

# Scale the location fcurves of the selected armature
for action in bpy.data.actions:
    for fcurve in action.fcurves:
        if fcurve.data_path.endswith("location"):
            for keyframe_point in fcurve.keyframe_points:
                keyframe_point.co.y *= scale_factor