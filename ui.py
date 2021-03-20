from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(612, 642)
        Dialog.setStyleSheet("QDialog {\n"
"background: #eff3ff;\n"
"}\n"
"\n"
"QPushButton {\n"
"background: #eeedc1;\n"
"border: 1.2px solid #7f3a19;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #e0d2b7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: #e8ecec;\n"
"}\n"
"\n"
"QTextEdit {\n"
"background: #a6b6ab;\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 570, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 390, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 370, 111, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 450, 111, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 370, 31, 21))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background: #ceeec2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #bcffbe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 470, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 550, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 450, 31, 21))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"background: #ceeec2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #bcffbe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 570, 31, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 410, 111, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 490, 111, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 410, 31, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 490, 31, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 141, 281))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 330, 141, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 530, 111, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 530, 31, 21))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"background: #ceeec2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #bcffbe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 570, 31, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 570, 111, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 370, 111, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(270, 490, 31, 21))
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(160, 410, 111, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(160, 10, 141, 281))
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 370, 31, 21))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background: #ceeec2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #bcffbe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_14 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(160, 330, 141, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(160, 470, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 390, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(160, 490, 111, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(270, 410, 31, 21))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(420, 570, 31, 21))
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 570, 111, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_16 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(310, 370, 111, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(420, 490, 31, 21))
        self.pushButton_15.setObjectName("pushButton_15")
        self.lineEdit_17 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(310, 410, 111, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.tableWidget_3 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_3.setGeometry(QtCore.QRect(310, 10, 141, 281))
        self.tableWidget_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(420, 370, 31, 21))
        self.pushButton_17.setStyleSheet("QPushButton {\n"
"background: #ceeec2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #bcffbe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit_20 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_20.setGeometry(QtCore.QRect(310, 330, 141, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(310, 470, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(310, 390, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_21 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_21.setGeometry(QtCore.QRect(310, 490, 111, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(420, 410, 31, 21))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 570, 31, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_22 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_22.setGeometry(QtCore.QRect(460, 570, 111, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_23.setGeometry(QtCore.QRect(460, 370, 111, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(570, 490, 31, 21))
        self.pushButton_20.setObjectName("pushButton_20")
        self.lineEdit_24 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_24.setGeometry(QtCore.QRect(460, 410, 111, 20))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.tableWidget_4 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_4.setGeometry(QtCore.QRect(460, 10, 141, 281))
        self.tableWidget_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.pushButton_22 = QtWidgets.QPushButton(Dialog)
        self.pushButton_22.setGeometry(QtCore.QRect(570, 370, 31, 21))
        self.pushButton_22.setStyleSheet("QPushButton {\n"
"background: #ceeec2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #bcffbe;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.lineEdit_27 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_27.setGeometry(QtCore.QRect(460, 330, 141, 20))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(460, 470, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(460, 390, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_28 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_28.setGeometry(QtCore.QRect(460, 490, 111, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.pushButton_23 = QtWidgets.QPushButton(Dialog)
        self.pushButton_23.setGeometry(QtCore.QRect(570, 410, 31, 21))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_26 = QtWidgets.QPushButton(Dialog)
        self.pushButton_26.setGeometry(QtCore.QRect(540, 300, 61, 20))
        self.pushButton_26.setStyleSheet("QPushButton {\n"
"background: #ffbba0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #ff817f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_25 = QtWidgets.QPushButton(Dialog)
        self.pushButton_25.setGeometry(QtCore.QRect(390, 300, 61, 20))
        self.pushButton_25.setStyleSheet("QPushButton {\n"
"background: #ffbba0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #ff817f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_27 = QtWidgets.QPushButton(Dialog)
        self.pushButton_27.setGeometry(QtCore.QRect(240, 300, 61, 20))
        self.pushButton_27.setStyleSheet("QPushButton {\n"
"background: #ffbba0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #ff817f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(Dialog)
        self.pushButton_28.setGeometry(QtCore.QRect(90, 300, 61, 20))
        self.pushButton_28.setStyleSheet("QPushButton {\n"
"background: #ffbba0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #ff817f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(160, 550, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(310, 550, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(460, 550, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(520, 610, 75, 23))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"background: #ffbba0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #ff817f;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #ffffff;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tarantino&Co Service Калькулятор"))
        self.label_3.setText(_translate("Dialog", "Выплата"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Введите процент"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Введите курс ВТС"))
        self.pushButton.setText(_translate("Dialog", "%"))
        self.label_5.setText(_translate("Dialog", "Выплата ВТС"))
        self.label_7.setText(_translate("Dialog", "Выплата Тезер"))
        self.pushButton_3.setText(_translate("Dialog", "ок"))
        self.pushButton_4.setText(_translate("Dialog", "⧉"))
        self.pushButton_5.setText(_translate("Dialog", "⧉"))
        self.pushButton_6.setText(_translate("Dialog", "⧉"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Имя"))
        self.lineEdit_8.setPlaceholderText(_translate("Dialog", "Сумма"))
        self.lineEdit_9.setPlaceholderText(_translate("Dialog", "Введите курс Тезер"))
        self.pushButton_8.setText(_translate("Dialog", "ок"))
        self.pushButton_9.setText(_translate("Dialog", "⧉"))
        self.lineEdit_10.setPlaceholderText(_translate("Dialog", "Введите процент"))
        self.pushButton_10.setText(_translate("Dialog", "⧉"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Имя"))
        self.pushButton_2.setText(_translate("Dialog", "%"))
        self.lineEdit_14.setPlaceholderText(_translate("Dialog", "Сумма"))
        self.label_6.setText(_translate("Dialog", "Выплата ВТС"))
        self.label_4.setText(_translate("Dialog", "Выплата"))
        self.pushButton_12.setText(_translate("Dialog", "⧉"))
        self.pushButton_14.setText(_translate("Dialog", "⧉"))
        self.lineEdit_16.setPlaceholderText(_translate("Dialog", "Введите процент"))
        self.pushButton_15.setText(_translate("Dialog", "⧉"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Имя"))
        self.pushButton_17.setText(_translate("Dialog", "%"))
        self.lineEdit_20.setPlaceholderText(_translate("Dialog", "Сумма"))
        self.label_13.setText(_translate("Dialog", "Выплата ВТС"))
        self.label_14.setText(_translate("Dialog", "Выплата"))
        self.pushButton_18.setText(_translate("Dialog", "⧉"))
        self.pushButton_7.setText(_translate("Dialog", "⧉"))
        self.lineEdit_23.setPlaceholderText(_translate("Dialog", "Введите процент"))
        self.pushButton_20.setText(_translate("Dialog", "⧉"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Имя"))
        self.pushButton_22.setText(_translate("Dialog", "%"))
        self.lineEdit_27.setPlaceholderText(_translate("Dialog", "Сумма"))
        self.label_17.setText(_translate("Dialog", "Выплата ВТС"))
        self.label_18.setText(_translate("Dialog", "Выплата"))
        self.pushButton_23.setText(_translate("Dialog", "⧉"))
        self.pushButton_26.setText(_translate("Dialog", "del"))
        self.pushButton_25.setText(_translate("Dialog", "del"))
        self.pushButton_27.setText(_translate("Dialog", "del"))
        self.pushButton_28.setText(_translate("Dialog", "del"))
        self.label_8.setText(_translate("Dialog", "Выплата Тезер"))
        self.label_9.setText(_translate("Dialog", "Выплата Тезер"))
        self.label_10.setText(_translate("Dialog", "Выплата Тезер"))
        self.pushButton_11.setText(_translate("Dialog", "C"))

