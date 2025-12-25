from functools import cached_property
from enum import StrEnum, EnumType

import air
from air.tags.utils import locals_cleanup
from air.tags.models.types import Renderable, AttributeType


class Mods(StrEnum):
    destructive = "destructive"
    secondary = "secondary"
    outline = "outline"


class ButtonMods(StrEnum):
    destructive = "destructive"
    secondary = "secondary"
    outline = "outline"
    ghost = "ghost"
    link = "link"
    # size
    sm = "sm"
    lg = "lg"
    # TODO add icons and combinations


class _BaseTag:
    class_: str | None

    @cached_property
    def attrs(self) -> str:
        """Return the formatted HTML attributes string.

        Returns:
            A string containing formatted attributes prefixed with a space,
            or an empty string when no attributes are present.
        """
        # Handle modifiers and classes
        if getattr(self, "class_", None) and "modifier" in self._attrs:
            modifier = self._attrs.pop("modifier")
            if isinstance(modifier, EnumType) or modifier == "":
                modifier = ""
            else:
                modifier = f"-{modifier}"
            class_ = f"{self.class_}{modifier}"
        elif getattr(self, "class_", None):
            class_ = self.class_

        # Combine the tag class and any user submitted ones
        if class_ and "class_" in self._attrs:
            self._attrs["class_"] = f"{class_} {self._attrs['class_']}"
        elif class_:
            self._attrs["class_"] = class_
        return " " + " ".join(
            self._format_attr(key)
            for key, value in self._attrs.items()
            if value is not False
        )


class DragonTag(_BaseTag, air.BaseTag):
    pass


class DragonTagSelfClosing(_BaseTag, air.SelfClosingTag):
    pass


class Alert(DragonTag):
    class_ = "alert"

    def __init__(
        self,
        *children: Renderable,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        modifier: Mods | str = "",
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(*children, **kwargs | locals_cleanup(locals()))

    def render(self) -> str:
        return f"""<div{self.attrs}>{self.children}</div>"""


class Article(DragonTag):
    class_ = "flex flex-col gap-4 sm:flex-row sm:flex-wrap py-2"


class Avatar(DragonTagSelfClosing):
    class_ = "size-8 shrink-0 object-cover rounded-full"

    def __init__(
        self,
        *,
        src: str,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        modifier: Mods | str = "",
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(**kwargs | locals_cleanup(locals()))

    def render(self):
        return f"""<img{self.attrs}/>"""


class AvatarGroup(DragonTag):
    class_ = "flex -space-x-3"

    def render(self) -> str:
        return f"""<div{self.attrs}>{self.children}</div>"""


class Badge(DragonTag):
    class_ = "badge"

    def __init__(
        self,
        *children: Renderable,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        modifier: Mods | str = "",
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(*children, **kwargs | locals_cleanup(locals()))

    def render(self) -> str:
        return f"""<span{self.attrs}>{self.children}</span>"""


class Button(DragonTag):
    class_ = "btn"

    def __init__(
        self,
        *children: Renderable,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        modifier: ButtonMods | str = "",
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(*children, **kwargs | locals_cleanup(locals()))

    def render(self) -> str:
        return f"""<button{self.attrs}>{self.children}</button>"""


class ButtonGroup(DragonTag):
    class_ = "button-group"

    def render(self) -> str:
        return f"""<div{self.attrs} role="group">{self.children}</div>"""


class Card(DragonTag):
    class_ = "card"

    def render(self) -> str:
        return f"""<div{self.attrs}>{self.children}</div>"""


class Form(DragonTag):
    class_ = "form grid gap-6"


class H1(DragonTag):
    class_ = "text-3xl sm:text-4xl font-semibold leading-tight"


class H2(DragonTag):
    class_ = "text-2xl sm:text-3xl font-semibold leading-tight"


class H3(DragonTag):
    class_ = "text-xl sm:text-2xl font-semibold leading-tight"


class Input(DragonTagSelfClosing):
    """A styled input field using BasecoatUI's input class.

    Renders an <input> element with consistent styling for forms and search bars.
    Automatically applies the "input" class - no need to specify Tailwind classes.

    When to use:
        Use ad.Input instead of air.Input when you want BasecoatUI styling
        without manually adding class_="input".

        # Without AirDragon (verbose):
        air.Input(class_="input", type="email", placeholder="Email")

        # With AirDragon (clean):
        ad.Input(type="email", placeholder="Email")
        # -> <input type="email" placeholder="Email" class="input"/>

    Composition:
        Typically used inside ad.Form or ad.Card with labels:

        >>> ad.Form(
        ...     air.Label("Email", for_="email"),
        ...     ad.Input(id="email", type="email", placeholder="you@example.com"),
        ...     ad.Button("Submit", type="submit"),
        ... )

        For search bars, combine with ad.Button in a fieldset:

        >>> ad.Card(
        ...     air.Fieldset(
        ...         ad.Input(type="search", name="q", placeholder="Search..."),
        ...         ad.Button("Search"),
        ...         role="group",
        ...     ),
        ... )

    Args:
        type: The input type (e.g., "text", "search", "email", "password").
            Defaults to "text".
        name: The form field name for submission.
        id: The element's unique identifier.
        placeholder: Hint text displayed when the input is empty.
        value: The initial value of the input.
        class_: Additional CSS classes to append (not replace) the default
            "input" class.
        style: Inline CSS styles.
        **kwargs: Additional HTML attributes (e.g., autofocus, required,
            disabled, hx_get, hx_trigger for HTMX).

    Example:
        >>> ad.Input(type="search", name="q", placeholder="Search...")
        <input type="search" name="q" placeholder="Search..." class="input"/>

    Example with HTMX:
        >>> ad.Input(
        ...     type="search",
        ...     name="q",
        ...     hx_get="/search",
        ...     hx_trigger="keyup changed delay:300ms",
        ... )
    """

    class_ = "input"

    def __init__(
        self,
        *,
        type: str = "text",
        name: str | None = None,
        id: str | None = None,
        placeholder: str | None = None,
        value: str | None = None,
        class_: str | None = None,
        style: str | None = None,
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(**kwargs | locals_cleanup(locals()))

    def render(self):
        return f"""<input{self.attrs}/>"""


class Link(DragonTag):
    """A styled anchor link using BasecoatUI's link class.

    Renders an <a> element with consistent styling for navigation and references.
    Automatically applies the "link" class for BasecoatUI styling.

    When to use:
        Use ad.Link instead of air.A when you want BasecoatUI link styling
        without manually adding class_="link".

        # Without AirDragon (verbose):
        air.A("Click here", href="/page", class_="link")

        # With AirDragon (clean):
        ad.Link("Click here", href="/page")
        # -> <a href="/page" class="link">Click here</a>

    Composition:
        Works anywhere you need navigation. Common patterns:

        Inside headings (e.g., for card titles):

        >>> ad.Card(
        ...     ad.H3(ad.Link("Article Title", href="/article/123")),
        ...     air.P("Article description..."),
        ... )

        In navigation lists:

        >>> air.Nav(
        ...     air.Ul(
        ...         air.Li(ad.Link("Home", href="/")),
        ...         air.Li(ad.Link("About", href="/about")),
        ...         air.Li(ad.Link("Contact", href="/contact")),
        ...     ),
        ... )

        External links (open in new tab):

        >>> ad.Link("View docs", href="https://docs.example.com", target="_blank")

    Args:
        *children: The link text or nested elements to display.
        href: The URL the link points to (required).
        class_: Additional CSS classes to append (not replace) the default
            "link" class.
        id: The element's unique identifier.
        style: Inline CSS styles.
        target: Where to open the link (e.g., "_blank" for new tab).
        **kwargs: Additional HTML attributes (e.g., rel="noopener" for security,
            download for file downloads, hx_get for HTMX navigation).

    Example:
        >>> ad.Link("Visit site", href="https://example.com", target="_blank")
        <a href="https://example.com" target="_blank" class="link">Visit site</a>

    Example with nested content:
        >>> ad.Link(air.Strong("Important"), " link", href="/important")
        <a href="/important" class="link"><strong>Important</strong> link</a>
    """

    class_ = "link"

    def __init__(
        self,
        *children: Renderable,
        href: str,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        target: str | None = None,
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(*children, **kwargs | locals_cleanup(locals()))

    def render(self) -> str:
        return f"""<a{self.attrs}>{self.children}</a>"""
