# Ruta de aprendizaje: desarrollo de add-ons para Blender

Material de estudio en español para aprender a crear, probar, mantener y distribuir herramientas con Python para Blender. Incluye 22 lecciones, tres proyectos progresivos, una chuleta de API y una extensión de ejemplo lista para instalar y modificar.

> **Versión objetivo:** Blender 4.2 o posterior para el flujo moderno de Extensions. Los ejemplos introductorios identificados como *legacy* sirven para entender add-ons tradicionales; la publicación de extensiones modernas utiliza `blender_manifest.toml`.

## Qué aprenderás

- Crear operadores, paneles y propiedades propios.
- Trabajar con la API `bpy`, eventos, temporizadores y Geometry Nodes.
- Depurar errores, proteger el estado de Blender y mejorar el rendimiento.
- Integrar servicios externos sin bloquear innecesariamente la interfaz ni exponer credenciales.
- Empaquetar una extensión, documentarla, versionarla y preparar su distribución.
- Construir un portafolio y evaluar opciones de monetización sin depender de promesas de ingresos.

## Estructura del repositorio

```text
BlenderDev-Addon-Study-Plan/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── 01_Fundamentos/       # Lecciones 1–6
├── 02_Intermedio/        # Lecciones 7–11
├── 03_Avanzado/          # Lecciones 12–16
├── 04_Proyectos/         # Proyectos 1–3
├── 05_Recursos/          # Enlaces, comunidad, API y GitHub
└── ejemplos/
    └── hola_blender_extension/  # Extensión moderna de demostración
```

## Requisitos

- Blender 4.2 o posterior recomendado para las lecciones sobre Extensions.
- VS Code u otro editor de texto.
- Conocimientos básicos de programación. Si Python es nuevo para ti, estudia primero variables, funciones, clases, módulos, listas, diccionarios y excepciones.
- Git y una cuenta de GitHub son recomendables, pero no necesarios para practicar localmente.

Los pasos de configuración están en [`02_Entorno_de_desarrollo.md`](01_Fundamentos/02_Entorno_de_desarrollo.md).

## Ruta recomendada

| Fase | Contenido | Ritmo orientativo |
|---|---|---|
| Fundamentos | Lecciones 1–6 | 4–6 semanas |
| Intermedio | Lecciones 7–11 | 5–7 semanas |
| Avanzado | Lecciones 12–16 | 6–10 semanas |
| Proyectos | Proyectos 1–3 | 4–8 semanas |

Como referencia, estudiar entre 1 y 2 horas por día podría llevar varios meses. La fecha del primer producto publicable o ingreso no se puede garantizar: depende de la práctica, la calidad del producto, la demanda, el soporte y los medios de cobro disponibles.

## Método de estudio

1. Lee una lección y ejecuta los ejemplos en una escena de prueba.
2. Teclea o reescribe el código, en lugar de limitarte a copiarlo.
3. Cambia parámetros y prueba casos límite.
4. Provoca errores de manera controlada y aprende a leer el traceback.
5. Guarda una nota con lo que aprendiste y lo que aún no entiendes.
6. Haz commits pequeños en Git al terminar cada ejercicio.
7. No pruebes código desconocido en un archivo de trabajo importante: usa una copia de la escena.

## Seguimiento

- [ ] Fase 1: Fundamentos
- [ ] Fase 2: Intermedio
- [ ] Fase 3: Avanzado
- [ ] Fase 4: Proyectos
- [ ] Primera extensión instalada y probada en una segunda escena
- [ ] Repositorio público con instrucciones de uso
- [ ] Primera versión etiquetada (`v0.1.0` o `v1.0.0`)
- [ ] Demo y documentación de una herramienta propia

## Empieza aquí

1. Lee [Lección 1: ¿Qué es un add-on?](01_Fundamentos/01_Que_es_un_addon.md).
2. Configura el entorno con [Lección 2](01_Fundamentos/02_Entorno_de_desarrollo.md).
3. Ejecuta la extensión de ejemplo de [`ejemplos/hola_blender_extension`](ejemplos/hola_blender_extension/README.md).
4. Sigue el orden de las carpetas y completa los proyectos.

## Publicarlo en GitHub

Consulta [`05_Recursos/23_Guia_GitHub.md`](05_Recursos/23_Guia_GitHub.md). Sube la carpeta del proyecto al repositorio; no subas únicamente el ZIP generado por esta distribución. Mantén este README en la raíz para que GitHub lo muestre como página inicial.

## Notas de compatibilidad y responsabilidad

- Blender cambia su API entre versiones. Comprueba siempre la versión de Blender y contrasta los nombres de clases, sockets y propiedades con la API de esa versión.
- Desde Blender 4.2, el sistema de Extensions usa un manifiesto `blender_manifest.toml`. El antiguo `bl_info` pertenece al flujo tradicional de add-ons y no sustituye al manifiesto de una extensión moderna.
- Los ejemplos están diseñados como material didáctico. Verifica cada operación destructiva en una escena descartable.
- Las plataformas de distribución, comisiones, disponibilidad de pagos y obligaciones fiscales cambian según el país y el proveedor. Revisa sus términos oficiales antes de comercializar una herramienta.

## Documentación oficial

- [Manual de Blender: Extensions](https://docs.blender.org/manual/en/latest/advanced/extensions/)
- [Cómo crear extensiones](https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html)
- [API de Blender Python](https://docs.blender.org/api/current/)
- [Comunidad de Extensions](https://extensions.blender.org/)
