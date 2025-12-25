# AirDragon - AI Context Guide

AirDragon is a Python UI component library that combines Air (Python web framework), BasecoatUI, and TailwindCSS. It provides pre-styled components so developers don't need to learn Tailwind CSS classes.

## Core Concept

AirDragon components automatically apply BasecoatUI classes. Use `ad.*` for styled components, `air.*` for structural HTML.

```python
# Without AirDragon (verbose):
air.Button("Click", class_="btn")
air.Input(class_="input", type="email")
air.A("Link", href="/", class_="link")

# With AirDragon (clean):
ad.Button("Click")           # -> <button class="btn">Click</button>
ad.Input(type="email")       # -> <input type="email" class="input"/>
ad.Link("Link", href="/")    # -> <a href="/" class="link">Link</a>
```

## Required Setup

Always wrap pages in `ad.layout()` - it injects BasecoatUI CSS/JS and TailwindCSS:

```python
import air
import airdragon as ad

app = air.Air()

@app.page
def index():
    return ad.layout(
        air.Title("My App"),
        ad.H1("Welcome"),
        # ... rest of content
    )
```

## Component Quick Reference

| Component | HTML Output | Default Class | Use For |
|-----------|-------------|---------------|---------|
| `ad.H1("text")` | `<h1>` | `text-3xl sm:text-4xl font-semibold leading-tight` | Page titles |
| `ad.H2("text")` | `<h2>` | `text-2xl sm:text-3xl font-semibold leading-tight` | Section headings |
| `ad.H3("text")` | `<h3>` | `text-xl sm:text-2xl font-semibold leading-tight` | Subsection headings |
| `ad.Button("text")` | `<button>` | `btn` | Actions, form submits |
| `ad.Input(...)` | `<input/>` | `input` | Form fields, search |
| `ad.Link("text", href=)` | `<a>` | `link` | Navigation, references |
| `ad.Card(...)` | `<div>` | `card` | Content grouping |
| `ad.Form(...)` | `<form>` | `form grid gap-6` | Form containers |
| `ad.Alert("text")` | `<div>` | `alert` | Notifications |
| `ad.Badge("text")` | `<span>` | `badge` | Labels, tags |
| `ad.Avatar(src=)` | `<img/>` | `size-8 shrink-0 object-cover rounded-full` | User images |
| `ad.AvatarGroup(...)` | `<div>` | `flex -space-x-3` | Stacked avatars |
| `ad.Article(...)` | `<article>` | `flex flex-col gap-4 sm:flex-row sm:flex-wrap py-2` | Flexible layouts |
| `ad.ButtonGroup(...)` | `<div role="group">` | `button-group` | Grouped buttons |

## Key Conventions

### 1. class_ appends, doesn't replace
```python
ad.Button("Click", class_="mt-4")
# -> <button class="btn mt-4">Click</button>
```

### 2. modifier= for variants
```python
ad.Button("Delete", modifier=ad.ButtonMods.destructive)
# -> <button class="btn-destructive">Delete</button>

ad.Button("Cancel", modifier=ad.ButtonMods.secondary)
# -> <button class="btn-secondary">Cancel</button>

ad.Alert("Error!", modifier=ad.Mods.destructive)
# -> <div class="alert-destructive">Error!</div>
```

### 3. Mix ad.* and air.* freely
Use `ad.*` for styled components, `air.*` for structure:
```python
ad.Card(
    air.Header(ad.H2("Title")),      # air for structure, ad for styled heading
    air.Section(air.P("Content")),   # air for structure and plain paragraph
    air.Footer(ad.Button("Save")),   # air for structure, ad for styled button
)
```

## Button Modifiers

```python
ad.ButtonMods.destructive  # Red/danger button
ad.ButtonMods.secondary    # Secondary style
ad.ButtonMods.outline      # Outline style
ad.ButtonMods.ghost        # Ghost/minimal style
ad.ButtonMods.link         # Looks like a link
ad.ButtonMods.sm           # Small size
ad.ButtonMods.lg           # Large size
```

## Common Patterns

### Search Bar
```python
ad.Card(
    air.Fieldset(
        ad.Input(type="search", name="q", placeholder="Search..."),
        ad.Button("Search"),
        role="group",
    ),
)
```

### Search with HTMX
```python
ad.Card(
    air.Fieldset(
        ad.Input(
            type="search",
            name="q",
            id="q",
            placeholder="Search...",
            hx_get="/search",
            hx_trigger="keyup changed delay:300ms",
            hx_target="#results",
        ),
        ad.Button("Search", hx_get="/search", hx_include="#q"),
        role="group",
    ),
)
```

### Form with Labels
```python
ad.Form(
    air.Div(
        air.Label("Email", class_="label", for_="email"),
        ad.Input(id="email", type="email", placeholder="you@example.com"),
        class_="grid gap-3",
    ),
    air.Div(
        air.Label("Password", class_="label", for_="password"),
        ad.Input(id="password", type="password"),
        class_="grid gap-3",
    ),
    ad.Button("Sign In", type="submit"),
)
```

### Card with Header and Actions
```python
ad.Card(
    air.Header(
        ad.H2("Card Title"),
        air.P("Description text"),
    ),
    air.Section(
        air.P("Main content goes here..."),
    ),
    air.Footer(
        ad.ButtonGroup(
            ad.Button("Save"),
            ad.Button("Cancel", modifier=ad.ButtonMods.secondary),
        ),
    ),
)
```

### Navigation with Links
```python
air.Nav(
    air.Ul(
        air.Li(ad.Link("Home", href="/")),
        air.Li(ad.Link("About", href="/about")),
        air.Li(ad.Link("Contact", href="/contact")),
    ),
)
```

### Card Grid with Links
```python
ad.Article(
    *[ad.Card(
        ad.H3(ad.Link(item.title, href=f"/items/{item.id}")),
        air.P(item.description),
    ) for item in items],
)
```

### Avatar Group
```python
ad.AvatarGroup(
    ad.Avatar(src="https://example.com/user1.jpg"),
    ad.Avatar(src="https://example.com/user2.jpg"),
    ad.Avatar(src="https://example.com/user3.jpg"),
)
```

### Alert Variants
```python
ad.Alert("Info message")                              # Default
ad.Alert("Warning!", modifier=ad.Mods.secondary)     # Secondary
ad.Alert("Error!", modifier=ad.Mods.destructive)     # Destructive
```

## Complete Page Example

```python
import air
import airdragon as ad

app = air.Air()

@app.page
def index():
    return ad.layout(
        air.Title("My App"),
        ad.H1("Dashboard"),
        air.P("Welcome to the dashboard."),

        ad.Article(
            ad.Card(
                air.Header(ad.H2("Users")),
                ad.AvatarGroup(
                    ad.Avatar(src="/avatars/1.jpg"),
                    ad.Avatar(src="/avatars/2.jpg"),
                ),
            ),
            ad.Card(
                air.Header(ad.H2("Actions")),
                ad.ButtonGroup(
                    ad.Button("Create"),
                    ad.Button("Export", modifier=ad.ButtonMods.secondary),
                ),
            ),
        ),

        ad.Card(
            ad.H3("Quick Search"),
            air.Fieldset(
                ad.Input(type="search", name="q", placeholder="Search..."),
                ad.Button("Go"),
                role="group",
            ),
        ),
    )
```

## When to Use air.* vs ad.*

| Need | Use | Example |
|------|-----|---------|
| Styled button | `ad.Button` | `ad.Button("Click")` |
| Styled input | `ad.Input` | `ad.Input(type="email")` |
| Styled link | `ad.Link` | `ad.Link("Home", href="/")` |
| Styled heading | `ad.H1/H2/H3` | `ad.H1("Title")` |
| Container with card styling | `ad.Card` | `ad.Card(...)` |
| Form with grid layout | `ad.Form` | `ad.Form(...)` |
| Plain paragraph | `air.P` | `air.P("Text")` |
| Structural divs | `air.Div` | `air.Div(..., class_="grid")` |
| Lists | `air.Ul/Li` | `air.Ul(air.Li(...))` |
| Semantic sections | `air.Header/Section/Footer` | `air.Header(...)` |
| Labels | `air.Label` | `air.Label("Email", for_="email")` |
| Any HTML not in AirDragon | `air.*` | `air.Nav(...)`, `air.Span(...)` |
