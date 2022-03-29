import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic

class ejemplo_Gui(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('activar.ui', self)
        self.btn_activar.clicked.connect(self.fn_activar)
        self.btn_desactivar.clicked.connect(self.fn_desactivar)
        
    def fn_activar(self):
        self.btn_desactivar.setEnabled(True)
        self.btn_activar.setEnabled(False)
        self.etiqueta.setText('Activado')    
    
    def fn_desactivar(self):
        self.btn_desactivar.setEnabled(False)
        self.btn_activar.setEnabled(True)
        self.etiqueta.setText('Desactivado')    
    
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    GUI = ejemplo_Gui()
    GUI.show()
    sys.exit(app.exec_())