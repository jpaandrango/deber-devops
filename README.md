Comandos Útiles de Git


### 1. Configuración Inicial
* `git init`: Inicializa un nuevo repositorio Git local en la carpeta actual.
* `git clone <url>`: Descarga una copia exacta de un repositorio remoto de GitHub a tu computadora.


### 2. El Día a Día (Guardar Cambios)
* `git status`: Te muestra el estado actual de tus archivos (cuáles han cambiado, cuáles no se están rastreando, etc.).
* `git add .`: Prepara **todos** los archivos modificados y nuevos para el próximo commit (los pasa al *Staging Area*).
* `git add nombre_archivo.py`: Prepara únicamente un archivo específico.
* `git commit -m "Mensaje explicativo"`: Guarda de forma permanente tus cambios en el historial local con un mensaje descriptivo.


### 3. Enviar y Traer Cambios (GitHub)
* `git push origin <nombre-rama>`: Sube tus commits locales desde tu computadora a la rama correspondiente en GitHub.
* `git pull origin <nombre-rama>`: Trae las últimas actualizaciones de GitHub y las fusiona con tu código local.


### 4. Trabajo con Ramas (Branches)
* `git branch`: Muestra la lista de ramas locales de tu proyecto.
* `git checkout -b <nombre-rama>`: Crea una nueva rama y te cambia a ella inmediatamente.
* `git checkout <nombre-rama>`: Te cambia a una rama que ya existe.
* `git merge <nombre-rama>`: Fusiona los cambios de la rama seleccionada con tu rama actual.