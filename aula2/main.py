import flet as ft

def main(page: ft.Page):

    # devemos definir o parametro da função sendo um 'e' de event
    def add_task(e):
        print(new_task.value)

    new_task = ft.TextField(hint_text='Insira uma tarefa...')
    new_button = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)

    page.floating_action_button = new_button
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_FLOAT


    page.add(new_task, new_button)

ft.app(target=main)