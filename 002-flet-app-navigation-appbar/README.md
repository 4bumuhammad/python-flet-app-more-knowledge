# Flet app more knowledge


### &#x1F530; Begin Project :

    ❯ pwd

        /Users/.../python-flet-app-more-knowledge

    ❯ python -m venv venv

    ❯ source ./venv/bin/activate

    ❯ pip install flet

    ❯ cd <project-name>


### &#x1FAB6; Code :

    import flet as ft

    def main(page: ft.Page):
        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            page.update()

        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            leading_width=40,
            title=ft.Text("AppBar Example"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False, on_click=check_item_clicked
                        ),
                    ]
                ),
            ],
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

    ft.app(target=main)




### &#x1F3C3; Run :

command for deploy desktop app

    ❯ flet main.py -d 


command for deploy web

    ❯ flet main.py -w

    

### &#x1F3C5; Result :

<p align="center">
    <img src="./gambar-petunjuk/ss_flet_app_desk_1.png" alt="ss_flet_app_desk_1" style="display: block; margin: 0 auto;">
</p>
<p align="center">desktop apps</p>

---

<p align="center">
    <img src="./gambar-petunjuk/ss_flet_app_web_1.png" alt="ss_flet_app_web_1" style="display: block; margin: 0 auto;">
</p>
<p align="center">web</p>


### &#x1FAA7; Notes :

    ❯ flet --version

        0.21.1
