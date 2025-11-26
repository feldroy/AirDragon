# AirDragon

_Air + BasecoatUI + TailwindCSS made easy._

AirDragon combines the capabilities of [Air]() with the simplicity of [BasecoatUI](https://basecoatui.com/) and the deep power of [Tailwind](https://tailwindcss.com/), allowing developers to create stunning user interfaces with ease. Whether you're building web applications, mobile apps, or desktop software, AirDragon provides the tools you need to bring your vision to life.

## Mandate

1. Provide a simple way to use BasecoatUI and Tailwind with Air.
2. Offer pre-built components and layouts that leverage BasecoatUI's design principles.
3. Ensure seamless integration with Air's existing features and functionalities and design theme.
4. No need to learn any Tailwind classes, just use AirDragon components.
5. Make it easy to customize and extend the components to fit specific project needs. 


## Installation

To install AirDragon's Python component, run the following command in your terminal:

```bash
uv add airdragon
```

### AirDragon with a Jinja base template

AirDragon's `layout()` function handles the JS dependencies for you, but if you need to include them in Jinja, use the following HTML snippets:

```html
<!-- Jinja base template, for Air Tags use airdragon.layout() -->
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

## Usage

To use AirDragon in your Air application, simply import the `airdragon` module and use the provided components and layout function. Here's a basic example:

```python
import air
import airdragon as ad

app = air.Air()

@app.page
def index():
    return ad.layout(
        # Adding a class_ to an AirDragon tag appends it to the list of
        # tailwind classes applied to that tag by AirDragon.
        # So this will be 
        # <h1 class="text-3xl sm:text-4xl font-semibold leading-tight Dragons">
        ad.H1('Hello, world', class_='Dragons'),
        ad.Card(
            air.Header(
                air.H2('Card title'),
                air.P('I am a handy paragraph.')
            ),
            air.Section(
                ad.ButtonGroup(
                    ad.Button('Click me'),
                    ad.Button("Don't click me", modifier=ad.ButtonMods.destructive)
                )
            )
        )        
    )
```
