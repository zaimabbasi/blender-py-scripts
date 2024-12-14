import bpy

context = bpy.context
obj = context.object

# add as many pairs in the list
bone_name_list = [("bone_name", "bone_new_name")]

for bone_name, bone_new_name in bone_name_list:
    # get the pose bone with name
    pb = obj.pose.bones.get(bone_name)
    # continue if no bone of that name
    if pb is None:
        continue
    # rename
    pb.name = pb.name.replace(bone_name, bone_new_name)
    
    
# Find the armature by its name
armature = bpy.data.objects.get("Armature")

# Select the armature
armature.select_set(True)
bpy.context.view_layer.objects.active = armature

for action in bpy.data.actions:
    #these so called action groups are the bones, ie one group contains all fcurves of one bone
    for group in action.groups:
        for bone_name, bone_new_name in bone_name_list:
            if group.name == bone_name:
                group.name = bone_new_name
                for fcurve in group.channels:
                    fcurve.data_path = fcurve.data_path.replace(bone_name, bone_new_name)
