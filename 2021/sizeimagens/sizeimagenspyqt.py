import sys
from Secao6.sizeimagens.desing import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Redimensionar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_escolher_arquivo.clicked.connect(self.abrir_imagem)
        self.btn_redimensionar.clicked.connect(self.redimensionar)
        self.btn_salvar.clicked.connect(self.salver)

    def abrir_imagem(self):
        imagem, _ =QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'C:\Users\gusta\Pictures',
            options=QFileDialog.DontUseNativeDialog
        )
        self.input_abrir_arquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.label_img.setPixmap(self.original_img)
        self.input_largura.setText(str(self.original_img.width()))
        self.input_altura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.input_largura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.label_img.setPixmap(self.nova_imagem)
        self.input_largura.setText(str(self.nova_imagem.width()))
        self.input_altura.setText(str(self.nova_imagem.height()))

    def salver(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'C:\Users\gusta\Pictures',
            options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimen = Redimensionar()
    redimen.show()
    qt.exec_()