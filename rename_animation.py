import bpy

# Find the armature by its name
armature = bpy.data.objects.get("Armature")

# Select the armature
armature.select_set(True)
bpy.context.view_layer.objects.active = armature

# Remove unwanted character in each action name of the selected armature
for action in bpy.data.actions:
    action.name = action.name.replace("Armature|", "")
    action.name = action.name.replace("|Base Layer", "")
    action.name = action.name.replace("|Base La", "")
    action.name = action.name.replace("_simple.generated", "")
    action.name = action.name.replace("_spirit.generated", "")
    action.name = action.name.lower()