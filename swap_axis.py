import bpy

# Find the armature by its name
armature = bpy.data.objects.get("Armature")

# Select the armature
armature.select_set(True)
bpy.context.view_layer.objects.active = armature

# Iterate through all actions
#for action in bpy.data.actions:
#    for curve in action.fcurves:
#        print(curve.data_path, curve.array_index)
#        for keyframe in curve.keyframe_points:
#            print(keyframe.co)

bone = armature.pose.bones.get("Root_Joint")
bone_location_path = bone.path_from_id("location")
bone_rotation_path = bone.path_from_id("rotation_quaternion")
for action in bpy.data.actions:
    total_keyframes = len(action.fcurves.find(bone_location_path).keyframe_points)
    location_keyframes_y = action.fcurves.find(bone_location_path, index=1).keyframe_points
    location_keyframes_z = action.fcurves.find(bone_location_path, index=2).keyframe_points
    rotation_keyframes_y = action.fcurves.find(bone_rotation_path, index=2).keyframe_points
    rotation_keyframes_z = action.fcurves.find(bone_rotation_path, index=3).keyframe_points
    print("action:", action.name, ",total_keyframes:", total_keyframes)
    for i in range(total_keyframes):
        temp_location = location_keyframes_y[i].co.y
        location_keyframes_y[i].co.y = -location_keyframes_z[i].co.y
        location_keyframes_z[i].co.y = temp_location
        temp_rotation = rotation_keyframes_y[i].co.y
        rotation_keyframes_y[i].co.y = -rotation_keyframes_z[i].co.y
        rotation_keyframes_z[i].co.y = temp_rotation
        
        
    