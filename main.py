from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Ma TODO list")
        
        self.main_layout = QVBoxLayout(self)
        self.lw_todos = QListWidget()
        self.le_task_title = QLineEdit()
        self.le_task_title.setPlaceholderText("tache à effectuer")
        self.btn_clear = QPushButton("tout supprimer !")
        
        self.main_layout.addWidget(self.lw_todos)
        self.main_layout.addWidget(self.le_task_title)
        self.main_layout.addWidget(self.btn_clear)
        
        self.le_task_title.returnPressed.connect(self.add_todo)
        self.btn_clear.clicked.connect(self.lw_todos.clear)
        self.lw_todos.itemDoubleClicked.connect(self.delete_todo)
        
    def add_todo(self):
        self.lw_todos.addItem(self.le_task_title.text())
        self.le_task_title.clear()
        
    def delete_todo(self, item):
        self.lw_todos.takeItem(self.lw_todos.row(item))    
        
app = QApplication()
win = MainWindow()
win.show()
app.exec() 