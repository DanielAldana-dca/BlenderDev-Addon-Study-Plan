# Lección 12: Optimización

Optimizar no significa evitar siempre `bpy.ops`. Significa medir dónde se consume el tiempo y escoger una API adecuada. `bpy.ops` es útil cuando se necesita ejecutar una operación tal como lo haría la interfaz; para edición masiva de datos, las API de datos directas pueden reducir sobrecarga de contexto.

## Principios

1. Mide antes de optimizar.
2. Evita recorrer los mismos datos repetidamente sin necesidad.
3. Cachea referencias que reutilices dentro de una operación.
4. Usa `foreach_get()` / `foreach_set()` para transferencias masivas soportadas.
5. Comprueba el rendimiento en escenas que representen el uso real.
6. Prefiere código claro a una optimización marginal difícil de mantener.

## Comparar enfoques

Crear un objeto con un operador puede ser apropiado:

```python
bpy.ops.mesh.primitive_cube_add()
```

Crear y enlazar datos directamente puede ser mejor para ciertos procesos por lotes:

```python
mesh = bpy.data.meshes.new("Malla_Demo")
obj = bpy.data.objects.new("Objeto_Demo", mesh)
bpy.context.collection.objects.link(obj)
```

Este segundo fragmento crea un objeto con una malla vacía; la geometría debe añadirse por separado.

## Transferencia masiva de coordenadas

```python
import bpy

obj = bpy.context.active_object
if obj and obj.type == 'MESH':
    vertices = obj.data.vertices
    coordenadas = [0.0] * (len(vertices) * 3)
    vertices.foreach_get("co", coordenadas)

    for indice_z in range(2, len(coordenadas), 3):
        coordenadas[indice_z] += 1.0

    vertices.foreach_set("co", coordenadas)
    obj.data.update()
```

Este ejemplo desplaza las coordenadas locales de todos los vértices en Z. Si el objeto está vinculado a otros objetos o la malla tiene datos compartidos, el cambio puede afectar a más de un objeto; comprueba el contexto antes de editar.

## Medir tiempo

```python
from time import perf_counter

inicio = perf_counter()
# Ejecuta aquí la operación a medir.
elapsed = perf_counter() - inicio
print(f"Tiempo: {elapsed:.4f} s")
```

## Ejercicio

Compara un bucle por vértices con una transferencia `foreach_get` / `foreach_set` en una malla suficientemente grande. Repite la prueba y documenta Blender, tamaño de la malla y resultados, sin suponer que una sola medida es concluyente.
