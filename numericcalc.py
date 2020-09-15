from PyQt5 import QtWidgets
from numcalculator import Ui_NumCalc
from polynomialdata import Ui_PolynomialRegressionAnalysis
from lineardata import Ui_LinearRegressionAnalysis


class Numerical_Window(QtWidgets.QMainWindow, Ui_NumCalc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton.clicked.connect(self.open_window1)
        self.pushButton_2.clicked.connect(self.open_window2)

    def open_window1(self):
        self.window = QtWidgets.QMainWindow(self)
        self.ui = Ui_LinearRegressionAnalysis()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_window2(self):
        self.window = QtWidgets.QMainWindow(self)
        self.ui = Ui_PolynomialRegressionAnalysis()
        self.ui.setupUi(self.window)
        self.window.show()
