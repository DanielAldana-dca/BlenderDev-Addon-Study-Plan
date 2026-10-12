"""Extensión educativa: muestra un panel y mueve el objeto activo en Z."""

import bpy


class HOLA_OT_mover_arriba(bpy.types.Operator):
    bl_idname = "hola_blender.mover_arriba"
    bl_label = "Mover arriba"
    bl_description = "Mueve el objeto activo una unidad en Z"
    bl_options = {'REGISTER', 'UNDO'}

    distancia: bpy.props.FloatProperty(
        name="Distancia",
        description="Desplazamiento en el eje Z",
        default=1.0,
        min=-100.0,
        max=100.0,
    )

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'WARNING'}, "Selecciona un objeto antes de continuar")
            return {'CANCELLED'}

        obj.location.z += self.distancia
        self.report({'INFO'}, f"{obj.name} se movió {self.distancia:g} unidades")
        return {'FINISHED'}


class HOLA_PT_panel(bpy.types.Panel):
    bl_label = "Hola Blender"
    bl_idname = "HOLA_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Hola Blender"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Extensión de demostración")
        layout.operator(HOLA_OT_mover_arriba.bl_idname, icon='OBJECT_ORIGIN')


CLASSES = (
    HOLA_OT_mover_arriba,
    HOLA_PT_panel,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
