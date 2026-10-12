# Lección 22: Chuleta de la API de Blender

Esta lista es un recordatorio, no un sustituto de la documentación. Las propiedades y los contextos disponibles cambian según el tipo de dato y la versión de Blender.

## Contexto

```python
bpy.context.active_object
bpy.context.selected_objects
bpy.context.scene
bpy.context.collection
bpy.context.window_manager
```

## Escena y tiempo

```python
bpy.context.scene.objects
bpy.context.scene.frame_current
bpy.context.scene.frame_set(10)
```

## Objetos

```python
obj = bpy.context.active_object
obj.location
obj.rotation_euler
obj.scale
obj.data
obj.modifiers
obj.parent
```

Accede por nombre solo si el nombre está controlado y comprueba que el dato existe: `bpy.data.objects.get("Nombre")` puede devolver `None`.

## Mallas

```python
mesh = obj.data
mesh.vertices
mesh.edges
mesh.polygons
mesh.uv_layers
```

## bmesh

```python
import bmesh

bm = bmesh.new()
try:
    bm.from_mesh(mesh)
    # Realiza aquí operaciones de edición de malla.
    bm.to_mesh(mesh)
    mesh.update()
finally:
    bm.free()
```

El modo de edición tiene un flujo distinto; lee la documentación de `bmesh` antes de mezclar cambios directos con datos que están siendo editados.

## Materiales

```python
mat = bpy.data.materials.new("Material_Demo")
mat.use_nodes = True
nodes = mat.node_tree.nodes
```

Crear un material no lo asigna automáticamente a un objeto: debes añadirlo a los slots correspondientes.

## Colecciones

```python
collection = bpy.data.collections.new("Coleccion_Demo")
bpy.context.scene.collection.children.link(collection)
collection.objects.link(obj)
```

Un objeto puede pertenecer a varias colecciones. Antes de desvincularlo, revisa `obj.users_collection`.

## Operadores frecuentes

```python
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
bpy.ops.mesh.primitive_cube_add()
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.object.duplicate()
```

Pueden depender del contexto, selección, modo y editor actual. Si necesitas llamar a un operador desde código, verifica primero sus requisitos.

## Handlers y timers

```python
bpy.app.handlers.depsgraph_update_post
bpy.app.handlers.frame_change_post
bpy.app.handlers.load_post
bpy.app.timers.register(mi_funcion, first_interval=1.0)
```

Elimina lo que registraste en `unregister()` y evita callbacks pesados o recursivos.

## Utilidades

```python
bpy.path.abspath("//ruta_relativa")
bpy.utils.user_resource('SCRIPTS')
bpy.utils.register_class(MiClase)
bpy.utils.unregister_class(MiClase)
```

## Depuración rápida

```python
print(bpy.app.version_string)
print(bpy.app.version)
print(bpy.context.mode)
print(bpy.context.active_object)
```

## Referencias

- [API de Blender Python](https://docs.blender.org/api/current/)
- [Gotchas de la API](https://docs.blender.org/api/current/info_gotchas.html)
