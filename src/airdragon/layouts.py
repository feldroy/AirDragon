from typing import Any

import air
from air.tags.types import AttributeType


def layout(*children: Any, **kwargs: AttributeType) -> air.Html | air.Children:
    body_tags = air.layouts.filter_body_tags(children)
    head_tags = air.layouts.filter_head_tags(children)
    return air.Html(
        air.Head(
            air.Meta(charset="UTF-8"),
            air.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            air.Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/basecoat-css@0.3.6/dist/basecoat.cdn.min.css",
            ),            
            air.Script(
                src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3.6/dist/js/all.min.js"
            ),
            air.Script(src="https://unpkg.com/lucide@latest"),
            air.Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"),


            air.Body(
                air.Main(
                *[x for x in body_tags],
                class_="max-w-3xl mx-auto px-6 py-16"),
                class_="bg-gradient-to-b from-gray-50 to-white min-h-screen text-gray-800"
            ),
        )
)

