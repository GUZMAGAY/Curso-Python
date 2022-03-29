import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class saludo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('saludo.ui', self)
        self.btn_saludo.clicked.connect(self.fn_saludo)
       
        
    def fn_saludo(self):
        self.etq_saludar.setText(self.txt_nombre.toPlainText())
    
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    GUI = saludo()
    GUI.show()
    sys.exit(app.exec_())