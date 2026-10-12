# Lección 8: Geometry Nodes mediante la API

## Objetivo

Crear un grupo de Geometry Nodes con Python y asignarlo a un modificador del objeto activo. La API de nodos depende de la versión; comprueba siempre los identificadores y sockets disponibles en tu instalación.

## Ejemplo: grupo que transforma la geometría

```python
import bpy


def crear_grupo_transform_demo():
    grupo = bpy.data.node_groups.new(
        name="GN_Transform_Demo",
        type='GeometryNodeTree',
    )

    grupo.interface.new_socket(
        name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry'
    )
    grupo.interface.new_socket(
        name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry'
    )

    entrada = grupo.nodes.new('NodeGroupInput')
    entrada.location = (-400, 0)
    transform = grupo.nodes.new('GeometryNodeTransform')
    transform.location = (-100, 0)
    salida = grupo.nodes.new('NodeGroupOutput')
    salida.location = (200, 0)

    # En GeometryNodeTransform, Translation es el desplazamiento del nodo.
    transform.inputs['Translation'].default_value = (1.0, 0.0, 0.0)

    grupo.links.new(entrada.outputs['Geometry'], transform.inputs['Geometry'])
    grupo.links.new(transform.outputs['Geometry'], salida.inputs['Geometry'])
    return grupo


def aplicar_grupo_al_objeto(obj, grupo):
    modificador = obj.modifiers.new(name="Transform Demo", type='NODES')
    modificador.node_group = grupo
    return modificador


obj = bpy.context.active_object
if obj is not None:
    grupo = crear_grupo_transform_demo()
    aplicar_grupo_al_objeto(obj, grupo)
else:
    print("Selecciona primero un objeto")
```

El ejemplo crea un grupo simple y desplaza la geometría un metro en X dentro del modificador. Si lo ejecutas varias veces, crearás grupos y modificadores adicionales; modifica el script para reutilizar o limpiar datos de forma explícita.

## Ideas para investigar

- `NodeTree.interface.new_socket()` para exponer parámetros.
- `NodeTree.nodes.new()` para crear nodos.
- `NodeTree.links.new()` para conectar sockets.
- `GeometryNodeDistributePointsOnFaces` y `GeometryNodeInstanceOnPoints` para crear herramientas de distribución, confirmando los identificadores en la versión objetivo.
- `NodesModifier.node_group` para asignar el grupo al modificador.

## Cómo descubrir los identificadores

1. Crea manualmente el nodo que necesitas.
2. En la consola Python inspecciona el nodo seleccionado, por ejemplo:

   ```python
   node = bpy.context.active_object.modifiers[-1].node_group.nodes[0]
   print(node.bl_idname)
   print([socket.name for socket in node.inputs])
   print([socket.name for socket in node.outputs])
   ```

3. Consulta la documentación de la versión instalada.

## Ejercicio

- Expón un parámetro de traslación como socket de entrada.
- Añade un segundo nodo compatible y conéctalo.
- Comprueba el grupo con más de un tipo de objeto.
- Evita depender de índices numéricos de sockets cuando exista un nombre estable.

## Referencia

- [API: Node Trees](https://docs.blender.org/api/current/bpy.types.NodeTree.html)
- [API: Nodes Modifier](https://docs.blender.org/api/current/bpy.types.NodesModifier.html)
