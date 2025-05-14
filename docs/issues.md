# 2. Issues

**¿Qué son los Issues?**

Un Issue es una forma de reportar:
errores (bugs), sugerencias de mejora,tareas por hacer,preguntas o problemas relacionados con el proyecto.
Los Issues permiten que tú y tu equipo organicen el trabajo y se comuniquen dentro del repositorio.
**¿Para qué sirven?**

-Documentar errores o fallas detectadas.
-Proponer mejoras o nuevas funcionalidades.
-Asignar tareas a otros colaboradores.
-Hacer seguimiento del progreso.
-Discutir problemas con otros usuarios del proyecto.
**¿Cómo crear un Issue?**

-Entra al repositorio en GitHub.
-accede al boton "Issues" en la parte superior.
-accede al botón verde "New issue".
-Al acceder coloca Un título claro (por ejemplo: "Error al cargar la página principal").
-Una descripción detallada del problema, con pasos para reproducirlo si es necesario.De forma opcional Puedes utilizar:
Labels (etiquetas como "bug", "enhancement", etc.).
Milestone (si forma parte de una etapa del proyecto).
Assignees (personas responsables del issue).
Haz clic en "Submit new issue".
**¿Cómo asignar un Issue?**

Después de crear el Issue:
En el panel derecho del Issue, haz clic en "Assignees".
Selecciona el usuario de GitHub que será responsable.
Necesitas permisos de colaborador o administrador para poder asignar a otros.
**¿Cómo cerrar un Issue?**

Un Issue se puede cerrar cuando:
Se resuelve el problema o se completa la tarea.
Ya no es relevante.
Desde el repositorio:Abre el Issue.
Haz clic en "Close issue".
desde el terminal se hace un commit que resuelve el Issue, puedes escribir algo como:
git commit -m "Corrige bug de inicio de sesión. Fixes #12"
**Ejemplo de Issue**.
Escenario:
Tienes un proyecto donde estás creando una lista de compras en un archivo de texto. El archivo tiene una lista de elementos y te das cuenta de que no se agrego un artículo.
El procedimiento:
Crear un issue:
Vas a la sección de "Issues" en tu repositorio de GitHub.
Haces clic en "New Issue" (Nuevo Issue).
Pones el título del issue: "Agregar "mochila" a la lista de compras".
En la descripción, puedes escribir algo como:
"No coloque "mochila" a la lista de compras. Debe añadirse al final de la lista."
Agregas la etiqueta: "documentacion" (ya que se trata de un cambio en la lista de compras que forma parte de la documentación del proyecto).
De esta forma figuraria la Issues:
Título: "Agregar 'mochila' a la lista de compras"

Descripción:

"no agregué 'mochila' a la lista de compras. Debe añadirse al final de la lista."

Etiqueta: documentation
