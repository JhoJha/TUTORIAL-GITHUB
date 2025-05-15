# 📘 Tutorial de GitHub

Este repositorio contiene una guía completa y práctica sobre el uso de GitHub. Fue desarrollada como parte de la **Evaluación Grupal 1** del curso **Lenguaje de Programación II**, con el objetivo de que los estudiantes comprendan y apliquen las principales herramientas que ofrece GitHub para colaborar, versionar y construir proyectos profesionales.

---

## 📚 Contenido del tutorial

* ¿Qué es GitHub?
* Cómo trabajar con **Issues**
* Uso de **Pull Requests**
* Gestión de proyectos con **GitHub Projects**
* Automatización con **GitHub Actions**
* Uso de **Gists**
* Publicación de sitios web con **GitHub Pages**
* Introducción a **Codespaces**
* Uso del **GitHub Dev Editor**

👉 Accede a la versión web completa del tutorial:
🔗 [https://jhojha.github.io/TUTORIAL-GITHUB/](https://jhojha.github.io/TUTORIAL-GITHUB/)

---

## 🎯 Objetivos del proyecto

* Comprender el funcionamiento de las principales herramientas de GitHub.
* Promover el trabajo colaborativo mediante **Pull Requests** e **Issues**.
* Aplicar buenas prácticas de documentación, versionado y desarrollo en equipo.

---

## 👥 Integrantes del grupo

* **Jhon Jhayro Villegas** [`JhoJha`](https://github.com/JhoJha)
* **Alonso Coronado de la Vega** [`ron-62`](https://github.com/ron-62)
* **Fernando José Ruiz Macedo** [`FernandoRuiz345`](https://github.com/FernandoRuiz345)

---

## 🗂️ Estructura del repositorio

| Carpeta / Archivo | ¿Qué contiene?                                                     | ¿Quién lo edita?                                  |
| ----------------- | ------------------------------------------------------------------ | ------------------------------------------------- |
| `_pages/`         | Archivos `.md` individuales que componen cada sección del tutorial | Todos (según el tema asignado)                    |
| `assets/`         | Imágenes y capturas del tutorial                                   | Todos (nombrar con sentido)                       |
| `docs/`           | Documentos complementarios (PDF, esquemas, etc.)                   | Opcional                                          |
| `ejemplos/`       | Código o ejemplos adicionales relacionados al contenido            | Todos                                             |
| `index.md`        | Página principal del sitio web con enlaces a cada sección          | Coordinador (Jhon) + colaboradores con aprobación |
| `_config.yml`     | Configuración del sitio web y navegación                           | Solo Jhon (o previa revisión)                     |
| `.gitignore`      | Lista de archivos/carpetas que no deben subirse al repositorio     | Coordinador                                       |
| `README.md`       | Este archivo (descripción general y guía de colaboración)          | Coordinador                                       |

---

## 📝 Plan de trabajo para los colaboradores

### 🔧 Paso 1: Redactar tu sección

1. Dirígete a la carpeta `_pages/`.
2. Abre el archivo `.md` correspondiente a tu tema.

   * Ejemplo: `issues.md`, `github_projects.md`, `pull_requests.md`, etc.
3. Redacta o edita el contenido asignado respetando la estructura Markdown.
4. Asegúrate de que el archivo tenga al inicio este bloque (front matter):

```yaml
---
title: "Nombre del tema"
nav_order: X
parent: "Contenido"
permalink: /nombre-url
layout: default
---
```

* Cambia `X` por el orden que tendrá en el menú (1, 2, 3…).
* Cambia `"nombre-url"` por el enlace que tendrá (por ejemplo: `/issues`).

---

### 🔗 Paso 2: Enlazar tu sección al `index.md`

1. Abre el archivo `index.md`.
2. Busca el bloque de contenido (enlace o botón) donde debería aparecer tu tema.
3. Añade tu entrada así:

```markdown
## X. Nombre del tema

Breve descripción de tu sección...

🔗 [Leer más...]({{ site.baseurl }}/nombre-url)
```

Ejemplo real:

```markdown
## 2. Issues

Los Issues permiten organizar el trabajo colaborativo: reportar errores, asignar tareas y planificar el desarrollo.

🔗 [Leer más...]({{ site.baseurl }}/issues)
```

---

### ✅ Buenas prácticas

* Subir imágenes a `assets/` y enlazarlas con:

  ```markdown
  ![Descripción]({{ site.baseurl }}/assets/nombre-imagen.png)
  ```

* Hacer los cambios en una rama diferente (por ejemplo, `mejora-seccion-issues`).

* Crear un Pull Request explicando qué sección editaste.

* No hacer `push` directo a `main`.

---


- Los aportes deben realizarse mediante ramas y Pull Requests.
- No se debe hacer push directo a la rama `main`.

Para más información sobre el flujo de trabajo, revisar los **issues** asignados o contactar al coordinador del proyecto.


