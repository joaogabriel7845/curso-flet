import flet as ft

class CheckBox(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, border=ft.InputBorder.UNDERLINE, filled=True,visible=False)
        self.edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=self.save,
                                         visible=False)
        self.delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=self.delete)

        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
            self.delete_button,
        ]


    # Criação das funções
    def edit(self, e):
        self.edit_button.visible = False
        self.delete_button.visible = False
        self.text_view.visible = False
        self.save_button.visible = True
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.text_edit.visible = False
        self.save_button.visible = False
        self.edit_button.visible = True
        self.delete_button.visible = True
        self.text_view.visible = True
        self.text_view.value = self.text_edit.value.capitalize()
        self.update()

    def delete(self, e):
        self.visible = False
        self.update()