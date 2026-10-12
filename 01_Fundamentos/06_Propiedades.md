# Lección 6: Propiedades personalizadas

Las propiedades definen parámetros configurables y conectan los valores con la interfaz de Blender.

## Tipos comunes

- `IntProperty`: enteros.
- `FloatProperty`: números decimales.
- `BoolProperty`: verdadero/falso.
- `StringProperty`: texto.
- `EnumProperty`: opciones de una lista.
- `PointerProperty`: referencia a un tipo de dato.
- `CollectionProperty`: colección de elementos definidos por un `PropertyGroup`.

## Propiedad en Scene

```python
def register():
    bpy.types.Scene.mi_cantidad_demo = bpy.props.IntProperty(
        name="Cantidad",
        description="Número de elementos",
        default=5,
        min=1,
        max=100,
    )


def unregister():
    del bpy.types.Scene.mi_cantidad_demo
```

Este fragmento ilustra el patrón. Integra el registro con las clases del proyecto y evita registrar la misma propiedad dos veces. En código de producción, revisa que la propiedad exista antes de eliminarla si tu procedimiento de recarga puede ejecutarse parcialmente.

## EnumProperty

```python
def opciones_modo(self, context):
    return [
        ('RAPIDO', "Rápido", "Menos controles"),
        ('DETALLADO', "Detallado", "Más controles"),
    ]

# Debe asignarse a un tipo compatible durante register().
# bpy.types.Scene.mi_modo_demo = bpy.props.EnumProperty(
#     name="Modo", items=opciones_modo, default='RAPIDO'
# )
```

Las tuplas suelen contener el identificador interno, el nombre visible y la descripción. Si la función `items` crea opciones dinámicas, sus identificadores deben mantenerse válidos mientras Blender los necesite.

## Callback de actualización

```python
def al_cambiar_mi_cantidad(self, context):
    print("Nuevo valor:", self.mi_cantidad_demo)
```

Puedes pasarlo mediante `update=al_cambiar_mi_cantidad`. Evita modificar la misma propiedad desde su callback sin controlar la recursión: podría producir actualizaciones repetidas.

## Agrupar valores con PropertyGroup

```python
class MiConfiguracionDemo(bpy.types.PropertyGroup):
    escala: bpy.props.FloatProperty(name="Escala", default=1.0, min=0.01)
    activo: bpy.props.BoolProperty(name="Activo", default=True)
    nombre: bpy.props.StringProperty(name="Nombre", default="")


# En register(), primero registra la clase:
# bpy.utils.register_class(MiConfiguracionDemo)
# bpy.types.Scene.mi_config_demo = bpy.props.PointerProperty(
#     type=MiConfiguracionDemo
# )

# En unregister(), elimina Scene.mi_config_demo y después desregistra la clase.
```

## Ejercicio

Crea un `PropertyGroup` con escala, nombre y estado activo; enlázalo a `Scene`, muéstralo en un panel y añade una actualización que escriba en la consola. Comprueba que el registro y la limpieza se ejecutan en el orden correcto.
