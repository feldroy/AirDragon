import air
import airdragon as ad

app = air.Air()


@app.page
def index():
    return ad.layout(
        ad.H1("Hello, world", class_="Dragons"),
        ad.Card(
            air.Header(air.H2("Card title"), air.P("I am a handy paragraph.")),
            air.Section(
                ad.ButtonGroup(
                    ad.Button("Click me"),
                    ad.Button("Don't click me", modifier=ad.ButtonMods.destructive),
                )
            ),
        ),
    )
