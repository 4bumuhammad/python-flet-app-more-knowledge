import flet as ft

def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    content = ft.Container(
        content = ft.Column([
            ft.Text("by Dhony Abu Muhammad", size=15)
        ])
    )

    page.add(ft.Image(src=f"/images/helloimage.jpeg"), content)

ft.app(
    target=main,
    assets_dir="assets", 
    port=8888
)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Berhasil
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
