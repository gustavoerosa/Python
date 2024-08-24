import sys
from geradorcpf import gera_cpf
from validadorcpf import valida_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import desing


class ValidaGeraCpf(QMainWindow, desing.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn_valida_cpf.clicked.connect(self.valida_cpf)
        self.btn_gera_cpf.clicked.connect(self.gera_cpf)

    def valida_cpf(self):
        cpf = self.input_valida_cpf.text()
        self.line_retorno.setText(str(valida_cpf(cpf)))

    def gera_cpf(self):
        self.line_retorno.setText(str(gera_cpf()))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    valida_gera = ValidaGeraCpf()
    valida_gera.show()
    qt.exec_()
