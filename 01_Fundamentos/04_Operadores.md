# Lección 4: Operadores en profundidad

Un operador representa una acción del usuario o una operación invocable por código. Los operadores suelen derivar de `bpy.types.Operator`.

## Propiedades útiles

```python
class MI_OT_desplazar(bpy.types.Operator):
    bl_idname = "mi.desplazar_demo"
    bl_label = "Desplazar"
    bl_options = {'REGISTER', 'UNDO'}

    distancia: bpy.props.FloatProperty(
        name="Distancia",
        description="Desplazamiento en el eje X",
        default=1.0,
        min=-100.0,
        max=100.0,
    )

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'ERROR'}, "Selecciona un objeto")
            return {'CANCELLED'}
        obj.location.x += self.distancia
        return {'FINISHED'}
```

## Métodos importantes

- `poll(cls, context)`: permite decidir si el operador está disponible en el contexto actual.
- `invoke(context, event)`: prepara la operación; suele usarse para diálogos o interacciones con el mouse.
- `execute(context)`: ejecuta la acción final.
- `draw(context)`: dibuja las propiedades que se muestran en un diálogo.
- `modal(context, event)`: procesa eventos mientras la operación permanece activa.

## Diálogo para elegir una cantidad

```python
class MI_OT_desplazar_dialogo(bpy.types.Operator):
    bl_idname = "mi.desplazar_dialogo_demo"
    bl_label = "Desplazar con diálogo"
    bl_options = {'REGISTER', 'UNDO'}

    cantidad: bpy.props.FloatProperty(
        name="Cantidad",
        default=1.0,
        min=-100.0,
        max=100.0,
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        self.layout.prop(self, "cantidad")

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({'ERROR'}, "No hay objeto activo")
            return {'CANCELLED'}
        obj.location.x += self.cantidad
        return {'FINISHED'}
```

Recuerda registrar la clase del ejemplo antes de invocarla y desregistrarla al desactivar la herramienta.

## Opciones y resultados

- `REGISTER`: permite mostrar/editar parámetros de la última operación cuando el contexto lo admite.
- `UNDO`: solicita integrar la operación en el sistema de deshacer de Blender.
- `{'FINISHED'}`: la operación terminó correctamente.
- `{'CANCELLED'}`: se canceló o no pudo realizarse.
- `{'RUNNING_MODAL'}`: la operación sigue activa.
- `{'PASS_THROUGH'}`: deja que el evento continúe propagándose según el contexto.

`UNDO` no sustituye a una implementación correcta de cancelación en un operador modal: si una operación modifica datos durante la interacción, debe restaurar explícitamente el estado cuando se cancele.

## Mensajes

```python
self.report({'INFO'}, "Operación completada")
self.report({'WARNING'}, "Comprueba los parámetros")
self.report({'ERROR'}, "No se pudo completar la operación")
```

## Ejercicio

Crea un operador que pregunte un nombre y renombre el objeto activo al aceptar. Debe:

- comprobar que existe un objeto activo;
- ofrecer el nombre como propiedad `StringProperty`;
- ser compatible con `Ctrl+Z`;
- mostrar un error claro si el usuario no seleccionó nada.
