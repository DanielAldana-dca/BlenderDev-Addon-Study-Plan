# Lección 1: ¿Qué es un add-on de Blender?

## Objetivos

Al terminar, distinguirás un script, un módulo Python, un add-on tradicional y una extensión moderna.

## Conceptos

Blender expone una API de Python mediante el módulo `bpy`. Con ella se pueden crear operadores, interfaces, propiedades, materiales, objetos, modificadores y muchas otras herramientas.

- **Script suelto:** código que ejecutas, por ejemplo, desde el editor Scripting. No tiene por qué instalarse ni mantenerse activo.
- **Módulo Python:** archivo o paquete que contiene funciones, clases y datos reutilizables.
- **Add-on tradicional (legacy):** paquete Python activable que suele declarar `bl_info` y funciones `register()` / `unregister()`.
- **Extensión moderna:** paquete que se distribuye con `blender_manifest.toml`; Blender 4.2 y posteriores usan el sistema Extensions.

Una extensión puede añadir herramientas al flujo de trabajo de Blender. No necesita modificar el código fuente de Blender.

## Esqueleto tradicional mínimo

Este ejemplo es para aprender el mecanismo clásico; no contiene aún una herramienta visible.

```python
bl_info = {
    "name": "Mi Add-on de Prueba",
    "author": "Tu nombre",
    "version": (0, 1, 0),
    "blender": (3, 6, 0),  # versión mínima del formato legacy de este ejemplo
    "location": "View3D > Sidebar",
    "description": "Esqueleto didáctico",
    "category": "3D View",
}

import bpy


def register():
    print("Add-on activado")


def unregister():
    print("Add-on desactivado")
```

`bl_info` describe add-ons del formato tradicional. En una extensión moderna estos metadatos se declaran en `blender_manifest.toml`; consulta el ejemplo incluido en `ejemplos/hola_blender_extension/`.

## Ciclo de vida

- `register()` registra clases, propiedades y handlers cuando se activa el paquete.
- `unregister()` debe retirar lo que registró `register()`. Esto evita clases duplicadas, callbacks huérfanos y errores al desactivar o recargar.
- El nombre de `register()` y `unregister()` es una convención del sistema de add-ons; no deben ejecutarse repetidamente sin controlar el registro.

## Ejercicio

1. Ejecuta el código desde el editor de texto de Blender.
2. Revisa la consola del sistema y comprueba que aparece el mensaje.
3. Añade un segundo mensaje a `unregister()` y ejecútalo.
4. Compara este script con `ejemplos/hola_blender_extension/__init__.py`.

## Referencia

- [Manual: Add-ons y Extensions](https://docs.blender.org/manual/en/latest/advanced/extensions/addons.html)
- [API de Blender](https://docs.blender.org/api/current/)
