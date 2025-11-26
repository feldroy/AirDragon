from functools import cached_property
from enum import StrEnum, EnumType

import air
from air.tags.utils import locals_cleanup
from air.tags.types import Renderable, AttributeType


class Mods(StrEnum):
    destructive = 'destructive'
    secondary = 'secondary'
    outline = 'outline'

class ButtonMods(StrEnum):
    destructive = 'destructive'
    secondary = 'secondary'
    outline = 'outline'   
    ghost = 'ghost'
    link = 'link'     
    # size
    sm = 'sm'
    lg = 'lg'
    # TODO add icons and combinations


class DragonTag(air.BaseTag):
    class_: str | None

    @cached_property
    def attrs(self) -> str:
        """Return the formatted HTML attributes string.

        Returns:
            A string containing formatted attributes prefixed with a space,
            or an empty string when no attributes are present.
        """
        # Handle modifiers and classes
        if getattr(self, 'class_', None) and 'modifier' in self._attrs:
            modifier = self._attrs.pop('modifier')
            if isinstance(modifier, EnumType) or modifier is '':
                modifier = ''
            else:
                modifier = f'-{modifier}'
            class_ = f"{self.class_}{modifier}"
        elif getattr(self, 'class_', None):
            class_ = self.class_

        # Combine the tag class and any user submitted ones
        if class_ and 'class_' in self._attrs:
            self._attrs['class_'] = f'{class_} {self._attrs['class_']}'
        elif class_:
            self._attrs['class_'] = class_
        return " " + " ".join(self._format_attr(key) for key, value in self._attrs.items() if value is not False)    



class Alert(DragonTag):
    class_ = 'alert'

    def __init__(
        self,
        *children: Renderable,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        modifier: Mods | str = '',
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(*children, **kwargs | locals_cleanup(locals()))    

    def render(self) -> str:
        return f"""<div{self.attrs}>{self.children}</div>"""       


class Badge(DragonTag):

    class_ = 'badge'

    def __init__(
        self,
        *children: Renderable,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        modifier: Mods | str = '',
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(*children, **kwargs | locals_cleanup(locals()))    

    def render(self) -> str:
        return f"""<span{self.attrs}>{self.children}</span>"""   


class Button(DragonTag):

    class_ = 'btn'

    def __init__(
        self,
        *children: Renderable,
        class_: str | None = None,
        id: str | None = None,
        style: str | None = None,
        modifier: ButtonMods | str = '',
        **kwargs: AttributeType,
    ) -> None:
        super().__init__(*children, **kwargs | locals_cleanup(locals()))    

    def render(self) -> str:
        return f"""<button{self.attrs}>{self.children}</button>"""

class ButtonGroup(DragonTag):
    class_ = 'button-group'

    def render(self) -> str:
        return f"""<div{self.attrs} role="group">{self.children}</div>"""  
    

class Card(DragonTag):

    class_ = 'card'

    def render(self) -> str:
        return f"""<div{self.attrs}>{self.children}</div>"""
    

class H1(DragonTag):
    class_ = 'text-3xl sm:text-4xl font-semibold leading-tight'
