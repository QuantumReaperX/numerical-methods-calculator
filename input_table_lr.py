
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractItemModel
from linearoutput import Ui_LinearRegressionResult

class Ui_InputDataLR(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 300)
        
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 91, 780, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        #change the column count to dynamic set by user on generate button from lineardata,py
        # self.tableWidget.setColumnCount(20)
        
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
       
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 220, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton { background-color: rgb(150, 180, 10)}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 30, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.calculate_button)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Linear Data Input"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "x"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "f(x)"))
        self.pushButton.setText(_translate("Form", "Calculate"))
        self.label.setText(_translate("Form", "Enter the set of data in the table"))


    def calculate_button(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LinearRegressionResult()
        self.ui.setupUi(self.window)
        model = self.tableWidget.model()  # type: QAbstractItemModel
        data = []
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                # We suppose data are strings
                data[row].append(model.data(index))

        self.ui.populate(data)
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_InputDataLR()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
