import air
import airdragon as ad

app = air.Air()


@app.page
def index():
    return ad.layout(
        ad.H1("Hello, world", class_="Dragons"),
        ad.Article(
            air.Ul(
                air.Li(
                    ad.Avatar(src="https://avatars.githubusercontent.com/u/62857"),
                ),
                air.Li(
                    ad.Avatar(src="https://avatars.githubusercontent.com/u/74739"),
                ),
            ),
        ),
        ad.Article(
            ad.AvatarGroup(
                ad.Avatar(src="https://avatars.githubusercontent.com/u/62857"),
                ad.Avatar(src="https://avatars.githubusercontent.com/u/74739"),
            ),
        ),
        ad.Article(
            ad.Card(
                air.Header(air.H2("Card title"), air.P("I am a handy paragraph.")),
                air.Section(
                    ad.ButtonGroup(
                        ad.Button("Click me"),
                        ad.Button("Don't click me", modifier=ad.ButtonMods.destructive),
                    )
                ),
            ),
            ad.Card(
                air.Header(air.H2("Card title"), air.P("I am a handy paragraph.")),
                air.Section(
                    ad.ButtonGroup(
                        ad.Button("Click me"),
                        ad.Button("Don't click me", modifier=ad.ButtonMods.destructive),
                    )
                ),
            ),
            ad.Card(
                air.Header(air.H2("Card title"), air.P("I am a handy paragraph.")),
                air.Section(
                    ad.ButtonGroup(
                        ad.Button("Click me"),
                        ad.Button("Don't click me", modifier=ad.ButtonMods.destructive),
                    )
                ),
            ),
            ad.Card(
                air.Header(air.H2("Card title"), air.P("I am a handy paragraph.")),
                air.Section(
                    ad.ButtonGroup(
                        ad.Button("Click me"),
                        # ad.Button("Don't click me", modifier=ad.ButtonMods.destructive),
                    )
                ),
            ),
            ad.Card(
                air.Header(air.H2("Card title"), air.P("I am a handy paragraph.")),
                air.Section(
                    ad.ButtonGroup(
                        ad.Button("Click me"),
                        # ad.Button("Don't click me", modifier=ad.ButtonMods.destructive),
                    )
                ),
            ),
            ad.Card(
                air.Header(air.H2("Card title"), air.P("I am a handy paragraph.")),
                air.Section(
                    ad.ButtonGroup(
                        ad.Button("Click me"),
                        # ad.Button("Don't click me", modifier=ad.ButtonMods.destructive),
                    )
                ),
            ),
        ),
    )
