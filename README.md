# AirDragon

_Air + BasecoatUI made easy._

AirDragon is a powerful framework that combines the capabilities of Air with the simplicity of BasecoatUI, allowing developers to create stunning user interfaces with ease. Whether you're building web applications, mobile apps, or desktop software, AirDragon provides the tools you need to bring your vision to life.


## Installation

To install AirDragon's Python component, run the following command in your terminal:

```bash
uv add airdragon
```

AirDragon's `layout` function handles the JS dependencies for you, but if you need to include them in Jinja, use the following HTML snippets:

```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/basecoat-css@0.3.6/dist/basecoat.cdn.min.css">
    <script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3.6/dist/js/all.min.js" defer></script>
    <script src="https://unpkg.com/lucide@latest"></script>    
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  </head>
  <body>
    <!-- Your content goes here -->
  </body>
</html>
``` 





