import air
import airdragon as ad

app = air.Air()

@app.page
def index():
    return ad.layout(
        air.H1('Hello, world', class_="text-3xl")
    )