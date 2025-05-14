---
title: "Tutorial Completo"
nav_order: 11
parent: "Contenido"
---

# 📘 Tutorial de GitHub

## 1. Introducción

![Texto alternativo](assets/descar.png)

¿Qué es GitHub?
**GitHub** es una plataforma en línea donde puedes guardar, compartir y colaborar en código con otras personas usando Git, que es un sistema de control de versiones.
**su importancia en el trabajo colaborativo**
GitHub es como una red social para programadores, pero con herramientas para:
-Guardar proyectos en la nube (repositorios)
-Trabajar en equipo
-Reportar errores o mejoras (issues)
-Proponer cambios (pull requests)
**cómo ha revolucionado el desarrollo de software**
GitHub ha tenido un impacto tremendo en la forma en que se desarrolla software. Aquí te explico cómo ha revolucionado el desarrollo:

1. **Facilitó la colaboración global**
GitHub ha hecho que sea mucho más fácil colaborar con desarrolladores de todo el mundo. Antes, los desarrolladores trabajaban de manera aislada o dependían de herramientas complejas para compartir y fusionar código. Con GitHub, ahora pueden:

Trabajar de manera colaborativa a través de pull requests, donde otros miembros del equipo revisan y sugieren cambios en el código.

Ver el código y hacer comentarios directamente en cada línea (lo que ayuda a resolver problemas y mejorar la calidad).

Gestionar proyectos de manera eficiente utilizando issues, milestones y proyectos.

2. **Control de versiones accesible para todos**
GitHub utiliza Git, un sistema de control de versiones muy poderoso que permite a los desarrolladores mantener un historial completo de cambios. Esto significa que:

Pueden trabajar en paralelo sin miedo a sobrescribir el trabajo de otros.

Volver atrás a una versión anterior del código si algo sale mal, haciendo más fácil experimentar y probar nuevas ideas sin riesgo.

Los errores se pueden rastrear y solucionar fácilmente, ya que todo está documentado.

Antes de GitHub, la gestión de versiones solo estaba disponible en sistemas complejos que no eran tan accesibles. GitHub hizo que el control de versiones fuera accesible para todos, incluso para personas sin mucha experiencia en el tema.

3. **Descentralización del código**
GitHub permitió la creación de proyectos "open source" (de código abierto), lo que democratizó el acceso a las herramientas y permitió que miles de personas contribuyeran al mismo proyecto sin estar en la misma ubicación física o tener acceso a un servidor central.

Los proyectos open source crecen de manera orgánica con contribuciones de desarrolladores de todo el mundo.

Cualquier persona puede revisar, aprender, y mejorar el código.

Facilita la creación de comunidades de desarrolladores que trabajan juntos por un propósito común.

4. **Mejora en la calidad del código**
El sistema de pull requests fomenta que el código sea revisado antes de ser fusionado al proyecto principal. Esto:

Mejora la calidad del código porque cada contribución es evaluada y validada por otros miembros del equipo.

Permite que se detecten errores y problemas de rendimiento antes de que lleguen a producción.

Facilita la implementación de mejores prácticas y estándares de codificación dentro de los equipos.

5. **Documentación accesible y abierta**
GitHub también cambió la manera en que se documenta el software. Los repositorios pueden tener archivos README, documentación adicional y Wiki integrados, lo que facilita:

Compartir información sobre cómo usar, instalar y contribuir a proyectos.

Mantener documentación actualizada junto al código fuente.

6. **Creación de una comunidad global**
GitHub no solo es una plataforma para desarrollar software, sino también una comunidad. Las personas pueden:

Seguir a otros desarrolladores, aprender de ellos y contribuir a sus proyectos.

Unirse a organizaciones y colaborar en proyectos grandes y complejos.

Participar en proyectos open source que impactan a toda la industria de software.

GitHub es como una red social para programadores, lo que crea una gran oportunidad de networking y colaboración.

7. **Fomentar la cultura de "open source"**
GitHub ha promovido la filosofía del código abierto, lo que ha revolucionado la industria de la tecnología. Los proyectos de código abierto pueden ser:

Usados, mejorados y redistribuidos por cualquier persona, lo que acelera la innovación y la evolución tecnológica.

Contribuir a la creación de herramientas, librerías y frameworks de uso gratuito, beneficiando a millones de desarrolladores y empresas.

8. **GitHub como plataforma de aprendizaje**
GitHub también se ha convertido en una herramienta educativa. Los desarrolladores nuevos pueden:

Explorar proyectos open source para aprender cómo se estructuran y cómo funcionan.

Seguir tutoriales y guías.

Colaborar en proyectos para adquirir experiencia y construir su portafolio.

GitHub tiene una gran comunidad de desarrolladores que se apoyan mutuamente, ayudando a que el aprendizaje sea más accesible.

**Historia de GitHub**
GitHub es una plataforma en línea para el desarrollo de software colaborativo. Está basada en Git, un sistema de control de versiones creado por Linus Torvalds (el mismo creador de Linux).

Línea de tiempo:
2005: Git es creado por Linus Torvalds.

2008: GitHub es fundado por Tom Preston-Werner, Chris Wanstrath, P. J. Hyett y Scott Chacon.

2010s: GitHub se vuelve muy popular entre desarrolladores y empresas como una herramienta para compartir código y colaborar en proyectos.

2018: Microsoft compra GitHub por $7.5 mil millones de dólares.

Hoy: Es la plataforma de colaboración de código más usada del mundo, con más de 100 millones de desarrolladores.

**Objetivos de GitHub**

*Colaboración en proyectos de software*
GitHub permite que muchos desarrolladores trabajen juntos en un mismo proyecto, desde cualquier lugar del mundo.

*Control de versiones*
Guarda un historial completo de cambios en el código. Puedes volver atrás, comparar versiones y ver quién hizo qué cambio.

*Compartir código*
Puedes publicar tu proyecto para que otros lo vean, lo usen o contribuyan (repositorios públicos) o mantenerlo privado.

*Revisión y mejora del código*
Los equipos pueden usar pull requests y code reviews para revisar y mejorar el código antes de integrarlo.

*Gestión de proyectos*
GitHub permite usar issues, boards (tableros tipo Kanban), wikis y más para organizar tareas y documentar el proyecto.

*Automatización (CI/CD)*
GitHub Actions permite automatizar pruebas, despliegues, compilaciones y más.

Breve explicación de qué es GitHub y su importancia en el trabajo colaborativo.

## 2. Issues

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

## 3. Pull Requests

![Texto alternativo](assets/descarg.png)

Un **Pull Request (PR)** en GitHub es una solicitud para fusionar cambios desde una rama (por ejemplo, tr) a otra (normalmente main o master) dentro de un repositorio. Es una herramienta clave en el desarrollo colaborativo de software.

**como se crea el Pull Request**

-Desde Git Bash, ya habiendo realizado los cambios en el archivo.
git push origin tr
-habiendo hecho el push accede al repositorio cambia a la rama que deses que se fusione con la rama main en este caso.
-Haz clic en "Compare & pull request".
-Completa los detalles y haz clic en "Create pull request".

**cómo se revisa y se aprueba**

¿Qué necesitas?

-Ser colaborador con permisos de escritura en el repositorio.

-Acceso al Pull Request abierto que quieres revisar.

1. Accede al repositorio en GitHub

2. Accede al boton Pull requests

3. Haz clic en el Pull Request que quieres revisar

4. Revisa los cambios

5. Aprobar el Pull Request

Selecciona la opción "Approve".

(Opcional) Escribe un comentario de aprobación.

Haz clic en "Submit review".

6. (Opcional) Hacer el merge
Si tienes permisos para hacerlo y ya hay al menos una aprobación, verás un botón verde que dice "Merge pull request".

Haz clic en ese botón para fusionar los cambios con la rama principal (por ejemplo, main).

Luego, haz clic en "Confirm merge".

**Incluir buenas prácticas para revisiones de código.**

- Revisa con atención, no con apuro

- Verifica que el cambio cumple su objetivo

- Revisa estilo y format

- Evalúa la estructura del código

- Asegúrate de que el código tenga pruebas

- Detecta posibles errores o riesgos
¿Hay código que podría fallar con ciertos datos?

- Sugiere mejoras, no solo señalas problemas

- Fomenta el aprendizaje

- Revisa solo lo necesario
Si un PR es demasiado grande, sugiere dividirlo.

## 4. GitHub Projects

GitHub Projects es una herramienta poderosa para gestionar tareas dentro de un repositorio usando tableros tipo Kanban. Permite organizar visualmente el progreso del equipo, planificar tareas, dar seguimiento a lo pendiente y mantener el enfoque en los objetivos del proyecto.

---

## ¿Para qué sirve GitHub Projects?

- Visualizar el avance de un proyecto en tiempo real.
- Asignar tareas específicas a cada integrante del equipo.
- Priorizar tareas y dividir el trabajo por etapas.
- Facilitar la colaboración y la transparencia.
- Reemplazar herramientas externas de gestión como Trello o Notion, todo **dentro de GitHub**.

---

## ¿Cómo lo usamos en este proyecto?

En este tutorial colaborativo, usamos **GitHub Projects** para organizar la creación de cada sección del contenido, asegurando que todos los temas fueran cubiertos de manera progresiva y coordinada. Creamos un tablero Kanban con tres columnas:

- **Por hacer**: Secciones pendientes por escribir.
- **En progreso**: Secciones que alguien ya está desarrollando.
- **Terminado**: Secciones completadas y revisadas.

---

### Vista del proyecto (estado general)

![Vista del tablero de proyecto con tareas abiertas](assets/proyectos_open.png)

---

### Vista del tablero Kanban con tareas distribuidas

![Tablero Kanban con tareas distribuidas por estado](assets/proyectos_board.png)

---

## Beneficios reales para este repositorio

- Nos permitió distribuir las responsabilidades entre los integrantes.
- Cada quien sabía qué debía hacer, evitando duplicidad o desorden.
- Hicimos seguimiento claro del progreso, viendo qué faltaba y qué estaba listo.
- Sirvió como evidencia visual del trabajo realizado durante la exposición del proyecto.

---

## 5. Automatización con GitHub Actions

Explica qué es y un ejemplo sencillo (por ejemplo, acción que despliegue una web).

## 6. GitHub Gists

Cómo crear snippets de código públicos o privados.

## 7. GitHub Pages

Cómo publicar una web desde el repositorio.

## 8. Codespaces y Dev Editor

Qué son, para qué sirven y ejemplos básicos.

## 9. Conclusión

El uso de GitHub no solo transforma la manera en que se gestiona el código, sino también la forma en que los equipos colaboran, se comunican y aprenden juntos. A lo largo de este tutorial, hemos explorado herramientas clave como Issues, Pull Requests, Projects, Gists, GitHub Pages y más. Cada una de estas funciones cumple un rol fundamental dentro del flujo de trabajo moderno en el desarrollo de software.

GitHub es mucho más que un simple repositorio de archivos:  
Es una **plataforma de colaboración global** que fomenta la transparencia, la organización, la revisión constante del código y la mejora continua. 

Entre los aprendizajes más importantes que este tutorial nos deja, destacamos:

- La importancia del **control de versiones** para el trabajo ordenado y reversible.
- El valor de la **colaboración estructurada** mediante herramientas como Issues y Pull Requests.
- Cómo utilizar GitHub como un espacio para **documentar, automatizar y compartir proyectos**.
- El poder de la comunidad y la filosofía **open source**, que nos invita a contribuir y aprender constantemente.

Este conocimiento no solo es útil para trabajar en equipo, sino también para tu crecimiento profesional individual, ya que dominar GitHub es una habilidad esencial en cualquier área relacionada con la tecnología y el desarrollo.

---

> "No se trata solo de escribir código, sino de construir soluciones juntos."

Gracias por llegar hasta aquí.

## 10. Créditos

Nombres completos, usuarios GitHub y aportes.
