import flet as ft

def main(page: ft.Page):

    # devemos definir o parametro da função sendo um 'e' de event.
    def add_task(e):

        print(new_task.value)
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()   

    # criamos as variáveis contendo funções e algumas c configurações visuais.
    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True)
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    # aqui adicionamos tudo em uma variavel que é uma coluna onde os controles dela possui uma linha que adiciona o TextField e o Botão Flutuante na mesma linha.
    card = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        new_task,
                        new_button
                    ]   
                )
            ]
        )


    page.add(card)

ft.app(target=main)