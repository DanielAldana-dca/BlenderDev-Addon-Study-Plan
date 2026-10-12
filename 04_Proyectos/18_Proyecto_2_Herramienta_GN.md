# Proyecto 2: Herramienta procedural con Geometry Nodes

## Objetivo

Crear una extensión que aplique un modificador de Geometry Nodes configurable. Proyecto sugerido: distribuir instancias de una colección en las caras de una malla.

## Componentes

1. Panel con controles como colección de instancias, densidad y semilla.
2. Operador para crear o reutilizar el grupo de nodos.
3. Entradas expuestas en la interfaz del grupo para que el modificador muestre controles.
4. Validaciones para geometría, colección y parámetros.
5. Presets, documentación y pruebas.

## Plan de trabajo

- [ ] Primero crea el árbol manualmente en Blender y anota las conexiones.
- [ ] Identifica los `bl_idname` de cada nodo y el nombre de cada socket.
- [ ] Crea el grupo de nodos usando `bpy.data.node_groups.new(..., 'GeometryNodeTree')`.
- [ ] Añade sockets de entrada/salida con `group.interface.new_socket(...)`.
- [ ] Crea y enlaza los nodos con `group.nodes.new(...)` y `group.links.new(...)`.
- [ ] Asigna el árbol al modificador `NODES` del objeto objetivo.
- [ ] Expón las propiedades al usuario y valida los datos.
- [ ] Prueba en al menos dos objetos y en la versión mínima de Blender.

## Diseño del producto

La herramienta debe evitar crear grupos duplicados en cada ejecución, distinguir datos que son propiedad del add-on y explicar qué ocurre cuando el usuario cambia o elimina la colección de instancias.

## Retos

- Guardar y cargar presets.
- Permitir actualizar el grupo sin destruir ediciones del usuario.
- Añadir estados de error descriptivos.
- Medir rendimiento con mallas densas.
- Documentar las diferencias de API entre versiones.

## Criterios de aceptación

- [ ] El modificador se crea en el objeto correcto.
- [ ] Todos los sockets están conectados como se espera.
- [ ] Los parámetros tienen límites y valores por defecto adecuados.
- [ ] Desactivar la extensión no deja handlers activos.
- [ ] Las instrucciones de instalación y uso son reproducibles.
