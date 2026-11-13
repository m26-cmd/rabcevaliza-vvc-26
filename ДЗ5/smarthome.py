import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout,
                             QStackedWidget, QMessageBox)


class Okno(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Умный дом")
        self.resize(350, 350)

        self.stack = QStackedWidget()

        glavny = QVBoxLayout()
        glavny.addWidget(self.stack)
        self.setLayout(glavny)

        self.makemenu()
        self.makeroom()

    def makemenu(self):
        self.menu = QWidget()
        lay = QVBoxLayout()

        zagolovok = QLabel("УМНЫЙ ДОМ")
        zagolovok.setStyleSheet("font-size: 18px; font-weight: bold;")
        lay.addWidget(zagolovok)

        podskazka = QLabel("Введите имя и выберите комнату:")
        lay.addWidget(podskazka)

        self.imya = QLineEdit()
        self.imya.setPlaceholderText("Ваше имя")
        lay.addWidget(self.imya)

        self.kuhnya = QPushButton("Кухня")
        self.kuhnya.clicked.connect(self.vkuhnyu)

        self.spalnya = QPushButton("Спальня")
        self.spalnya.clicked.connect(self.vspalnyu)

        self.gostinaya = QPushButton("Гостиная")
        self.gostinaya.clicked.connect(self.vgostinuyu)

        lay.addWidget(self.kuhnya)
        lay.addWidget(self.spalnya)
        lay.addWidget(self.gostinaya)

        self.menu.setLayout(lay)
        self.stack.addWidget(self.menu)

    def makeroom(self):
        self.room = QWidget()
        lay = QVBoxLayout()

        self.privet = QLabel("Комната")
        self.privet.setStyleSheet("font-size: 15px;")
        lay.addWidget(self.privet)

        lay.addWidget(QLabel("Температура:"))
        self.temperatura = QComboBox()
        self.temperatura.addItems(["18", "20", "22", "24"])
        lay.addWidget(self.temperatura)

        self.knopkatemp = QPushButton("Установить температуру")
        self.knopkatemp.clicked.connect(self.pomenyattemp)
        lay.addWidget(self.knopkatemp)

        self.svet = QPushButton("Включить свет")
        self.svet.clicked.connect(self.pomenyatsvet)
        lay.addWidget(self.svet)

        self.chainik = QPushButton("Вскипятить чайник")
        self.chainik.clicked.connect(self.kipit)
        lay.addWidget(self.chainik)

        self.status = QLabel("")
        self.status.setStyleSheet("color: gray;")
        lay.addWidget(self.status)

        self.nazad = QPushButton("Назад в меню")
        self.nazad.clicked.connect(self.vmenu)
        lay.addWidget(self.nazad)

        self.room.setLayout(lay)
        self.stack.addWidget(self.room)

    def vkuhnyu(self):
        self.proverka("Кухня")

    def vspalnyu(self):
        self.proverka("Спальня")

    def vgostinuyu(self):
        self.proverka("Гостиная")

    def proverka(self, komnata):
        name = self.imya.text().strip()
        if name == "":
            QMessageBox.warning(self, "Ошибка", "Сначала введите имя!")
            return
        self.privet.setText("Привет, " + name + "! Вы в комнате: " + komnata)
        self.status.setText("Свет выключен")
        self.room.setStyleSheet("background-color: #f0f0f0;")
        self.svet.setText("Включить свет")
        self.stack.setCurrentIndex(1)

    def pomenyatsvet(self):
        if self.svet.text() == "Включить свет":
            self.room.setStyleSheet("background-color: #fffacd;")
            self.svet.setText("Выключить свет")
            self.status.setText("Свет включен")
        else:
            self.room.setStyleSheet("background-color: #f0f0f0;")
            self.svet.setText("Включить свет")
            self.status.setText("Свет выключен")

    def pomenyattemp(self):
        t = self.temperatura.currentText()
        self.status.setText("Температура установлена: " + t + " градусов")

    def kipit(self):
        QMessageBox.information(self, "Чайник", "Чайник вскипел! Можно заваривать чай.")

    def vmenu(self):
        self.stack.setCurrentIndex(0)


app = QApplication(sys.argv)
okno = Okno()
okno.show()
sys.exit(app.exec())
