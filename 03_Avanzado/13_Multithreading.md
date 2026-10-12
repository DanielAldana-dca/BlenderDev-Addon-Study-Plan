# Lección 13: Concurrencia, tareas diferidas y Blender

## Advertencia importante

La integración de Python de Blender no es thread-safe. Los hilos de Python que siguen ejecutándose mientras Blender usa la interfaz o el render pueden causar cierres o errores difíciles de reproducir. **No accedas a `bpy` desde un hilo de fondo y no dejes hilos activos al terminar el script.** La documentación oficial recomienda evitar este patrón.

## ¿Qué opciones usar?

- **Trabajo pequeño:** hacerlo directamente en el operador.
- **Trabajo que puede repartirse entre eventos de UI:** operador modal o `bpy.app.timers`, con pasos breves por llamada.
- **Cálculos independientes de Blender:** procesa datos Python simples fuera de `bpy`; cualquier estrategia concurrente debe probarse con cuidado.
- **Trabajo CPU intensivo y aislado:** valorar un proceso separado y pasarle datos serializables, sin compartir objetos de Blender.
- **Descargas:** planifica cancelación, timeout y actualización visual; no permitas que una descarga bloquee indefinidamente la interfaz.

## Timer para dividir trabajo

```python
import bpy


def trabajo_en_pasos_demo():
    # Ejecuta una cantidad pequeña de trabajo por llamada.
    terminado = True  # reemplaza por tu condición real
    if terminado:
        return None  # detener el timer
    return 0.1        # volver a ejecutar más tarde


# bpy.app.timers.register(trabajo_en_pasos_demo, first_interval=0.1)
```

El ejemplo muestra el patrón de salida del timer; todavía no procesa una colección. Para trabajos grandes, guarda un índice o una cola de elementos entre llamadas y procesa un lote pequeño cada vez.

## Hilos y procesos

Los hilos pueden ser útiles en programas Python generales, pero no deben tratarse como una solución automática para hacer más rápido un add-on. La documentación de Blender señala que su uso seguro está limitado y que no deben usarse para acceder a la API mientras Blender continúa trabajando. Si eliges un proceso externo, manda solo datos que puedan serializarse (números, cadenas, listas o archivos), no referencias `bpy`.

## Ejercicio

Diseña un operador que procese una lista larga en lotes de 100 elementos por timer, muestre progreso y permita cancelar. Comprueba que el timer se detenga en éxito, cancelación y al desactivar el add-on.

## Referencia

- [API de Blender: Python Threads are Not Supported](https://docs.blender.org/api/current/info_gotchas_threading.html)
- [API de timers](https://docs.blender.org/api/current/bpy.app.timers.html)
