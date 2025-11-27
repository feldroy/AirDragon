import airdragon as ad


def test_H1():
    html = ad.H1("Hello, world.").render()
    assert (
        html
        == '<h1 class="text-3xl sm:text-4xl font-semibold leading-tight">Hello, world.</h1>'
    )


def test_H3():
    html = ad.H3("Subheading").render()
    assert (
        html
        == '<h3 class="text-xl sm:text-2xl font-semibold leading-tight">Subheading</h3>'
    )


def test_Form():
    html = ad.Form("Contents").render()
    assert html == '<form class="form grid gap-6">Contents</form>'
