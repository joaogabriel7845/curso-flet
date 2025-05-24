import flet as ft

def main(page: ft.Page):
    stack = ft.Stack(
        controls=[
            # Fundo azul (camada de baixo)
            ft.Container(width=200, height=200, bgcolor="blue"),

            # Texto posicionado na parte superior esquerda
            ft.Text("Topo esquerdo", color="white", left=10, top=10),

            # Botão posicionado no centro
            ft.ElevatedButton("Clique aqui", left=50, top=80)
        ],
        width=200,
        height=200
    )

    page.add(stack)

ft.app(target=main)