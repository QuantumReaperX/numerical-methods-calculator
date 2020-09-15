from PyQt5 import QtCore, QtGui, QtWidgets
from linearRI import Ui_LinearInterpolationCalculator
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt 


class Ui_LinearRegressionResult(object):
    def setupUi(self, LinearRegressionResult):
        LinearRegressionResult.setObjectName("LinearRegressionResult")
        LinearRegressionResult.resize(800, 600)
        LinearRegressionResult.setStyleSheet("QMainWindow {background-color: gray}")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        LinearRegressionResult.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LinearRegressionResult)
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
        self.label.setGeometry(QtCore.QRect(250, 50, 2000, 50))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(20)
        font.setBold(True)
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
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 530, 241, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton { background-color: rgb(191, 10, 10); color: rgb(250, 250, 250)}")
        LinearRegressionResult.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LinearRegressionResult)
        self.statusbar.setObjectName("statusbar")
        LinearRegressionResult.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(LinearRegressionResult)
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
        LinearRegressionResult.setMenuBar(self.menubar)
        self.actionFull_Screen = QtWidgets.QAction(LinearRegressionResult)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionMinimize = QtWidgets.QAction(LinearRegressionResult)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionMaximize = QtWidgets.QAction(LinearRegressionResult)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionNew = QtWidgets.QAction(LinearRegressionResult)
        self.actionNew.setShortcutVisibleInContextMenu(False)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(LinearRegressionResult)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(LinearRegressionResult)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(LinearRegressionResult)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(LinearRegressionResult)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(LinearRegressionResult)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(LinearRegressionResult)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(LinearRegressionResult)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreferences = QtWidgets.QAction(LinearRegressionResult)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionMenu = QtWidgets.QAction(LinearRegressionResult)
        self.actionMenu.setObjectName("actionMenu")
        self.actionUndo = QtWidgets.QAction(LinearRegressionResult)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(LinearRegressionResult)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(LinearRegressionResult)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(LinearRegressionResult)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo_2 = QtWidgets.QAction(LinearRegressionResult)
        self.actionUndo_2.setObjectName("actionUndo_2")
        self.actionRedo_2 = QtWidgets.QAction(LinearRegressionResult)
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

        self.retranslateUi(LinearRegressionResult)
        QtCore.QMetaObject.connectSlotsByName(LinearRegressionResult)

        self.pushButton.clicked.connect(self.switch_to_lr2)
        self.pushButton_2.clicked.connect(self.linear_graph)


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

            valuexy = round(valuex * valuey, 4)
            itemxy = QtWidgets.QTableWidgetItem(str(valuexy))
            self.tableWidget.setItem(row, 3, itemxy)

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
            # a2 = round(modelx.coef_[1], 4)
            # self.data['a2'] = a2


            totals[0] += valuex
            self.data['totalx'] = totals[0]
            print(totals[0])
            totals[1] += valuey
            self.data['totaly'] = totals[1]
            print(totals[1])
            totals[2] += valuex2
            self.data['totalx2'] = totals[2]
            print(totals[2])
            totals[3] += valuexy
            self.data['totalxy'] = totals[3]
            print(totals[3])
            # totals[4] += valueym
            # print(totals[4])
            # totals[5] += value_e12
            # print(totals[5])
            # totals[6] += value_y1_y
            # print(totals[6])
            print(f'the totals are: {totals}')
            
           


        for i in range(len(totals)):
            totals[i] = round(totals[i], 4)

        a0 = round((totals[1] * totals[2] - totals[0] * totals[3]) / (row_count * totals[2] - totals[0] ** 2), 4)
        print(f'The value of a0 is {a0}')
        self.data['a0'] = a0

        a1 = round((row_count * totals[3] - totals[0] * totals[1]) / (row_count * totals[2] - totals[0] ** 2), 4)
        print(f'The value of a1 is {a1}')
        self.data['a1'] = a1

        mean_x = round(totals[0] / row_count, 4)
        self.data['mean_x'] = mean_x

        mean_y = round(totals[1] / row_count, 4)
        self.data['mean_y'] = mean_y

        y_bar = round(totals[1] / row_count, 4)
        print(y_bar)
        self.data['y_bar'] = y_bar


        for row in range(row_count):
            valuex = float(data[0][row])
            valuey = float(data[1][row])


            valueym = f'{round(a0 + a1 * valuex, 4)}'
            itemym = QtWidgets.QTableWidgetItem(str(valueym))
            self.tableWidget.setItem(row, 4, itemym)

            value_e12 = f'{round((float(valueym) - valuey) ** 2, 4)}'
            iteme12 = QtWidgets.QTableWidgetItem(str(value_e12))
            self.tableWidget.setItem(row, 5, iteme12)

            value_y1_y = f'{round((float(valuey) - float(y_bar)), 4)}'
            itemy1_y = QtWidgets.QTableWidgetItem(str(value_y1_y))
            self.tableWidget.setItem(row, 6, itemy1_y)




    def retranslateUi(self, LinearRegressionResult):
        _translate = QtCore.QCoreApplication.translate
        LinearRegressionResult.setWindowTitle(_translate("LinearRegressionResult", "MainWindow"))
        self.pushButton.setText(_translate("LinearRegressionResult", "Show the General Equation"))
        self.label.setText(_translate("LinearRegressionResult", "Linear Regression Analysis"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LinearRegressionResult", "x1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LinearRegressionResult", "y1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("LinearRegressionResult", "x1^2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("LinearRegressionResult", "x1y1"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("LinearRegressionResult", "ym"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("LinearRegressionResult", "e1^2"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("LinearRegressionResult", "y1-y"))
        self.pushButton_2.setText(_translate("LinearRegressionResult", "Linear Regression Analysis Graph"))
        self.menuFile.setTitle(_translate("LinearRegressionResult", "File"))
        self.menuEdit.setTitle(_translate("LinearRegressionResult", "Edit"))
        self.menuView.setTitle(_translate("LinearRegressionResult", "View"))
        self.menuSettings.setTitle(_translate("LinearRegressionResult", "Settings"))
        self.menuWindow.setTitle(_translate("LinearRegressionResult", "Window "))
        self.menuHelp.setTitle(_translate("LinearRegressionResult", "Help"))
        self.actionFull_Screen.setText(_translate("LinearRegressionResult", "Full Screen"))
        self.actionFull_Screen.setShortcut(_translate("LinearRegressionResult", "F11"))
        self.actionMinimize.setText(_translate("LinearRegressionResult", "Minimize"))
        self.actionMinimize.setShortcut(_translate("LinearRegressionResult", "Ctrl+N"))
        self.actionMaximize.setText(_translate("LinearRegressionResult", "Maximize"))
        self.actionMaximize.setShortcut(_translate("LinearRegressionResult", "Ctrl+M"))
        self.actionNew.setText(_translate("LinearRegressionResult", "New"))
        self.actionNew.setStatusTip(_translate("LinearRegressionResult", "Create a new file"))
        self.actionNew.setShortcut(_translate("LinearRegressionResult", "Ctrl+N"))
        self.actionOpen.setText(_translate("LinearRegressionResult", "Open"))
        self.actionOpen.setStatusTip(_translate("LinearRegressionResult", "Open a file"))
        self.actionSave.setText(_translate("LinearRegressionResult", "Save"))
        self.actionSave.setStatusTip(_translate("LinearRegressionResult", "Save a file"))
        self.actionSave.setShortcut(_translate("LinearRegressionResult", "Ctrl+S"))
        self.actionSave_As.setText(_translate("LinearRegressionResult", "Save As"))
        self.actionSave_As.setStatusTip(_translate("LinearRegressionResult", "Save as a new file"))
        self.actionClose.setText(_translate("LinearRegressionResult", "Close"))
        self.actionExit.setText(_translate("LinearRegressionResult", "Exit"))
        self.actionAbout.setText(_translate("LinearRegressionResult", "About"))
        self.actionAbout.setShortcut(_translate("LinearRegressionResult", "F12"))
        self.actionHelp.setText(_translate("LinearRegressionResult", "Help"))
        self.actionHelp.setShortcut(_translate("LinearRegressionResult", "F1"))
        self.actionPreferences.setText(_translate("LinearRegressionResult", "Preferences"))
        self.actionPreferences.setShortcut(_translate("LinearRegressionResult", "F10"))
        self.actionMenu.setText(_translate("LinearRegressionResult", "Menu"))
        self.actionMenu.setShortcut(_translate("LinearRegressionResult", "Ctrl+M"))
        self.actionUndo.setText(_translate("LinearRegressionResult", "History"))
        self.actionUndo.setStatusTip(_translate("LinearRegressionResult", "Check History"))
        self.actionUndo.setShortcut(_translate("LinearRegressionResult", "Ctrl+H"))
        self.actionRedo.setText(_translate("LinearRegressionResult", "Copy"))
        self.actionRedo.setShortcut(_translate("LinearRegressionResult", "Ctrl+C"))
        self.actionCut.setText(_translate("LinearRegressionResult", "Cut"))
        self.actionCut.setShortcut(_translate("LinearRegressionResult", "Ctrl+X"))
        self.actionPaste.setText(_translate("LinearRegressionResult", "Paste"))
        self.actionUndo_2.setText(_translate("LinearRegressionResult", "Undo"))
        self.actionUndo_2.setShortcut(_translate("LinearRegressionResult", "Ctrl+Z"))
        self.actionRedo_2.setText(_translate("LinearRegressionResult", "Redo"))
        self.actionRedo_2.setShortcut(_translate("LinearRegressionResult", "Ctrl+R"))

    def switch_to_lr2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LinearInterpolationCalculator()
        self.ui.setupUi(self.window)
        self.ui.populate(self.data)
        self.ui.equation_changed()
        self.window.show()

    
    def linear_graph(self, data):
        lin = LinearRegression() 
  

        x_array = self.data['x_array']
        y_array = self.data['y_array']

        x = self.data['x']
        y = self.data['y']

        lin.fit(x, y)
       
        
        plt.scatter(x_array, y_array, color = 'blue') 
  
        plt.plot(x, lin.predict(x), color = 'red') 
        plt.title('Linear Regression') 
        plt.xlabel('x') 
        plt.ylabel('f(x)') 
        plt.show() 


    

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LinearRegressionResult = QtWidgets.QMainWindow()
    ui = Ui_LinearRegressionResult()
    ui.setupUi(LinearRegressionResult)
    LinearRegressionResult.show()
    sys.exit(app.exec_())
