# Lección 10: Preferencias y persistencia

Hay tres ubicaciones habituales para los datos de un add-on:

1. **Parámetros del archivo `.blend`:** apropiados para configuraciones que pertenecen a una escena o proyecto.
2. **Preferencias del add-on:** apropiadas para opciones globales, como una carpeta de recursos preferida.
3. **Archivo externo:** apropiado para datos compartidos entre proyectos, siempre que se gestione con cuidado la ruta, los permisos y el formato.

## Preferencias de un paquete

En un paquete de add-on, `AddonPreferences.bl_idname` debe corresponder al identificador del módulo del paquete. En extensiones modernas el espacio de nombres puede incluir el repositorio de extensiones, por lo que `__package__` suele ser más seguro que escribir un nombre fijo.

```python
import bpy


class MI_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    carpeta_assets: bpy.props.StringProperty(
        name="Carpeta de recursos",
        subtype='DIR_PATH',
    )
    auto_actualizar: bpy.props.BoolProperty(
        name="Actualizar automáticamente",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "carpeta_assets")
        layout.prop(self, "auto_actualizar")
```

Después de registrar la clase, se puede acceder a las preferencias desde el contenedor de add-ons correspondiente. Comprueba que la clave esté disponible antes de acceder a ella.

## Datos que se guardan en el `.blend`

Las propiedades registradas en `Scene` normalmente se guardan con el archivo Blender cuando corresponda al sistema de datos serializable. Elige su tipo de dato según si la configuración pertenece a una escena, objeto, material o al paquete completo.

## Persistencia JSON

Para preferencias simples propias, JSON puede ser suficiente. Maneja tanto la ausencia del archivo como el JSON dañado y los errores de escritura.

```python
import json
from pathlib import Path


CONFIG_PATH = Path.home() / ".mi_addon_demo.json"


def guardar_config(datos):
    CONFIG_PATH.write_text(
        json.dumps(datos, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def cargar_config():
    if not CONFIG_PATH.exists():
        return {}
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"No se pudo leer la configuración: {error}")
        return {}
```

No guardes contraseñas ni claves privadas sin una solución de almacenamiento adecuada. No des por hecho que una ruta tiene permisos de escritura.

## Ejercicio

Crea preferencias que permitan seleccionar una carpeta de assets, y guarda una opción booleana en un archivo JSON. Prueba un archivo ausente, uno válido y otro con JSON inválido.
