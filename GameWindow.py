from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QGroupBox, QVBoxLayout, QPushButton
import utils

from ResultWindow import ResultWindow


class GameWindow(QWidget):
    def __init__(self, parent, total_rounds):
        super().__init__(parent)

        self.player_last_choice = None
        self.parent = parent
        self.current_round_count = 1
        self.total_rounds = total_rounds

        self.scissors_button = QPushButton("Scissors")
        self.rock_button = QPushButton("Rock")
        self.paper_button = QPushButton("Paper")

        self.resize(800, 600)

        self.info_text_group_box = QGroupBox()
        self.buttons_group_box = QGroupBox()
        self.move_group_box = QGroupBox()

        self.info_text_group_box_layout = QHBoxLayout()
        self.buttons_group_box_layout = QHBoxLayout()
        self.move_group_box_layout = QVBoxLayout()

        self.layout = QVBoxLayout()

        self.setup()

    def setup_info(self):
        info_label = QLabel("Computer has chosen!\n Make your move...")

        info_label.setFont(QFont("Arial", 15))

        self.info_text_group_box_layout.addWidget(info_label)
        self.info_text_group_box_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.info_text_group_box.setLayout(self.info_text_group_box_layout)

        self.info_text_group_box.setFlat(True)

    def setup_move(self):
        info_label = QLabel("Choose one...")

        info_label.setFont(QFont('Arial', 10))

        self.move_group_box_layout.addWidget(info_label)
        self.move_group_box_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.move_group_box.setLayout(self.move_group_box_layout)

    def setup_buttons(self):
        self.paper_button.setIcon(QIcon("paper.png"))
        self.paper_button.setIconSize(QSize(100, 100))

        self.paper_button.clicked.connect(lambda: self.button_clicked(self.paper_button.text().lower()))

        self.rock_button.setIcon(QIcon("rock.png"))
        self.rock_button.setIconSize(QSize(100, 100))

        self.rock_button.clicked.connect(lambda: self.button_clicked(self.rock_button.text().lower()))

        self.scissors_button.setIcon(QIcon("scissors.png"))
        self.scissors_button.setIconSize(QSize(100, 100))

        self.scissors_button.clicked.connect((lambda: self.button_clicked(self.scissors_button.text().lower())))

        self.buttons_group_box_layout.addWidget(self.rock_button)
        self.buttons_group_box_layout.addWidget(self.paper_button)
        self.buttons_group_box_layout.addWidget(self.scissors_button)

        self.buttons_group_box.setLayout(self.buttons_group_box_layout)

    def setup(self):
        self.setup_info()
        self.setup_move()
        self.setup_buttons()

        self.round_count_label = QLabel("Current Round: " + str(self.current_round_count))
        self.round_count_label.setFont(QFont("Arial", 10))

        self.layout.addWidget(self.round_count_label)
        self.layout.addWidget(self.info_text_group_box)
        self.layout.addWidget(self.move_group_box)
        self.layout.addWidget(self.buttons_group_box)

        self.setLayout(self.layout)

        # self.set_flat()

    def set_flat(self):
        self.info_text_group_box.setFlat(True)
        self.move_group_box.setFlat(True)
        self.buttons_group_box.setFlat(True)

    def button_clicked(self, player_choice):
        computer_choice = utils.get_computer_choice(self.player_last_choice)

        utils.update_matrix(self.player_last_choice, player_choice)
        self.player_last_choice = player_choice
        result_window = ResultWindow(self.parent, player_choice, computer_choice, self.current_round_count,
                                     self.total_rounds)

        self.hide()
        result_window.show()
