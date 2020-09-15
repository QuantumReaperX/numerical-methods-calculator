from PyQt5 import QtCore, QtGui, QtWidgets
from polynomialR import Ui_PolynomialResult
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt 

class Ui_PolynomialRegressionResult(object):
    def setupUi(self, PolynomialRegressionResult):
        PolynomialRegressionResult.setObjectName("PolynomialRegressionResult")
        PolynomialRegressionResult.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        PolynomialRegressionResult.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PolynomialRegressionResult)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 90, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton { background-color: rgb(191, 10, 10); color: rgb(250, 250, 250)}")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setMidLineWidth(0)
        self.label.setObjectName("label")
        self.label.setStyleSheet(" QLabel {color:red }")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 140, 791, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
 
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 530, 241, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton { background-color: rgb(191, 10, 10); color: rgb(250, 250, 250)}")

        PolynomialRegressionResult.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PolynomialRegressionResult)
        self.statusbar.setObjectName("statusbar")
        PolynomialRegressionResult.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(PolynomialRegressionResult)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        PolynomialRegressionResult.setMenuBar(self.menubar)
        self.actionFull_Screen = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionMinimize = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionMaximize = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionNew = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionNew.setShortcutVisibleInContextMenu(False)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreferences = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionMenu = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionMenu.setObjectName("actionMenu")
        self.actionUndo = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo_2 = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionUndo_2.setObjectName("actionUndo_2")
        self.actionRedo_2 = QtWidgets.QAction(PolynomialRegressionResult)
        self.actionRedo_2.setObjectName("actionRedo_2")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo_2)
        self.menuEdit.addAction(self.actionRedo_2)
        self.menuView.addAction(self.actionMenu)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuWindow.addAction(self.actionFull_Screen)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionMaximize)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PolynomialRegressionResult)
        QtCore.QMetaObject.connectSlotsByName(PolynomialRegressionResult)

        self.pushButton.clicked.connect(self.switch_to_pr2)
        self.pushButton_2.clicked.connect(self.poly_graph)

    def retranslateUi(self, PolynomialRegressionResult):
        _translate = QtCore.QCoreApplication.translate
        PolynomialRegressionResult.setWindowTitle(_translate("PolynomialRegressionResult", "MainWindow"))
        self.pushButton.setText(_translate("PolynomialRegressionResult", "Show the General Equation"))
        self.label.setText(_translate("PolynomialRegressionResult", "Polynomial Regression Analysis"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PolynomialRegressionResult", "x1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PolynomialRegressionResult", "y1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PolynomialRegressionResult", "x1^2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PolynomialRegressionResult", "x1^3"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PolynomialRegressionResult", "x1^4"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("PolynomialRegressionResult", "x1y1"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("PolynomialRegressionResult", "x1^2y1"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("PolynomialRegressionResult", "ym"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("PolynomialRegressionResult", "ei"))
        self.pushButton_2.setText(_translate("PolynomialRegressionResult", "Polynomial Regression Analysis Graph"))
        self.menuFile.setTitle(_translate("PolynomialRegressionResult", "File"))
        self.menuEdit.setTitle(_translate("PolynomialRegressionResult", "Edit"))
        self.menuView.setTitle(_translate("PolynomialRegressionResult", "View"))
        self.menuSettings.setTitle(_translate("PolynomialRegressionResult", "Settings"))
        self.menuWindow.setTitle(_translate("PolynomialRegressionResult", "Window "))
        self.menuHelp.setTitle(_translate("PolynomialRegressionResult", "Help"))
        self.actionFull_Screen.setText(_translate("PolynomialRegressionResult", "Full Screen"))
        self.actionFull_Screen.setShortcut(_translate("PolynomialRegressionResult", "F11"))
        self.actionMinimize.setText(_translate("PolynomialRegressionResult", "Minimize"))
        self.actionMinimize.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+N"))
        self.actionMaximize.setText(_translate("PolynomialRegressionResult", "Maximize"))
        self.actionMaximize.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+M"))
        self.actionNew.setText(_translate("PolynomialRegressionResult", "New"))
        self.actionNew.setStatusTip(_translate("PolynomialRegressionResult", "Create a new file"))
        self.actionNew.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+N"))
        self.actionOpen.setText(_translate("PolynomialRegressionResult", "Open"))
        self.actionOpen.setStatusTip(_translate("PolynomialRegressionResult", "Open a file"))
        self.actionSave.setText(_translate("PolynomialRegressionResult", "Save"))
        self.actionSave.setStatusTip(_translate("PolynomialRegressionResult", "Save a file"))
        self.actionSave.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+S"))
        self.actionSave_As.setText(_translate("PolynomialRegressionResult", "Save As"))
        self.actionSave_As.setStatusTip(_translate("PolynomialRegressionResult", "Save as a new file"))
        self.actionClose.setText(_translate("PolynomialRegressionResult", "Close"))
        self.actionExit.setText(_translate("PolynomialRegressionResult", "Exit"))
        self.actionAbout.setText(_translate("PolynomialRegressionResult", "About"))
        self.actionAbout.setShortcut(_translate("PolynomialRegressionResult", "F12"))
        self.actionHelp.setText(_translate("PolynomialRegressionResult", "Help"))
        self.actionHelp.setShortcut(_translate("PolynomialRegressionResult", "F1"))
        self.actionPreferences.setText(_translate("PolynomialRegressionResult", "Preferences"))
        self.actionPreferences.setShortcut(_translate("PolynomialRegressionResult", "F10"))
        self.actionMenu.setText(_translate("PolynomialRegressionResult", "Menu"))
        self.actionMenu.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+M"))
        self.actionUndo.setText(_translate("PolynomialRegressionResult", "History"))
        self.actionUndo.setStatusTip(_translate("PolynomialRegressionResult", "Check History"))
        self.actionUndo.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+H"))
        self.actionRedo.setText(_translate("PolynomialRegressionResult", "Copy"))
        self.actionRedo.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+C"))
        self.actionCut.setText(_translate("PolynomialRegressionResult", "Cut"))
        self.actionCut.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+X"))
        self.actionPaste.setText(_translate("PolynomialRegressionResult", "Paste"))
        self.actionUndo_2.setText(_translate("PolynomialRegressionResult", "Undo"))
        self.actionUndo_2.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+Z"))
        self.actionRedo_2.setText(_translate("PolynomialRegressionResult", "Redo"))
        self.actionRedo_2.setShortcut(_translate("PolynomialRegressionResult", "Ctrl+R"))

    def populate(self, data):
        self.data = {}

        
        totals = [0, 0, 0, 0, 0, 0, 0]
        row_count = len(data[0])
        for row in range(row_count):
            self.tableWidget.insertRow(row)
            
            valuex = float(data[0][row])
            valuey = float(data[1][row])

            itemx = QtWidgets.QTableWidgetItem(str(valuex))
            self.tableWidget.setItem(row, 0, itemx)
            
            itemy = QtWidgets.QTableWidgetItem(str(valuey))
            self.tableWidget.setItem(row, 1, itemy)

            valuex2 = round(valuex ** 2, 4)
            itemx2 = QtWidgets.QTableWidgetItem(str(valuex2))
            self.tableWidget.setItem(row, 2, itemx2)

            valuex3 = round(valuex ** 3, 4)
            itemx3 = QtWidgets.QTableWidgetItem(str(valuex3))
            self.tableWidget.setItem(row, 3, itemx3)

            valuex4 = round(valuex ** 4, 4)
            itemx4 = QtWidgets.QTableWidgetItem(str(valuex4))
            self.tableWidget.setItem(row, 4, itemx4)

            valuexy = round(valuex * valuey, 4)
            itemxy = QtWidgets.QTableWidgetItem(str(valuexy))
            self.tableWidget.setItem(row, 5, itemxy)

            valuex2y = round((valuex ** 2) * valuey, 4)
            itemx2y = QtWidgets.QTableWidgetItem(str(valuex2y))
            self.tableWidget.setItem(row, 6, itemx2y)

            # array inputs for poly sklearn module to get coefficients
            x_array = data[0]
            x_array = list(map(float, x_array))
            self.data['x_array'] = x_array
            print(f'the x are: {x_array}') 
            y_array = data[1]
            y_array = list(map(float, y_array))
            self.data['y_array'] = y_array
            print(f'the y are: {y_array}')

            x = np.array(x_array).reshape((-1, 1))
            self.data['x'] = x
            y = np.array(y_array)
            self.data['y'] = y
            

            # transformer = PolynomialFeatures(degree=2, include_bias=False)
            # transformer.fit(x)
            # x_ = transformer.transform(x)
            x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
            print(x_)
            self.data['x_'] = x_

            modelx = LinearRegression().fit(x_, y)
            self.data['modelx'] = modelx
            r_sq = modelx.score(x_, y)
            self.data['r_sq'] = r_sq
            print('coefficient of determination', r_sq)
            a0 = round(r_sq, 4)
            self.data['a0'] = a0
            print('intercept:', modelx.intercept_)
            self.data['y_int'] = round(modelx.intercept_, 4)
            print('coefficients:', modelx.coef_)
            print(modelx.coef_[0])
            a1 = round(modelx.coef_[0], 4)
            self.data['a1'] = a1
            print(modelx.coef_[1])
            a2 = round(modelx.coef_[1], 4)
            self.data['a2'] = a2



            totals[0] += valuex
            self.data['totalx'] = totals[0]
            print(totals[0])
            totals[1] += valuey
            self.data['totaly'] = totals[1]
            print(totals[1])
            totals[2] += valuex2
            self.data['totalx2'] = totals[2]
            print(totals[2])
            totals[3] += valuex3
            self.data['totalx3'] = totals[3]
            print(totals[3])
            totals[4] += valuex4
            self.data['totalx4'] = totals[4]
            print(totals[4])
            totals[5] += valuexy
            self.data['totalxy'] = totals[5]
            print(totals[5])
            totals[6] += valuex2y
            self.data['totalx2y'] = totals[6]
            print(totals[6])

            print(f'the totals are: {totals}')

        for i in range(len(totals)):
            totals[i] = round(totals[i], 4)

        y_bar = round(totals[1] / row_count, 4)
        print(y_bar)
        self.data['y_bar'] = y_bar

        x_mean = round(totals[0]/row_count, 4)
        print(x_mean)
        self.data['x_mean'] = x_mean

        mean_x = round(totals[0] / row_count, 4)
        self.data['mean_x'] = mean_x
        print(f'the mean of x is {mean_x}')

        mean_y = round(totals[1] / row_count, 4)
        self.data['mean_y'] = mean_y
        print(f'the mean of y is {mean_y}')

        for row in range(row_count):
            valuex = float(data[0][row])
            valuey = float(data[1][row])


            valueym = f'{round(a0 + a1 * valuex + a2*(valuex **2), 4)}'
            itemym = QtWidgets.QTableWidgetItem(str(valueym))
            self.tableWidget.setItem(row, 7, itemym)

            value_ei = f'{round((valuey) - float(valueym), 4)}'
            itemei = QtWidgets.QTableWidgetItem(str(value_ei))
            self.tableWidget.setItem(row, 8, itemei)


    def switch_to_pr2(self, data):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PolynomialResult()
        self.ui.setupUi(self.window)
        self.ui.populate(self.data)
        self.ui.equation_changed()
        self.window.show()

    def poly_graph(self, data):
        x_array = self.data['x_array']
        y_array = self.data['y_array']
        
        x = self.data['x']
        y = self.data['y']
        
        poly = PolynomialFeatures(degree = 4) 
        X_poly = poly.fit_transform(x) 
        
        poly.fit(X_poly, y) 
        lin2 = LinearRegression() 
        lin2.fit(X_poly, y) 
       
        
        plt.scatter(x_array, y_array, color = 'blue') 
  
        plt.plot(x, lin2.predict(poly.fit_transform(x)), color = 'red') 
        plt.title('Polynomial Regression') 
        plt.xlabel('x') 
        plt.ylabel('f(x)') 
        plt.show() 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PolynomialRegressionResult = QtWidgets.QMainWindow()
    ui = Ui_PolynomialRegressionResult()
    ui.setupUi(PolynomialRegressionResult)
    PolynomialRegressionResult.show()
    sys.exit(app.exec_())
