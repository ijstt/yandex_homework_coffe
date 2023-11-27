from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    pass


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
