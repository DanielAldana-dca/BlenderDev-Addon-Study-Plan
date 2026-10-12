# Lección 9: Operadores avanzados y modales

Un operador modal permanece activo y recibe eventos del mouse o del teclado. Es útil para herramientas interactivas; requiere manejar confirmación, cancelación y limpieza cuidadosamente.

## Ejemplo: desplazar el objeto con el mouse

Este ejemplo desplaza el objeto en X según el movimiento horizontal del mouse. Guarda la posición inicial para restaurarla si se cancela.

```python
import bpy


class MI_OT_desplazar_modal_demo(bpy.types.Operator):
    bl_idname = "mi.desplazar_modal_demo"
    bl_label = "Desplazar con el mouse"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        obj = context.active_object
        if obj is None:
            self.report({'WARNING'}, "Selecciona un objeto")
            return {'CANCELLED'}

        self.objeto = obj
        self.posicion_inicial = obj.location.copy()
        self.mouse_inicial_x = event.mouse_x
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if self.objeto.name not in bpy.data.objects:
            return {'CANCELLED'}

        if event.type == 'MOUSEMOVE':
            delta = (event.mouse_x - self.mouse_inicial_x) * 0.01
            self.objeto.location.x = self.posicion_inicial.x + delta
        elif event.type in {'ESC', 'RIGHTMOUSE'}:
            self.objeto.location = self.posicion_inicial
            return {'CANCELLED'}
        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            return {'FINISHED'}

        return {'RUNNING_MODAL'}
```

Registra la clase antes de usar `bpy.ops.mi.desplazar_modal_demo('INVOKE_DEFAULT')`. El ejemplo es didáctico: añade validaciones si tu herramienta puede cambiar de escena o eliminar el objeto durante la operación.

## Ejecutar operadores existentes

```python
bpy.ops.object.duplicate()
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
```

Los operadores dependen del contexto (modo, editor, selección, área activa). Si una llamada falla, inspecciona sus condiciones con `poll()` y revisa el contexto. Prefiere la API de datos directa cuando sea apropiada y más clara.

## Context override

En versiones recientes se usa `bpy.context.temp_override()` para llamar a un operador con contexto explícito. No intentes forzar un contexto arbitrario sin saber qué ventana, área, región y objeto exige la operación.

```python
with bpy.context.temp_override(active_object=obj, object=obj):
    # Coloca aquí una llamada que requiera ese contexto.
    pass
```

Este es solo el patrón sintáctico: no todos los operadores funcionan únicamente con `active_object` y `object`.

## Ejercicio

Implementa una herramienta modal que rote un objeto; `Esc` cancela y restaura el ángulo original, mientras un clic izquierdo confirma. Prueba también el caso en que no haya objeto activo.
