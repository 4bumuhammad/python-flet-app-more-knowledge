import flet as ft


def main(page: ft.Page):
    page.title = "Markdown Editor"  # the title of our app
    page.theme_mode = "dark"
    
    page.appbar = ft.AppBar(
        title=ft.Text("Markdown Editor", color=ft.colors.WHITE),  # title of the AppBar with a white color
        center_title=True,  # we center the title
        bgcolor=ft.colors.BLUE,  # a color for the AppBar's background
    )
    
    text_field = ft.TextField(
        value="## Hello from Markdown",  # the initial value in the field (a simple Markdown code to test)
        multiline=True,  # True means: it will be possible to have many lines of text
        # on_change=md_update,
        expand=True,  # tells the field to 'expand' (take all the available space)
        border_color=ft.colors.TRANSPARENT,  # makes the border of the field transparent(invisible), creating an immersive effect
    )
    
    page.add(text_field)    # replaced the placeholder with our TextField (the LHS content)

ft.app(target=main,view=ft.WEB_BROWSER)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Berhasil
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
