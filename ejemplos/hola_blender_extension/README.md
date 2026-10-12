# Extensión de ejemplo: Hola Blender

Extensión educativa para Blender 4.2 o posterior. Añade la pestaña **Hola Blender** a la barra lateral del Viewport 3D (`N`) y un operador que desplaza el objeto activo en Z.

## Instalar desde el código fuente

### Crear el ZIP con Blender

Ejecuta desde una terminal usando Blender 4.2 o posterior:

```bash
blender --command extension validate --source-dir ./ejemplos/hola_blender_extension
blender --command extension build --source-dir ./ejemplos/hola_blender_extension --output-dir ./dist
```

Ejecuta los comandos desde la raíz del repositorio. En Windows, puede que tengas que utilizar la ruta completa al ejecutable de Blender o abrir la terminal donde el comando `blender` esté disponible.

### Instalar el ZIP

En Blender, abre **Edit > Preferences > Get Extensions**, abre el menú desplegable de la sección y elige **Install from Disk**. Selecciona el archivo generado en `dist`. El nombre exacto del menú puede variar con el idioma y la versión de Blender.

Después de instalar y activar la extensión:

1. Abre el Viewport 3D.
2. Pulsa `N` para abrir la barra lateral.
3. Selecciona la pestaña **Hola Blender**.
4. Selecciona un objeto y pulsa el botón.
5. Comprueba que `Ctrl+Z` revierte el movimiento.

## Qué observar

- El manifiesto declara metadatos y versión mínima, sin `bl_info`.
- Las clases se registran en `register()` y se desregistran en orden inverso.
- El operador valida que exista un objeto activo.
- `bl_options = {'REGISTER', 'UNDO'}` permite registrar la operación y deshacerla.

## Licencia

El ejemplo declara `GPL-3.0-or-later` en su manifiesto. Si lo modificas para redistribuirlo, revisa y conserva las obligaciones de esa licencia.
