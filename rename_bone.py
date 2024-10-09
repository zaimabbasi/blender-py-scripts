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