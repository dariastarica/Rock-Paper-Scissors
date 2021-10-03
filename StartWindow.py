from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QGroupBox, QLabel, QMessageBox

from GameWindow import GameWindow


class StartWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.total_rounds = 0

        self.start_button = QPushButton()
        self.text_input = QLineEdit()

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

        label = QLabel("Number of rounds: ")
        label.setFont(QFont("Arial", 10))
        self.layout.layout().addItem(QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))
        self.layout.addWidget(self.start_group_box)

        text_input_group_box = QGroupBox()
        text_input_group_box_layout = QVBoxLayout()

        text_input_group_box_layout.addWidget(label)
        text_input_group_box_layout.addWidget(self.text_input)

        text_input_group_box.setLayout(text_input_group_box_layout)

        self.layout.addWidget(text_input_group_box)

        self.setLayout(self.layout)

        self.setLayout(self.layout)

    def start_button_clicked(self):

        if self.text_input.text() == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('More information')
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        self.hide()
        self.total_rounds = self.text_input.text()
        self.parent.game_window = GameWindow(self.parent, self.total_rounds)
        self.parent.game_window.show()