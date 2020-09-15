import sys
from PyQt5.QtWidgets import QApplication
from numericcalc import Numerical_Window

app = QApplication(sys.argv)
# app.setStyle('Windows')
# app.setStyle('Oxygen')
# app.setStyle('Windows')
# app.setStyle('QtCurve')
# app.setStyle('Breeze')


num_calculator = Numerical_Window()

sys.exit(app.exec_())