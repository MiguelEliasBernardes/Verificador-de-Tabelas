import flet as ft
import verifica


def main(page: ft.Page):
    page.padding = 0
    page.window_width = 1024
    page.window_height = 700
    page.window_center()

    data = verifica.verifica_despesa()
    dados = verifica.ajusta_lista(data["array"])

    # Criando um contêiner de rolagem
    scroll_container = ft.Column(scroll='auto', expand=True)

    # Adicionando os dados ao contêiner de rolagem
    scroll_container.controls.append(ft.Text(dados))

    scroll_container.controls.append(ft.Text(f"Total: {data['total']}"))

    page.controls.append(scroll_container)

    page.update()

ft.app(main)