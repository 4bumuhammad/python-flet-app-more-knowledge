# Flet app more knowledge


### Begin Project :

    ❯ pwd

        /Users/.../python-flet-app-more-knowledge

    ❯ python -m venv venv

    ❯ source ./venv/bin/activate

    ❯ pip install flet

    ❯ cd <project-name>


### Code :

    import flet as ft


    def main(page: ft.Page):
        page.horizontal_alignment = page.vertical_alignment = "center"

        page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
        page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

        page.appbar = ft.AppBar(
            title=ft.Text("Bottom AppBar Demo"),
            center_title=True,
            bgcolor=ft.colors.GREEN_300,
            automatically_imply_leading=False,
        )
        page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.BLUE,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                ]
            ),
        )

        page.add(ft.Text("Body!"))


    ft.app(target=main)




### &#x1F3C3; Run :

command for deploy desktop app

    ❯ flet main.py -d 


command for deploy web

    ❯ flet main.py -w

    

### Result :

<p align="center">
    <img src="./gambar-petunjuk/under_construction_small.png" alt="under_construction_small" style="display: block; margin: 0 auto;">
</p>
<p align="center">desktop apps</p>

---

<p align="center">
    <img src="./gambar-petunjuk/under_construction_small.png" alt="under_construction_small" style="display: block; margin: 0 auto;">
</p>
<p align="center">web</p>


### Notes :

    ❯ flet --version

        0.21.1
