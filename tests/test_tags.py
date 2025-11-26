import airdragon as ad


def test_H1():
    html = ad.H1("Hello, world.").render()
    assert (
        html
        == '<h1 class="text-3xl sm:text-4xl font-semibold leading-tight">Hello, world.</h1>'
    )
