# Guía adicional: subir este proyecto a GitHub

## Opción A: desde la web de GitHub

1. Inicia sesión en GitHub y crea un repositorio nuevo.
2. Ponle un nombre, por ejemplo `BlenderDev-Addon-Study-Plan`.
3. Decide si será público o privado.
4. Evita inicializarlo con un README si vas a subir esta carpeta, porque ya incluye uno.
5. En el repositorio, selecciona **Add file > Upload files**.
6. Arrastra los archivos y carpetas del proyecto extraído del ZIP. Asegúrate de que `README.md` queda en la raíz, no dentro de una carpeta duplicada.
7. Escribe un mensaje de commit, por ejemplo `Añade plan de estudio inicial`, y confirma.

Si la interfaz web no acepta tantas carpetas o archivos de una vez, usa Git desde la terminal.

## Opción B: con Git en Windows

1. Extrae el ZIP en una ruta sencilla, por ejemplo `D:\BlenderDev-Addon-Study-Plan`.
2. Abre PowerShell o Git Bash en esa carpeta.
3. Configura Git una sola vez si aún no lo has hecho:

   ```bash
   git config --global user.name "Tu nombre"
   git config --global user.email "tu-correo@example.com"
   ```

4. Inicializa y registra los archivos:

   ```bash
   git init
   git add .
   git commit -m "Añade plan de estudio de Blender"
   git branch -M main
   ```

5. Copia la URL del repositorio que creaste en GitHub y conéctala:

   ```bash
   git remote add origin https://github.com/TU_USUARIO/BlenderDev-Addon-Study-Plan.git
   git push -u origin main
   ```

Reemplaza `TU_USUARIO` por tu usuario real. Si Git te pide autenticarte, sigue el proceso actual de GitHub; las contraseñas de la cuenta normalmente no se usan directamente para `git push` por HTTPS.

## Actualizar después de editar

```bash
git add .
git commit -m "Describe el cambio"
git push
```

## Antes de publicar

- No incluyas claves API, contraseñas, tokens, archivos `.blend` privados o rutas con datos personales.
- Comprueba que el README enlaza a archivos que existen.
- Mantén el código fuente y la documentación en el repositorio. Usa ZIP separados para distribuir una extensión a sus usuarios.
- Para marcar una versión, crea una etiqueta, por ejemplo `git tag v0.1.0` y `git push origin v0.1.0`.
