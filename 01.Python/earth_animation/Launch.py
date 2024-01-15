import sys
from PySide6 import QtWidgets
from app import MainPresenter


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainPresenter()
    main.main_window.show()
    sys.exit(app.exec())
