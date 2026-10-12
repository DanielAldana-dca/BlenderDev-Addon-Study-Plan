# Lección 2: Configurar el entorno de desarrollo

## Herramientas recomendadas

- Blender, preferentemente una versión estable compatible con la API que estás estudiando.
- VS Code o un editor equivalente.
- Extensión de Python y Pylance para VS Code.
- Git y una cuenta de GitHub para registrar avances.
- Opcional: una extensión de VS Code para ejecutar scripts en Blender. Las extensiones concretas cambian; comprueba que estén mantenidas y sean compatibles con tu versión.

## Obtener el intérprete Python de Blender

Blender suele incluir su propio intérprete de Python. Para conocer la ruta exacta de tu instalación:

1. Abre Blender y entra en **Scripting**.
2. En la consola Python ejecuta:

   ```python
   import sys
   print(sys.executable)
   print(sys.version)
   ```

3. Copia la ruta del ejecutable. En VS Code, usa **Python: Select Interpreter** si necesitas que el editor inspeccione ese intérprete.

La selección del intérprete puede ayudar con el autocompletado, pero ejecutar el código desde Python externo no convierte ese proceso en Blender y normalmente no permite importar `bpy` sin configuraciones especiales.

## Organización sugerida de un add-on

```text
mi_extension/
├── blender_manifest.toml
├── __init__.py
├── operators.py
├── panels.py
├── properties.py
├── utils.py
└── README.md
```

En paquetes con varios módulos, importa los módulos de forma relativa, por ejemplo `from . import operators`. En extensiones modernas, usa `__package__` donde se necesite la identidad del paquete; evita asumir un nombre fijo del módulo.

## Flujo de trabajo

1. Guarda un `.blend` de prueba.
2. Escribe un cambio pequeño.
3. Ejecuta el script o instala la extensión desde disco.
4. Lee la consola si algo falla.
5. Desactiva y reactiva el paquete para comprobar que `register()` / `unregister()` están equilibrados.
6. Guarda el cambio en Git.

## Recarga durante desarrollo

`importlib.reload()` puede servir para experimentar, pero no gestiona automáticamente todos los efectos de registro de clases, propiedades y handlers. Para empezar, desactiva y reactiva el add-on o reinicia Blender si aparecen clases registradas dos veces. Más adelante puedes construir una rutina de recarga que limpie de manera explícita el estado que tu paquete crea.

## Ejercicio

- [ ] Obtén la ruta y versión de Python de Blender.
- [ ] Crea una carpeta de proyecto y ábrela en VS Code.
- [ ] Crea `README.md` para tu primera herramienta.
- [ ] Inicializa Git y registra un commit inicial.

## Referencias

- [Descargar Blender](https://www.blender.org/download/)
- [VS Code](https://code.visualstudio.com/)
- [Documentación de Python](https://docs.python.org/3/)
