---
title: "GitHub Pages"
nav_order: 7
parent: "Contenido"
permalink: /github_pages
layout: default
---

# GitHub Pages

## ¿Qué es GitHub Pages?

**GitHub Pages** es una funcionalidad gratuita que permite convertir un repositorio en un sitio web estático directamente desde tu código Markdown o HTML. Es ideal para documentación, portafolios, blogs y tutoriales.

## ⚙️ ¿Cómo se configura GitHub Pages?

1. Ve al repositorio en GitHub.
2. Entra a **Settings > Pages**.
3. Selecciona la rama a usar (por ejemplo `main`) y la carpeta base (`/root` o `/docs`).
4. Guarda y espera unos segundos.
5. Tu web estará disponible en una URL como:

```
[https://tuusuario.github.io/tu-repositorio](https://tuusuario.github.io/tu-repositorio)
````

---

## Implementación en este proyecto

En este tutorial colaborativo, **usamos GitHub Pages para presentar todo el contenido de manera visual y navegable**. Aquí te explicamos cómo lo hicimos paso a paso:

---

### 1. Creamos un archivo `index.md`

Este archivo es el punto de entrada del sitio. Contiene una tabla de contenido con enlaces a cada tema del tutorial.

```markdown
### Ejemplo de enlace:
🔗 [Leer más...](docs/issues.md)
````

Este `index.md` se encuentra en la raíz del repositorio y actúa como página de inicio.

---

### ⚙️ 2. Configuramos el archivo `_config.yml`

Este archivo define los metadatos del sitio y es clave para que GitHub Pages funcione correctamente con Jekyll (el motor que renderiza el sitio).

```yaml
title: Tutorial de GitHub
description: Guía colaborativa para dominar GitHub
author: Jhon Villegas

url: "https://jhojha.github.io"
baseurl: "/TUTORIAL-GITHUB"

theme: jekyll-theme-minimal

sass:
  sass_dir: assets/css
  style: compressed

include:
  - assets/css

nav:
  - title: "Inicio"
    url: /
  - title: "Repositorio"
    url: https://github.com/JhoJha/TUTORIAL-GITHUB
  - title: "Ver TUTORIAL.md"
    url: /TUTORIAL.md
```

📌 El campo `baseurl` fue clave para que los enlaces funcionaran correctamente al estar en una subcarpeta.

---

### 🎨 3. Estilizamos el sitio con SCSS personalizado

Creamos un archivo `.scss` dentro de `assets/css/` con un diseño adaptado a la lectura:

* Fondo crema claro.
* Tipografía legible.
* Layout responsive.
* Colores amigables para la vista.

```scss
@import "{{ site.theme }}";

body {
  background-color: #fdf6e3;
  color: #2c3e50;
  font-family: "Segoe UI", "Helvetica Neue", sans-serif;
}
```

El estilo fue aplicado automáticamente al agregar el SCSS en el `include:` del `_config.yml`.

---

### 🖼️ 4. Vista real del sitio publicado

#### 📷 Vista general del sitio web

![Vista general del sitio](../assets/pages_vista_1.png)

#### 📷 Menú de navegación personalizado

![Menú lateral con enlaces](../assets/pages_vista_2.png)

---

## Ventajas de usar GitHub Pages en este proyecto

* Permite mostrar el contenido de forma clara y ordenada.
* Transforma el repositorio en una experiencia visual accesible.
* Facilita la exposición ante la profesora o cualquier evaluador.
* Sirve como portafolio digital para mostrar el trabajo realizado.

---

## Conclusión

Gracias a GitHub Pages, este tutorial dejó de ser solo archivos `.md` para convertirse en una **guía web profesional y navegable**. Aprender a configurar y publicar con GitHub Pages es una habilidad fundamental para todo desarrollador moderno.
