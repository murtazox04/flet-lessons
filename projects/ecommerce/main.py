import flet as ft


def main(page: ft.Page):
    page.title = "Demo Ecom"
    page.horizontal_alignment = "center"
    page.update()


app = ft.app(target=main)
