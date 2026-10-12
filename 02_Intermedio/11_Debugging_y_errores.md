# Lección 11: Depuración y manejo de errores

## Dónde ver errores

En Windows, Blender suele ofrecer **Window > Toggle System Console**. También puedes revisar la salida de la terminal si abriste Blender desde consola. El mensaje de error completo (traceback) suele indicar la línea y la secuencia de llamadas que llevaron al fallo.

## Validar antes de modificar datos

```python
def execute(self, context):
    obj = context.active_object
    if obj is None:
        self.report({'ERROR'}, "No hay un objeto activo")
        return {'CANCELLED'}
    if obj.type != 'MESH':
        self.report({'ERROR'}, "Selecciona un objeto de tipo malla")
        return {'CANCELLED'}

    # La operación real va aquí.
    return {'FINISHED'}
```

## Registro de mensajes

```python
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log.debug("Dato interno para depuración")
log.info("Operación iniciada")
log.warning("Se usó un valor por defecto")
log.error("No se pudo completar la operación")
```

Según cómo se ejecute Blender, puede ser necesario configurar un handler de logging para ver los mensajes con el formato esperado.

## Capturar excepciones sin ocultar información

```python
import traceback

try:
    # Código que estás probando.
    resultado = 10 / 2
except Exception as error:
    traceback.print_exc()
    self.report({'ERROR'}, f"La operación falló: {error}")
    return {'CANCELLED'}
```

No envuelvas todo el programa en `except Exception: pass`: ocultaría la causa real del problema. Captura excepciones donde puedas ofrecer una recuperación concreta.

## Fallos frecuentes

- Clase no registrada o registrada dos veces.
- Identificador `bl_idname` que no coincide entre el registro y la UI.
- Propiedad accedida antes de registrarse o después de eliminarse.
- Operador invocado en un contexto inválido.
- Objeto activo igual a `None`.
- Handler o timer que quedó activo después de desactivar el add-on.
- Socket o clase de Geometry Nodes cuyo identificador cambió entre versiones.

## Ejercicio

Fuerza una excepción controlada, muestra el traceback en la consola y presenta un mensaje legible al usuario. Después elimina la causa del error y confirma que no deja clases, propiedades o handlers registrados de más.
