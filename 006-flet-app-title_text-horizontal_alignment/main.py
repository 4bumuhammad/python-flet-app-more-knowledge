import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = 'CENTER'
    page.title = "app test - dhony abu muhammad"
    page.scroll = "adaptive"
    title_text = ft.Text(
        value=f"Jakarta +62",
        size=60,
        weight=ft.FontWeight.W_100,
        text_align="CENTER"
    )
    page.add(title_text)
    page.update()


ft.app(target=main, port=8888)


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Berhasil
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
