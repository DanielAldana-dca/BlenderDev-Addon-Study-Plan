# Lección 14: Integración con APIs externas

Una API externa puede servir para consultar catálogos, descargar recursos o conectar un add-on con un servicio. Antes de integrar un servicio, revisa sus términos, límites de uso, autenticación y política de privacidad.

## Petición HTTP con la biblioteca estándar

No des por hecho que `requests` está instalado en el Python incluido en cada versión de Blender. Para ejemplos sencillos puedes usar `urllib`; para dependencias externas, estudia cómo empaquetarlas en una extensión.

```python
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def obtener_json(url):
    solicitud = Request(
        url,
        headers={"User-Agent": "BlenderAddonStudy/1.0"},
    )
    try:
        with urlopen(solicitud, timeout=10) as respuesta:
            return json.loads(respuesta.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as error:
        print(f"No se pudieron obtener los datos: {error}")
        return None
```

Prueba con un endpoint público apropiado y respeta los límites del proveedor. No llames a una URL externa arbitraria que no controles desde un add-on sin validar qué datos envías.

## No bloquees la interfaz sin necesidad

Una solicitud de red dentro de `execute()` puede congelar la interfaz hasta terminar o agotar el timeout. Para operaciones largas, diseña una tarea modal o diferida con estado, cancelación y mensajes de progreso. No muevas el acceso a `bpy` a un hilo de fondo como solución rápida.

## Acceso a internet

En versiones modernas de Blender, revisa el estado de acceso en preferencias (`bpy.app.online_access`) antes de iniciar conexiones y explica al usuario por qué tu herramienta necesita red. Para una extensión moderna, declara permisos en `blender_manifest.toml` cuando corresponda y sigue la documentación de la versión objetivo.

## Seguridad

- No publiques claves API, tokens, contraseñas ni archivos `.env`.
- No insertes credenciales en el código del add-on.
- Usa HTTPS cuando el servicio lo ofrezca.
- Define timeouts, trata respuestas HTTP fallidas y valida la estructura de los datos.
- Descarga solo archivos de fuentes confiables, verifica tamaño y formato y evita sobrescribir archivos sin confirmación.
- Informa al usuario qué datos salen de su equipo.

## Ejercicio

Crea una herramienta de consulta de un catálogo público. Muestra estados de carga y error, permite reintentar y documenta qué información envía al servicio. No guardes tokens en el repositorio.
