import flet as ft
from custom_checkbox import CheckBox

def main(page: ft.Page):
    page.title='Minhas Tarefas'
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.resizable = False
    page.window.maximizable = False
    page.window.width = 450
    page.window.height = 650
    page.padding = ft.padding.only(top=20, left=20, right=20, bottom=20)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # capturar a largura e altura da pagina do nosso aplicativo
    WIDTH: int = page.width
    HEIGHT: int = page.height
    print(WIDTH, HEIGHT)

    # devemos definir o parametro da função sendo um 'e' de event.
    def add_task(e):
        if new_task.value == '':
            new_task.focus()       
            return
        task_list.controls.append(CheckBox(new_task.value.capitalize()))
        new_task.value = ''
        page.update()
        new_task.focus()       

    # criamos as variáveis contendo funções e algumas c configurações visuais.
    new_task = ft.TextField(hint_text='Insira uma tarefa...', expand=True, autofocus=True, on_submit=add_task, border_radius=5) # -> expand=True pega o valor da largura da janela e se expande/adapta.
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task, height=55)

    task_list = ft.Column(spacing=0, height=HEIGHT-170, scroll=ft.ScrollMode.ADAPTIVE)

    # white_card = ft.Container(
    #     task_list,
    #     width= 400,
    #     height= 700,
    #     bgcolor=ft.colors.WHITE,
    #     border_radius=20
    #     )

    # aqui adicionamos tudo em uma variavel que é uma coluna onde os controles dela possui uma linha que adiciona o TextField e o Botão Flutuante na mesma linha.
    card = ft.Column(
        width=400,
            controls=[
                ft.Row(
                    controls=[
                        new_task,
                        new_button
                    ]   
                ),
                task_list
            ]
        )


    page.add(card)

ft.app(target=main)