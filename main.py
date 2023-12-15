from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from ui_login import Ui_tela_login
from ui_main import Ui_MainWindow
import sys
from banco_de_dados import KanbanDB


class Login(QWidget, Ui_tela_login):
    def __init__(self):
        super(Login, self).__init__()
        
        self.setupUi(self) # criando instância a partir do documento ui (setando Ui_tela_login)
        self.setWindowTitle("Login Kanban System")

        # chamando clique no botão
        self.btn_acessar.clicked.connect(self.abrir_sistema)

        


    

    def abrir_sistema(self):
        # validação de credenciais
        if self.usuario_input.text() == 'hugo' and self.senha_input.text() == '123': 
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            print('login ou senha inválida')
        


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self) # criando instância a partir do documento ui (setando Ui_MainWindow)
        self.setWindowTitle("Kanban System")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()