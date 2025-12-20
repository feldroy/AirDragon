import airdragon as ad


def test_Alert():
    html = ad.Alert("Alert message").render()
    assert html == '<div class="alert">Alert message</div>'


def test_Article():
    html = ad.Article("Article content").render()
    assert (
        html
        == '<article class="flex flex-col gap-4 sm:flex-row sm:flex-wrap py-2">Article content</article>'
    )


def test_Avatar():
    html = ad.Avatar(src="avatar.jpg").render()
    assert (
        html
        == '<img src="avatar.jpg" class="size-8 shrink-0 object-cover rounded-full"/>'
    )


def test_AvatarGroup():
    html = ad.AvatarGroup("Avatars").render()
    assert html == '<div class="flex -space-x-3">Avatars</div>'


def test_Badge():
    html = ad.Badge("New").render()
    assert html == '<span class="badge">New</span>'


def test_Button():
    html = ad.Button("Click me").render()
    assert html == '<button class="btn">Click me</button>'


def test_ButtonGroup():
    html = ad.ButtonGroup("Buttons").render()
    assert html == '<div class="button-group" role="group">Buttons</div>'


def test_Card():
    html = ad.Card("Card content").render()
    assert html == '<div class="card">Card content</div>'


def test_Form():
    html = ad.Form("Contents").render()
    assert html == '<form class="form grid gap-6">Contents</form>'


def test_H1():
    html = ad.H1("Hello, world.").render()
    assert (
        html
        == '<h1 class="text-3xl sm:text-4xl font-semibold leading-tight">Hello, world.</h1>'
    )


def test_H2():
    html = ad.H2("Medium heading").render()
    assert (
        html
        == '<h2 class="text-2xl sm:text-3xl font-semibold leading-tight">Medium heading</h2>'
    )


def test_H3():
    html = ad.H3("Subheading").render()
    assert (
        html
        == '<h3 class="text-xl sm:text-2xl font-semibold leading-tight">Subheading</h3>'
    )


def test_Input():
    html = ad.Input(placeholder="Search").render()
    assert html == '<input type="text" placeholder="Search" class="input"/>'


def test_Input_with_attrs():
    html = ad.Input(type="search", name="q", id="search-box").render()
    assert html == '<input type="search" name="q" id="search-box" class="input"/>'


def test_Link():
    html = ad.Link("Click here", href="https://example.com").render()
    assert html == '<a href="https://example.com" class="link">Click here</a>'


def test_Link_with_target():
    html = ad.Link("External", href="https://example.com", target="_blank").render()
    assert (
        html
        == '<a href="https://example.com" target="_blank" class="link">External</a>'
    )
