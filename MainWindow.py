import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from StartWindow import StartWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start_window = StartWindow(self)
        self.game_window = None

        self.resize(800, 600)
        self.setStyleSheet("background-color : white")
        self.setCentralWidget(self.start_window)


app = QApplication(sys.argv)
app.setStyle('Fusion')
win = MainWindow()
win.show()
sys.exit(app.exec_())
