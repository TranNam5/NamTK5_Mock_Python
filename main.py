from PyQt5 import QtWidgets
from hospital import UiHospitalWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = UiHospitalWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
