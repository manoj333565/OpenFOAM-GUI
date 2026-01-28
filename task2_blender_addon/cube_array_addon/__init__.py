bl_info = {
    "name": "FOSSEE Cube Array Addon",
    "author": "FOSSEE",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > FOSSEE",
    "description": "Create and manage cube arrays",
    "category": "Object",
}

import bpy
import math
from bpy.props import IntProperty


# -------------------------------
# Operator: Create Cubes
# -------------------------------
class FOSSEE_OT_CreateCubes(bpy.types.Operator):
    bl_idname = "fossee.create_cubes"
    bl_label = "Create Cubes"

    def execute(self, context):
        N = context.scene.fossee_n

        if N < 1 or N > 20:
            self.report({'ERROR'}, "The number is out of range")
            bpy.context.window_manager.popup_menu(
                lambda self, context: self.layout.label(text="The number is out of range"),
                title="Error",
                    icon='ERROR'
    )
            return {'CANCELLED'}


        # Create / get collection
        col_name = "FOSSEE_Cubes"
        if col_name not in bpy.data.collections:
            cube_col = bpy.data.collections.new(col_name)
            context.scene.collection.children.link(cube_col)
        else:
            cube_col = bpy.data.collections[col_name]

        # Calculate grid size
        rows = math.ceil(math.sqrt(N))
        cols = math.ceil(N / rows)

        # Create cubes
        for i in range(N):
            x = i % cols
            y = i // cols
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x * 1, y * 1, 0))
            obj = context.active_object

            # Move cube to collection
            for col in obj.users_collection:
                col.objects.unlink(obj)
            cube_col.objects.link(obj)

        return {'FINISHED'}


# -------------------------------
# Operator: Delete Selected Cubes
# -------------------------------
class FOSSEE_OT_DeleteSelected(bpy.types.Operator):
    bl_idname = "fossee.delete_selected"
    bl_label = "Delete Selected Cubes"

    def execute(self, context):
        bpy.ops.object.delete()
        return {'FINISHED'}
    
# -------------------------------------------------------
class FOSSEE_OT_MergeMeshes(bpy.types.Operator):
    bl_idname = "object.fossee_merge_meshes"
    bl_label = "Merge Selected Meshes"
    bl_description = "Merge selected meshes with at least one common face"

    def execute(self, context):
        # Ensure object Mode 
        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode = 'OBJECT')
        selected = [obj for obj in context.selected_objects if obj.type == 'MESH']

        if len(selected) < 2:
            self.report({'ERROR'}, "Select at least two mesh objects")
            return {'CANCELLED'}

        # Make first object active
        context.view_layer.objects.active = selected[0]

        bpy.ops.object.transform_apply(
            location = True,
            rotation = True,
            scale = True
        )
        # Join meshes
        bpy.ops.object.join()

        # Enter edit mode
        bpy.ops.object.mode_set(mode='EDIT')

        # Merge common vertices
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold = 0.01)

        # Back to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        self.report({'INFO'}, "Meshes merged successfully")
        return {'FINISHED'}




# -------------------------------
# UI Panel
# -------------------------------
class FOSSEE_PT_Panel(bpy.types.Panel):
    bl_label = "FOSSEE Cube Tools"
    bl_idname = "FOSSEE_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "FOSSEE"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "fossee_n")
        layout.operator("fossee.create_cubes")
        layout.operator("fossee.delete_selected")

        layout.separator()
        layout.operator("object.fossee_merge_meshes", text="Merge Selected Meshes")



# -------------------------------
# Register
# -------------------------------
def register():
    bpy.utils.register_class(FOSSEE_OT_CreateCubes)
    bpy.utils.register_class(FOSSEE_OT_DeleteSelected)
    bpy.utils.register_class(FOSSEE_OT_MergeMeshes)
    bpy.utils.register_class(FOSSEE_PT_Panel)

    bpy.types.Scene.fossee_n = IntProperty(
        name="Number of Cubes (N)",
        default=4,
        min=1,
        
    )


def unregister():
    bpy.utils.unregister_class(FOSSEE_PT_Panel)
    bpy.utils.unregister_class(FOSSEE_OT_MergeMeshes) 
    bpy.utils.unregister_class(FOSSEE_OT_DeleteSelected)
    bpy.utils.unregister_class(FOSSEE_OT_CreateCubes)

    
    del bpy.types.Scene.fossee_n


if __name__ == "__main__":
    register()
