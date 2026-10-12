# Proyecto 1: Generador de cuadrícula de cubos

## Objetivo

Construir una herramienta con panel que genere una cuadrícula configurable de cubos y pueda borrar únicamente los cubos que creó.

## Requisitos

- Propiedades para filas, columnas y separación.
- Botón **Generar**.
- Botón **Limpiar generados**.
- Soporte de deshacer.
- Colección propia para no borrar objetos ajenos.

## Guía de implementación

1. Registra propiedades en `Scene` o utiliza propiedades del operador.
2. En el operador Generar, crea/recupera una colección identificada por la herramienta.
3. Crea cada cubo y enlázalo a esa colección.
4. Añade nombres o una marca propia a los objetos generados.
5. En Limpiar, elimina solo los objetos de esa colección que pertenecen al generador.
6. Valida rangos y añade mensajes cuando la escena no permita completar la acción.

## Código base: operador seguro para generar

Este fragmento demuestra el bucle; debes integrarlo en un add-on registrando la clase y conectándola a un panel.

```python
import bpy


class MI_OT_generar_cuadricula(bpy.types.Operator):
    bl_idname = "mi.generar_cuadricula_demo"
    bl_label = "Generar cuadrícula"
    bl_options = {'REGISTER', 'UNDO'}

    filas: bpy.props.IntProperty(name="Filas", default=5, min=1, max=50)
    columnas: bpy.props.IntProperty(name="Columnas", default=5, min=1, max=50)
    separacion: bpy.props.FloatProperty(
        name="Separación", default=2.0, min=0.1, max=100.0
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        escena = context.scene
        nombre_coleccion = "MI_ADDON_CUADRICULA_GENERADA"
        coleccion = bpy.data.collections.get(nombre_coleccion)
        if coleccion is None:
            coleccion = bpy.data.collections.new(nombre_coleccion)
            escena.collection.children.link(coleccion)

        for fila in range(self.filas):
            for columna in range(self.columnas):
                bpy.ops.mesh.primitive_cube_add(
                    size=1.0,
                    location=(fila * self.separacion,
                              columna * self.separacion, 0.0),
                )
                obj = context.active_object
                # Desvincular de colecciones anteriores y asociar a la propia.
                for coleccion_actual in list(obj.users_collection):
                    coleccion_actual.objects.unlink(obj)
                coleccion.objects.link(obj)
                obj["mi_addon_cuadricula"] = True

        self.report({'INFO'}, f"Generados {self.filas * self.columnas} cubos")
        return {'FINISHED'}
```

> Nota: como usa `bpy.ops.mesh.primitive_cube_add`, el operador depende del contexto de Blender. Para una versión más avanzada, crea la malla y los objetos mediante la API de datos y revisa el comportamiento de deshacer.

## Limpiar solo los objetos generados

Integra una clase con `bl_options = {'REGISTER', 'UNDO'}` y usa un patrón como este:

```python
for obj in list(bpy.data.objects):
    if obj.get("mi_addon_cuadricula") is True:
        bpy.data.objects.remove(obj, do_unlink=True)
```

No borres objetos solo porque su nombre empiece por `Cube`: podrías eliminar cubos creados manualmente por el usuario.

## Entregables

- [ ] Generación con parámetros configurables.
- [ ] Limpieza que no afecta a objetos ajenos.
- [ ] Panel fácil de entender.
- [ ] Prueba de deshacer/rehacer.
- [ ] Captura de pantalla y breve explicación.
- [ ] README y etiqueta de versión.
