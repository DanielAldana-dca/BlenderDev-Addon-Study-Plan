# Lección 15: Empaquetado y distribución

## Decide el formato

- **Add-on tradicional (legacy):** normalmente usa `bl_info` y módulos Python. Sigue apareciendo en proyectos existentes, pero no es el modelo nuevo de publicación en Extensions.
- **Extensión moderna:** Blender 4.2+ utiliza `blender_manifest.toml` y se empaqueta como ZIP de extensión. El manifiesto contiene ID, versión, nombre, tipo, licencia y versión mínima de Blender, entre otros metadatos.

## Estructura de una extensión simple

```text
mi_extension/
├── blender_manifest.toml
├── __init__.py
├── operators.py
├── panels.py
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## Manifiesto de ejemplo

```toml
schema_version = "1.0.0"
id = "mi_extension_demo"
version = "0.1.0"
name = "Mi Extension Demo"
tagline = "Herramienta de ejemplo para Blender"
maintainer = "Tu nombre o alias"
type = "add-on"
blender_version_min = "4.2.0"
license = ["SPDX:GPL-3.0-or-later"]
```

Los campos requeridos y las etiquetas válidas pueden cambiar con el esquema de Extensions. Comprueba el manual de la versión con la que vas a construir el paquete. Usa una licencia que realmente puedas otorgar y cuyos términos comprendas.

## Construir y validar con Blender

Desde la terminal, usa una versión de Blender que soporte el comando de extensiones. Cambia la ruta según tu sistema:

```bash
blender --command extension validate --source-dir ./mi_extension
blender --command extension build --source-dir ./mi_extension --output-dir ./dist
```

Si la versión de Blender que tienes usa una sintaxis distinta, ejecuta `blender --help` o consulta la documentación correspondiente. Antes de distribuirlo, instala el ZIP resultante desde **Preferences > Get Extensions > menú desplegable > Install from Disk** (los nombres pueden variar ligeramente por idioma y versión).

## Preparar un lanzamiento

- [ ] Nombre claro e identificador único.
- [ ] Versión semántica (`MAJOR.MINOR.PATCH`).
- [ ] Compatibilidad probada en la versión mínima declarada.
- [ ] README con instalación, uso, limitaciones y soporte.
- [ ] Licencia compatible con el código y los recursos incluidos.
- [ ] Changelog con los cambios del lanzamiento.
- [ ] Errores y permisos de red/archivos tratados correctamente.
- [ ] ZIP instalado y probado desde disco en una instalación limpia.
- [ ] Capturas o vídeo que representen la versión publicada.

## Publicación

Puedes mantener el código en GitHub y distribuir versiones empaquetadas. Para publicar en la plataforma oficial de Blender, revisa sus términos, condiciones de licencia y proceso de revisión: no basta con subir el proyecto a GitHub.

## Iconos y recursos

Incluye solo recursos que tengas derecho a redistribuir. Evita cargar imágenes innecesarias en memoria y libera los recursos de vista previa creados por tu add-on cuando se desactive.

## Ejercicio

Convierte el proyecto 1 en una extensión moderna, valida su manifiesto, construye un ZIP, instálalo desde disco y etiqueta el código fuente con `v0.1.0`.

## Referencia

- [Cómo crear Extensions](https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html)
- [Argumentos de línea de comandos para Extensions](https://docs.blender.org/manual/en/latest/advanced/command_line/extension_arguments.html)
- [Plataforma Blender Extensions](https://extensions.blender.org/)
