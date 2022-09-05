from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
import utils


class ResultWindow(QWidget):
    def __init__(self, parent, player_choice, compute_choice, current_round_count, total_rounds):
        super().__init__(parent)

        self.replay_button = QPushButton("Replay")
        self.exit_button = QPushButton("Exit")
        self.resize(800, 600)

        self.parent = parent

        self.player_choice = player_choice
        self.computer_choice = compute_choice
        self.current_round_count = current_round_count
        self.total_rounds = total_rounds

        self.player_choice_box = QGroupBox()
        self.player_choice_box_layout = QVBoxLayout()

        self.computer_choice_box = QGroupBox()
        self.computer_choice_box_layout = QVBoxLayout()

        self.result_group_box = QGroupBox()
        self.result_group_box_layout = QHBoxLayout()

        self.info_group_box = QGroupBox()
        self.info_group_box_layout = QHBoxLayout()

        self.layout = QVBoxLayout()

        self.setup()

    def setup_player_choice(self):
        info_label = QLabel("You chose:")
        info_label.setFont(QFont('Arial', 10))
        choice_label_image = QLabel()
        path = self.player_choice + ".png"
        pixmap = QPixmap(path)
        choice_label_image.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))

        choice_label_info = QLabel(self.player_choice)
        choice_label_info.setFont(QFont("Arial", 15))

        self.player_choice_box_layout.addWidget(info_label)
        self.player_choice_box_layout.addWidget(choice_label_image)
        self.player_choice_box_layout.addWidget(choice_label_info)

        self.player_choice_box_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.player_choice_box.setLayout(self.player_choice_box_layout)

    def setup_computer_choice(self):
        info_label = QLabel("Computer chose:")
        info_label.setFont(QFont('Arial', 15))
        choice_label_image = QLabel()
        path = self.computer_choice + ".png"
        pixmap = QPixmap(path)
        choice_label_image.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))

        choice_label_info = QLabel(self.computer_choice)
        choice_label_info.setFont(QFont('Arial', 10))

        self.computer_choice_box_layout.addWidget(info_label)
        self.computer_choice_box_layout.addWidget(choice_label_image)
        self.computer_choice_box_layout.addWidget(choice_label_info)

        self.computer_choice_box_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.computer_choice_box.setLayout(self.computer_choice_box_layout)

    def setup_result_choice(self):
        result_text = utils.decide_winner(self.player_choice, self.computer_choice)
        info_label = QLabel(result_text)
        info_label.setFont(QFont('Arial', 15))

        self.info_group_box_layout.addWidget(info_label)
        self.info_group_box_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.info_group_box.setLayout(self.info_group_box_layout)

    def setup(self):
        self.setup_player_choice()
        self.setup_computer_choice()
        self.setup_result_choice()

        self.result_group_box_layout.addWidget(self.player_choice_box)
        self.result_group_box_layout.addWidget(self.computer_choice_box)

        self.result_group_box.setLayout(self.result_group_box_layout)

        self.layout.addWidget(self.result_group_box)
        self.layout.addWidget(self.info_group_box)

        groupbox = self.create_replay_exit_buttons_box()
        self.layout.addWidget(groupbox)

        self.setLayout(self.layout)

    def create_replay_exit_buttons_box(self):
        groupbox = QGroupBox()
        self.replay_button.clicked.connect(self.replay_button_clicked)

        self.replay_button.setFont(QFont("Arial", 10))

        self.exit_button.setFont(QFont("Arial", 10))
        self.exit_button.setEnabled(False)
        groupbox_layout = QHBoxLayout()
        self.exit_button.clicked.connect(self.exit_button_clicked)

        groupbox_layout.addWidget(self.replay_button)
        groupbox_layout.addWidget(self.exit_button)

        groupbox.setLayout(groupbox_layout)
        return groupbox

    def exit_button_clicked(self):
        self.close()

    def replay_button_clicked(self):
        if self.current_round_count < int(self.total_rounds):
            self.hide()
            self.current_round_count = self.current_round_count + 1
            self.parent.game_window.current_round_count = self.current_round_count
            self.parent.game_window.round_count_label.setText("Current round: " + str(self.current_round_count))
            self.parent.game_window.show()
        else:
            self.exit_button.setEnabled(True)
