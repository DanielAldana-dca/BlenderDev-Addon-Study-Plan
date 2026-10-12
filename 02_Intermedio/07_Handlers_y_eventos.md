# Lección 7: Handlers y eventos

Los handlers son callbacks que Blender ejecuta cuando ocurre un evento específico. No son una forma de ejecutar cualquier trabajo pesado sin coste: algunos se disparan con mucha frecuencia.

## Handlers comunes

- `bpy.app.handlers.depsgraph_update_post`: tras actualizaciones del dependency graph.
- `frame_change_pre` / `frame_change_post`: antes o después del cambio de frame.
- `load_post`: después de cargar un archivo.
- `save_pre` / `save_post`: antes o después de guardar.
- `render_init`, `render_complete` y `render_cancel`: eventos relacionados con el render.
- `undo_post`: después de una operación de deshacer, según el evento disponible en la versión.

## Ejemplo: contar objetos en los cambios del dependency graph

```python
import bpy


def contar_objetos_handler(scene, depsgraph):
    # Mantén este trabajo pequeño: puede llamarse con mucha frecuencia.
    print("Objetos en escena:", len(scene.objects))


def register():
    handlers = bpy.app.handlers.depsgraph_update_post
    if contar_objetos_handler not in handlers:
        handlers.append(contar_objetos_handler)


def unregister():
    handlers = bpy.app.handlers.depsgraph_update_post
    if contar_objetos_handler in handlers:
        handlers.remove(contar_objetos_handler)
```

En un add-on real, evita imprimir en cada actualización si esto genera miles de mensajes. Guarda un estado previo, filtra los cambios relevantes o usa una actualización diferida.

## Timer de Blender

```python
import bpy


def tarea_periodica_demo():
    print("Se ejecutó el timer")
    return 2.0  # devuelve segundos para programar otra ejecución


# Registrar una vez, por ejemplo al activar la herramienta:
# bpy.app.timers.register(tarea_periodica_demo, first_interval=2.0)

# Para limpiar al desactivar:
# if bpy.app.timers.is_registered(tarea_periodica_demo):
#     bpy.app.timers.unregister(tarea_periodica_demo)
```

Un timer devuelve un número para solicitar otra llamada después de esa cantidad de segundos. Devuelve `None` cuando no quieras que se vuelva a ejecutar.

## Consideraciones

- Los handlers pertenecen a listas compartidas: elimina solamente los handlers que tu add-on haya añadido.
- Limpia handlers y timers en `unregister()`.
- Si necesitas un handler que sobreviva a la carga de otro archivo, estudia `bpy.app.handlers.persistent`.
- Modificar datos desde handlers de cambio de frame puede interactuar con el render y el viewport; lee la documentación antes de alterar geometría durante el render.

## Ejercicio

Crea un contador de polígonos que se actualice con un timer cada dos segundos y que se pueda detener al desactivar el add-on. Evita realizar trabajo innecesario en cada actualización de la escena.

## Referencia

- [API: Application Handlers](https://docs.blender.org/api/current/bpy.app.handlers.html)
- [API: Timers](https://docs.blender.org/api/current/bpy.app.timers.html)
