from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from ui import Ui_Dialog
from decimal import Decimal
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
app.setWindowIcon(QtGui.QIcon('icon.ico'))
window = QtWidgets.QWidget()
window.setWindowIcon(QtGui.QIcon('icon.ico'))

Dialog.show()

def Addrow1():
    rowCount = ui.tableWidget.rowCount()
    ui.tableWidget.insertRow(rowCount)
def Addrow2():
    rowCount = ui.tableWidget_2.rowCount()
    ui.tableWidget_2.insertRow(rowCount)
def Addrow3():
    rowCount = ui.tableWidget_3.rowCount()
    ui.tableWidget_3.insertRow(rowCount)
def Addrow4():
    rowCount = ui.tableWidget_4.rowCount()
    ui.tableWidget_4.insertRow(rowCount)


#def Removerow():
#    if ui.tableWidget.rowCount() > 0:
#        ui.tableWidget.removeRow(ui.tableWidget.rowCount()-1)



def Summ1():
    rows = ui.tableWidget.rowCount()
    cols = ui.tableWidget.columnCount()
    data = []
    for row in range(rows):
        tmp = []
        for col in range(cols):
            try:
                tmp.append(ui.tableWidget.item(row, col).text())
            except:
                tmp.append('0')
        data.append(tmp)
    try:
        a = (sum(data, []))
        a[0] = '0'
        c = [Decimal(item) for item in a]
        result = (sum(c))
        ui.lineEdit_8.setText(str(result))
    except:
        ui.lineEdit_8.setText('wrong')
def Summ2():
    rows = ui.tableWidget_2.rowCount()
    cols = ui.tableWidget_2.columnCount()
    data = []
    for row in range(rows):
        tmp = []
        for col in range(cols):
            try:
                tmp.append(ui.tableWidget_2.item(row, col).text())
            except:
                tmp.append('0')
        data.append(tmp)
    try:
        a = (sum(data, []))
        a[0] = '0'
        c = [Decimal(item) for item in a]
        result = (sum(c))
        ui.lineEdit_14.setText(str(result))
    except:
        ui.lineEdit_14.setText('wrong')
def Summ3():
    rows = ui.tableWidget_3.rowCount()
    cols = ui.tableWidget_3.columnCount()
    data = []
    for row in range(rows):
        tmp = []
        for col in range(cols):
            try:
                tmp.append(ui.tableWidget_3.item(row, col).text())
            except:
                tmp.append('0')
        data.append(tmp)
    try:
        a = (sum(data, []))
        a[0] = '0'
        c = [Decimal(item) for item in a]
        result = (sum(c))
        ui.lineEdit_20.setText(str(result))
    except:
        ui.lineEdit_20.setText('wrong')
def Summ4():
    rows = ui.tableWidget_4.rowCount()
    cols = ui.tableWidget_4.columnCount()
    data = []
    for row in range(rows):
        tmp = []
        for col in range(cols):
            try:
                tmp.append(ui.tableWidget_4.item(row, col).text())
            except:
                tmp.append('0')
        data.append(tmp)
    try:
        a = (sum(data, []))
        a[0] = '0'
        c = [Decimal(item) for item in a]
        result = (sum(c))
        ui.lineEdit_27.setText(str(result))
    except:
        ui.lineEdit_27.setText('wrong')


def Prcnt1():
    a = ui.lineEdit_8.text()
    b = ui.lineEdit_4.text()
    try:
        fin = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
        ui.lineEdit_6.setText(str(fin))
    except:
        ui.lineEdit_6.setText('wrong')
def Prcnt2():
    a = ui.lineEdit_14.text()
    b = ui.lineEdit_10.text()
    try:
        fin = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
        ui.lineEdit_11.setText(str(fin))
    except:
        ui.lineEdit_11.setText('wrong')
def Prcnt3():
    a = ui.lineEdit_20.text()
    b = ui.lineEdit_16.text()
    try:
        fin = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
        ui.lineEdit_17.setText(str(fin))
    except:
        ui.lineEdit_17.setText('wrong')
def Prcnt4():
    a = ui.lineEdit_27.text()
    b = ui.lineEdit_23.text()
    try:
        fin = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
        ui.lineEdit_24.setText(str(fin))
    except:
        ui.lineEdit_24.setText('wrong')


def Tether():
    value = ui.lineEdit_9.text()
    value1 = ui.lineEdit_6.text()
    value2 = ui.lineEdit_11.text()
    value3 = ui.lineEdit_17.text()
    value4 = ui.lineEdit_24.text()
    try:
        if value != '' and value1 != '':
            tthr1 = Decimal(value1) / Decimal(value)
            ui.lineEdit.setText(str(tthr1))
        else:
            ui.lineEdit.setText('')
    except:
        ui.lineEdit.setText('wrong')
    try:
        if value != '' and value2 != '':
            tthr2 = Decimal(value2) / Decimal(value)
            ui.lineEdit_2.setText(str(tthr2))
        else:
            ui.lineEdit_2.setText('')
    except:
        ui.lineEdit_2.setText('wrong')
    try:
        if value != '' and value3 != '':
            tthr3 = Decimal(value3) / Decimal(value)
            ui.lineEdit_3.setText(str(tthr3))
        else:
            ui.lineEdit_3.setText('')
    except:
        ui.lineEdit_3.setText('wrong')
    try:
        if value != '' and value4 != '':
            tthr4 = Decimal(value4) / Decimal(value)
            ui.lineEdit_22.setText(str(tthr4))
        else:
            ui.lineEdit_22.setText('')
    except:
        ui.lineEdit_22.setText('wrong')


def Btc():
    value = ui.lineEdit_5.text()
    value1 = ui.lineEdit_6.text()
    value2 = ui.lineEdit_11.text()
    value3 = ui.lineEdit_17.text()
    value4 = ui.lineEdit_24.text()
    try:
        if value != '' and value1 != '':
            tthr1 = Decimal(value1) / Decimal(value)
            ui.lineEdit_7.setText(str(tthr1))
        else:
            ui.lineEdit_7.setText('')
    except:
        ui.lineEdit_7.setText('wrong')
    try:
        if value != '' and value2 != '':
            tthr2 = Decimal(value2) / Decimal(value)
            ui.lineEdit_15.setText(str(tthr2))
        else:
            ui.lineEdit_15.setText('')
    except:
        ui.lineEdit_15.setText('wrong')
    try:
        if value != '' and value3 != '':
            tthr3 = Decimal(value3) / Decimal(value)
            ui.lineEdit_21.setText(str(tthr3))
        else:
            ui.lineEdit_21.setText('')
    except:
        ui.lineEdit_21.setText('wrong')
    try:
        if value != '' and value4 != '':
            tthr4 = Decimal(value4) / Decimal(value)
            ui.lineEdit_28.setText(str(tthr4))
        else:
            ui.lineEdit_28.setText('')
    except:
        ui.lineEdit_28.setText('wrong')


def Copy(num):
    cb = QApplication.clipboard()
    cb.clear(mode=cb.Clipboard)
    cb.setText(num, mode=cb.Clipboard)


def Cleartable1():
    ui.tableWidget.clearContents()
    ui.lineEdit_8.clear()
    ui.lineEdit_6.clear()
    ui.lineEdit_7.clear()
    ui.lineEdit.clear()
def Cleartable2():
    ui.tableWidget_2.clearContents()
    ui.lineEdit_14.clear()
    ui.lineEdit_11.clear()
    ui.lineEdit_15.clear()
    ui.lineEdit_2.clear()
def Cleartable3():
    ui.tableWidget_3.clearContents()
    ui.lineEdit_20.clear()
    ui.lineEdit_17.clear()
    ui.lineEdit_21.clear()
    ui.lineEdit_3.clear()
def Cleartable4():
    ui.tableWidget_4.clearContents()
    ui.lineEdit_27.clear()
    ui.lineEdit_24.clear()
    ui.lineEdit_28.clear()
    ui.lineEdit_22.clear()

def Clearall():
    ui.tableWidget.clearContents()
    ui.tableWidget_2.clearContents()
    ui.tableWidget_3.clearContents()
    ui.tableWidget_4.clearContents()

    ui.lineEdit_8.clear()
    ui.lineEdit_14.clear()
    ui.lineEdit_20.clear()
    ui.lineEdit_27.clear()

    ui.lineEdit_4.clear()
    ui.lineEdit_10.clear()
    ui.lineEdit_16.clear()
    ui.lineEdit_23.clear()

    ui.lineEdit_6.clear()
    ui.lineEdit_11.clear()
    ui.lineEdit_17.clear()
    ui.lineEdit_24.clear()

    ui.lineEdit_5.clear()
    ui.lineEdit_9.clear()

    ui.lineEdit_7.clear()
    ui.lineEdit_15.clear()
    ui.lineEdit_21.clear()
    ui.lineEdit_28.clear()

    ui.lineEdit.clear()
    ui.lineEdit_2.clear()
    ui.lineEdit_3.clear()
    ui.lineEdit_22.clear()

    ui.tableWidget.setRowCount(20)
    ui.tableWidget_2.setRowCount(20)
    ui.tableWidget_3.setRowCount(20)
    ui.tableWidget_4.setRowCount(20)

ui.tableWidget.cellChanged.connect(lambda: Addrow1())
ui.tableWidget_2.cellChanged.connect(lambda: Addrow2())
ui.tableWidget_3.cellChanged.connect(lambda: Addrow3())
ui.tableWidget_4.cellChanged.connect(lambda: Addrow4())

ui.tableWidget.cellChanged.connect(lambda: Summ1())
ui.tableWidget_2.cellChanged.connect(lambda: Summ2())
ui.tableWidget_3.cellChanged.connect(lambda: Summ3())
ui.tableWidget_4.cellChanged.connect(lambda: Summ4())

ui.pushButton_8.clicked.connect(lambda: Tether())
ui.pushButton_3.clicked.connect(lambda: Btc())

ui.pushButton.clicked.connect(lambda: Prcnt1())
ui.pushButton_2.clicked.connect(lambda: Prcnt2())
ui.pushButton_17.clicked.connect(lambda: Prcnt3())
ui.pushButton_22.clicked.connect(lambda: Prcnt4())

ui.pushButton_5.clicked.connect(lambda: Copy(ui.lineEdit_6.text()))
ui.pushButton_12.clicked.connect(lambda: Copy(ui.lineEdit_11.text()))
ui.pushButton_18.clicked.connect(lambda: Copy(ui.lineEdit_17.text()))
ui.pushButton_23.clicked.connect(lambda: Copy(ui.lineEdit_24.text()))
ui.pushButton_6.clicked.connect(lambda: Copy(ui.lineEdit_7.text()))
ui.pushButton_10.clicked.connect(lambda: Copy(ui.lineEdit_15.text()))
ui.pushButton_15.clicked.connect(lambda: Copy(ui.lineEdit_21.text()))
ui.pushButton_20.clicked.connect(lambda: Copy(ui.lineEdit_28.text()))
ui.pushButton_4.clicked.connect(lambda: Copy(ui.lineEdit.text()))
ui.pushButton_9.clicked.connect(lambda: Copy(ui.lineEdit_2.text()))
ui.pushButton_14.clicked.connect(lambda: Copy(ui.lineEdit_3.text()))
ui.pushButton_7.clicked.connect(lambda: Copy(ui.lineEdit_22.text()))

ui.pushButton_28.clicked.connect(lambda: Cleartable1())
ui.pushButton_27.clicked.connect(lambda: Cleartable2())
ui.pushButton_25.clicked.connect(lambda: Cleartable3())
ui.pushButton_26.clicked.connect(lambda: Cleartable4())

ui.pushButton_11.clicked.connect(lambda: Clearall())

sys.exit(app.exec_())