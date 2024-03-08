import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        bgcolor=ft.colors.SURFACE_VARIANT,
        trailing=ft.Icon(ft.icons.WB_SUNNY_OUTLINED),
      middle=ft.Text("CupertinoAppBar Test"),
    )

    content_1 = ft.Container(
        content = ft.Column([
            ft.Text("Hello From Flet", size=40)
        ])
    )

    content_2 = ft.Container(
        content = ft.Column([
            ft.Text("by Dhony Abu Muhammad", size=20)
        ])
    )

    page.add(content_1, content_2)


ft.app(target=main, port=8888)