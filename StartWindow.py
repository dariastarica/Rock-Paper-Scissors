from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QGroupBox, QMessageBox, QLabel

from GameWindow import GameWindow


class StartWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.total_rounds = 0

        self.start_button = QPushButton()

        self.text_input = QLineEdit("3")

        self.layout = QVBoxLayout()

        self.start_group_box = QGroupBox()
        self.start_group_box_layout = QGridLayout()

        self.setup()

    def setup(self):
        self.start_button.clicked.connect(self.start_button_clicked)

        self.start_button.setIcon(QIcon("start.png"))
        self.start_button.setIconSize(QSize(100, 150))

        self.start_group_box_layout.addWidget(QWidget(), 0, 0)
        self.start_group_box_layout.addWidget(self.start_button, 0, 1)
        self.start_group_box_layout.addWidget(QWidget(), 0, 2)

        self.start_group_box.setLayout(self.start_group_box_layout)

        label = QLabel("How many games would you want to play?")

        self.layout.addWidget(self.start_group_box)
        self.layout.addWidget(label)
        self.layout.addWidget(self.text_input)

        self.setLayout(self.layout)

    def start_button_clicked(self):

        if self.text_input.text() == '' or not self.text_input.text().isdecimal():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Please enter how many games you want to play!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        self.hide()
        self.total_rounds = self.text_input.text()
        self.parent.game_window = GameWindow(self.parent, self.total_rounds)
        self.parent.game_window.show()
