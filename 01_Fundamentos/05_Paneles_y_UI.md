# Lección 5: Paneles e interfaz de usuario

## Tipos habituales

- **Panel:** contenedor con título.
- **Subpanel:** panel subordinado que puede plegarse.
- **Menú:** lista de acciones.
- **Header:** zona de cabecera de un editor.
- **Operator dialog:** diálogo generado por las propiedades de un operador.

## Panel básico

```python
class VIEW3D_PT_panel_demo(bpy.types.Panel):
    bl_label = "Mi Panel"
    bl_idname = "VIEW3D_PT_panel_demo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mi Add-on"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Herramientas")
        layout.operator("object.mover_arriba_demo")
```

El operador tiene que estar registrado y el `bl_idname` debe coincidir exactamente con el que se usa en el botón.

## Elementos de interfaz frecuentes

```python
layout.label(text="Etiqueta")
layout.prop(context.scene, "mi_propiedad")
layout.separator()
layout.operator("mi.accion_demo")

row = layout.row(align=True)
row.label(text="Fila")
row.prop(context.scene, "otra_propiedad")

col = layout.column(align=True)
col.label(text="Columna")
col.operator("mi.accion_demo")

box = layout.box()
box.label(text="Opciones avanzadas")
```

## Mostrar u ocultar contenido

Comprueba el contexto antes de acceder a objetos que pueden no existir:

```python
def draw(self, context):
    layout = self.layout
    obj = context.active_object
    if obj is None:
        layout.label(text="Selecciona un objeto")
        return
    layout.label(text=f"Objeto: {obj.name}")
    layout.prop(obj, "location")
```

## Subpanel plegable

```python
class VIEW3D_PT_padre_demo(bpy.types.Panel):
    bl_label = "Herramienta"
    bl_idname = "VIEW3D_PT_padre_demo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mi Add-on"

    def draw(self, context):
        self.layout.label(text="Opciones principales")


class VIEW3D_PT_hijo_demo(bpy.types.Panel):
    bl_label = "Avanzado"
    bl_idname = "VIEW3D_PT_hijo_demo"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mi Add-on"
    bl_parent_id = "VIEW3D_PT_padre_demo"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.label(text="Opciones secundarias")
```

Registra primero el panel padre y después el hijo. Al desregistrarlos, utiliza el orden inverso.

## Ejercicio

Construye un panel con un texto de ayuda, dos botones, una fila y un subpanel plegable. Comprueba también el aspecto cuando no hay objeto seleccionado.
