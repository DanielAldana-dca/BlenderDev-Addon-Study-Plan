# Lección 3: Tu primera herramienta funcional

## Objetivo

Crear un operador con panel que mueva el objeto activo una unidad hacia arriba en Z.

## Código didáctico de add-on tradicional

Este código usa `bl_info` para mostrar el ciclo clásico de registro. Para construir una extensión moderna, revisa también el ejemplo con `blender_manifest.toml` incluido en este repositorio.

```python
bl_info = {
    "name": "Mover Objeto Arriba",
    "author": "Tu nombre",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > Mi Herramienta",
    "description": "Mueve el objeto activo en el eje Z",
    "category": "3D View",
}

import bpy


class OBJECT_OT_mover_arriba(bpy.types.Operator):
    bl_idname = "object.mover_arriba_demo"
    bl_label = "Mover arriba"
    bl_description = "Mueve el objeto activo una unidad en Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'WARNING'}, "No hay un objeto activo")
            return {'CANCELLED'}

        obj.location.z += 1.0
        self.report({'INFO'}, f"Movido: {obj.name}")
        return {'FINISHED'}


class VIEW3D_PT_mi_herramienta(bpy.types.Panel):
    bl_label = "Mi Herramienta"
    bl_idname = "VIEW3D_PT_mi_herramienta_demo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mi Herramienta"

    def draw(self, context):
        self.layout.operator("object.mover_arriba_demo")


CLASSES = (
    OBJECT_OT_mover_arriba,
    VIEW3D_PT_mi_herramienta,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
```

## Qué hace cada parte

- `bl_idname`: identificador interno único del operador o panel.
- `bl_label`: texto que ve el usuario.
- `execute()`: lógica principal del operador.
- `context.active_object`: objeto activo, que puede no existir.
- `{'REGISTER', 'UNDO'}`: habilita opciones del operador y soporte de deshacer cuando corresponde.
- `draw()`: define los elementos del panel.
- `CLASSES`: mantiene el registro organizado; se desregistran las clases en orden inverso.

## Ejecutar

1. Abre un archivo nuevo y guarda una copia de prueba.
2. En el editor de texto, pega el ejemplo y pulsa **Run Script**.
3. Ve al Viewport 3D y pulsa `N` para abrir la barra lateral.
4. Entra en **Mi Herramienta** y pulsa **Mover arriba**.
5. Comprueba que `Ctrl+Z` revierte el movimiento.
6. Ejecuta otra vez con ningún objeto activo y observa el aviso.

## Ejercicios

- Cambia el movimiento a `obj.location.x += 2.0`.
- Añade una propiedad `FloatProperty` para elegir la distancia.
- Convierte el código en una extensión moderna usando los archivos del ejemplo incluido.
