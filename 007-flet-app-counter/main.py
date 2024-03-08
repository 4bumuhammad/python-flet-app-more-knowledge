import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        title=ft.Text("Counter"),
        center_title=False,
        bgcolor=ft.colors.BLUE,
        automatically_imply_leading=False,
    )

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        content=ft.Row(
            controls=[
                ft.Container(expand=True),
                ft.Text("by Dhony Abu Muhammad", size=20),
                ft.Container(expand=True),
            ]
        ),        
    )

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main,port=8888)


## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Berhasil
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
