import flet as ft

# classe para criar as tarefas
class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

        self.display_task = ft.Checkbox(
            value=False,
            label=self.task_name,
            on_change=self.status_change
            )

        self.edit_name = ft.TextField(
                expand=True,
                on_submit=self.save_clicked
            )

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip='Editar tarefa',
                            on_click = self.edit_clicked,
                            icon_color=ft.Colors.GREEN,                    
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            tooltip='Deletar tarefa',
                            on_click = self.delete_clicked,
                            icon_color=ft.Colors.RED, 
                        ),
                    ]
                ),
            ]
        )
        
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(icon=ft.Icons.DONE_OUTLINED,
                tooltip='Atualizar tarefa',
                on_click=self.save_clicked,
                icon_color=ft.Colors.GREEN,              
                ),
            ]
        )
        self.controls = [self.display_view, self.edit_view]


    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()


    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.edit_view.visible = True
        self.edit_name.focus()
        self.display_view.visible = False
        self.update()   

    
    def delete_clicked(self, e):
        self.task_delete(self)
        self.update()


    def status_change(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)
        self.update()



# classe para criar o aplicativo
class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()

        self.new_task = ft.TextField(
            hint_text='Qual tarefa precisa ser feita?',
            expand=True,
            on_submit=self.add_task,
            border_color=ft.Colors.WHITE
        )

        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change = self.tabs_changed,
            tabs=[
                ft.Tab(text='Todas'),
                ft.Tab(text='Ativas'),
                ft.Tab(text='Concluídas'),
            ],
        )

        self.items_left = ft.Text('0 Tarefas adicionadas')

        self.controls=[
                # Título da aplicação
                ft.Row(
                    controls=[
                        ft.Text(
                            value='Tarefas',
                            font_family='Montserrat',
                            theme_style='headlineMedium',
                            weight='bold',
                            color=ft.colors.with_opacity(0.8, 'white')
                        )
                    ],
                    alignment='center'
                ),
                # Inserção das tarefas
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_task),
                    ]
                ),
                # Lista de tarefas
                ft.Column(
                    controls=[
                        self.filter,
                        self.tasks,
                        ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                ft.OutlinedButton(
                                    text='Apagar todas as tarefas concluídas'.upper(),
                                    on_click=self.clear_completed_tasks
                                ),
                            ],
                        ),
                    ],
                ),
            ]







    def tabs_changed(self, e):
        self.update()

    def add_task(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ''
            self.new_task.focus()
            self.update()

    def clear_completed_tasks(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)


    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()


    def before_update(self):
        
        count = 0

        for task in self.tasks.controls:
            if not task.completed:
                count += 1

        self.items_left.value = 'f{count} Tarefa(s) não concluída(s)'


def main(page: ft.Page):
    page.title = 'Minhas Tarefas'
    page.window.resizable = False
    page.window.width = 500
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.only(top=20, bottom=20, left=20, right=20)
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.update()

    app = TodoApp()

    page.add(app)

ft.app(target=main)