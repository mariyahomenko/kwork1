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
        res = (sum(c))
        result = str(res)
        if '.' in result:
            a = result
            b = float(a)
            c = round(b, 8)
            ui.lineEdit_8.setText(str(c))
        elif '.' in result and result[-1] == '0':
            result = result[:-1]
            ui.lineEdit_8.setText(result)
        elif result[-1] == '.':
            result = result[:-1]
            ui.lineEdit_8.setText(result)
        else:
            ui.lineEdit_8.setText(result)
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
        res = (sum(c))
        result = str(res)
        if '.' in result:
            a = result
            b = float(a)
            c = round(b, 8)
            ui.lineEdit_14.setText(str(c))
        elif '.' in result and result[-1] == '0':
            result = result[:-1]
            ui.lineEdit_14.setText(result)
        elif result[-1] == '.':
            result = result[:-1]
            ui.lineEdit_14.setText(result)
        else:
            ui.lineEdit_14.setText(result)
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
        res = (sum(c))
        result = str(res)
        if '.' in result:
            a = result
            b = float(a)
            c = round(b, 8)
            ui.lineEdit_20.setText(str(c))
        elif '.' in result and result[-1] == '0':
            result = result[:-1]
            ui.lineEdit_20.setText(result)
        elif result[-1] == '.':
            result = result[:-1]
            ui.lineEdit_20.setText(result)
        else:
            ui.lineEdit_20.setText(result)
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
        res = (sum(c))
        result = str(res)
        if '.' in result:
            a = result
            b = float(a)
            c = round(b, 8)
            ui.lineEdit_27.setText(str(c))
        elif '.' in result and result[-1] == '0':
            result = result[:-1]
            ui.lineEdit_27.setText(result)
        elif result[-1] == '.':
            result = result[:-1]
            ui.lineEdit_27.setText(result)
        else:
            ui.lineEdit_27.setText(result)
    except:
        ui.lineEdit_27.setText('wrong')


def Prcnt1():
    if ui.lineEdit_4.text() == '0':
        s = ui.lineEdit_8.text()
        ui.lineEdit_6.setText(s)
    else:
        a = ui.lineEdit_8.text()
        b = ui.lineEdit_4.text()
        try:
            res = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
            result = str(res)
            if '.' in result:
                a = result
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_6.setText(str(c))
            elif '.' in result and result[-1] == '0':
                result = result[:-1]
                ui.lineEdit_6.setText(result)
            elif result[-1] == '.':
                result = result[:-1]
                ui.lineEdit_6.setText(result)
            else:
                ui.lineEdit_6.setText(result)
        except:
            ui.lineEdit_6.setText('wrong')
def Prcnt2():
    if ui.lineEdit_10.text() == '0':
        s = ui.lineEdit_14.text()
        ui.lineEdit_11.setText(s)
    else:
        a = ui.lineEdit_14.text()
        b = ui.lineEdit_10.text()
        try:
            res = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
            result = str(res)
            if '.' in result:
                a = result
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_11.setText(str(c))
            elif '.' in result and result[-1] == '0':
                result = result[:-1]
                ui.lineEdit_11.setText(result)
            elif result[-1] == '.':
                result = result[:-1]
                ui.lineEdit_11.setText(result)
            else:
                ui.lineEdit_11.setText(result)
        except:
            ui.lineEdit_11.setText('wrong')
def Prcnt3():
    if ui.lineEdit_16.text() == '0':
        s = ui.lineEdit_20.text()
        ui.lineEdit_17.setText(s)
    else:
        a = ui.lineEdit_20.text()
        b = ui.lineEdit_16.text()
        try:
            res = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
            result = str(res)
            if '.' in result:
                a = result
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_17.setText(str(c))
            elif '.' in result and result[-1] == '0':
                result = result[:-1]
                ui.lineEdit_17.setText(result)
            elif result[-1] == '.':
                result = result[:-1]
                ui.lineEdit_17.setText(result)
            else:
                ui.lineEdit_17.setText(result)
        except:
            ui.lineEdit_17.setText('wrong')
def Prcnt4():
    if ui.lineEdit_23.text() == '0':
        s = ui.lineEdit_27.text()
        ui.lineEdit_24.setText(s)
    else:
        a = ui.lineEdit_27.text()
        b = ui.lineEdit_23.text()
        try:
            res = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
            result = str(res)
            if '.' in result:
                a = result
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_24.setText(str(c))
            elif '.' in result and result[-1] == '0':
                result = result[:-1]
                ui.lineEdit_24.setText(result)
            elif result[-1] == '.':
                result = result[:-1]
                ui.lineEdit_24.setText(result)
            else:
                ui.lineEdit_24.setText(result)
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
            res1 = Decimal(value1) / Decimal(value)
            result1 = str(res1)
            if '.' in result1:
                a = result1
                b = float(a)
                c = round(b, 8)
                ui.lineEdit.setText(str(c))
            elif '.' in result1 and result1[-1] == '0':
                result1 = result1[:-1]
                ui.lineEdit.setText(result1)
            elif result1[-1] == '.':
                result1 = result1[:-1]
                ui.lineEdit.setText(result1)
            else:
                ui.lineEdit.setText(result1)
        else:
            ui.lineEdit.setText('')
    except:
        ui.lineEdit.setText('wrong')
    try:
        if value != '' and value2 != '':
            res2 = Decimal(value2) / Decimal(value)
            result2 = str(res2)
            if '.' in result2:
                a = result2
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_2.setText(str(c))
            elif '.' in result2 and result2[-1] == '0':
                result2 = result2[:-1]
                ui.lineEdit_2.setText(result2)
            elif result2[-1] == '.':
                result2 = result2[:-1]
                ui.lineEdit_2.setText(result2)
            else:
                ui.lineEdit_2.setText(result2)
        else:
            ui.lineEdit_2.setText('')
    except:
        ui.lineEdit_2.setText('wrong')
    try:
        if value != '' and value3 != '':
            res3 = Decimal(value3) / Decimal(value)
            result3 = str(res3)
            if '.' in result3:
                a = result3
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_3.setText(str(c))
            elif '.' in result3 and result3[-1] == '0':
                result3 = result3[:-1]
                ui.lineEdit_3.setText(result3)
            elif result3[-1] == '.':
                result3 = result3[:-1]
                ui.lineEdit_3.setText(result3)
            else:
                ui.lineEdit_3.setText(result3)
        else:
            ui.lineEdit_3.setText('')
    except:
        ui.lineEdit_3.setText('wrong')
    try:
        if value != '' and value4 != '':
            res4 = Decimal(value4) / Decimal(value)
            result4 = str(res4)
            if '.' in result4:
                a = result4
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_22.setText(str(c))
            elif '.' in result4 and result4[-1] == '0':
                result4 = result4[:-1]
                ui.lineEdit_22.setText(result4)
            elif result4[-1] == '.':
                result4 = result4[:-1]
                ui.lineEdit_22.setText(result4)
            else:
                ui.lineEdit_22.setText(result4)
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
            res1 = Decimal(value1) / Decimal(value)
            result1 = str(res1)
            if '.' in result1:
                a = result1
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_7.setText(str(c))
            elif '.' in result1 and result1[-1] == '0':
                result1 = result1[:-1]
                ui.lineEdit_7.setText(result1)
            elif result1[-1] == '.':
                result1 = result1[:-1]
                ui.lineEdit_7.setText(result1)
            else:
                ui.lineEdit_7.setText(result1)
        else:
            ui.lineEdit_7.setText('')
    except:
        ui.lineEdit_7.setText('wrong')
    try:
        if value != '' and value2 != '':
            res2 = Decimal(value2) / Decimal(value)
            result2 = str(res2)
            if '.' in result2:
                a = result2
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_15.setText(str(c))
            elif '.' in result2 and result2[-1] == '0':
                result2 = result2[:-1]
                ui.lineEdit_15.setText(result2)
            elif result2[-1] == '.':
                result2 = result2[:-1]
                ui.lineEdit_15.setText(result2)
            else:
                ui.lineEdit_15.setText(result2)
        else:
            ui.lineEdit_15.setText('')
    except:
        ui.lineEdit_15.setText('wrong')
    try:
        if value != '' and value3 != '':
            res3 = Decimal(value3) / Decimal(value)
            result3 = str(res3)
            if '.' in result3:
                a = result3
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_21.setText(str(c))
            elif '.' in result3 and result3[-1] == '0':
                result3 = result3[:-1]
                ui.lineEdit_21.setText(result3)
            elif result3[-1] == '.':
                result3 = result3[:-1]
                ui.lineEdit_21.setText(result3)
            else:
                ui.lineEdit_21.setText(result3)
        else:
            ui.lineEdit_21.setText('')
    except:
        ui.lineEdit_21.setText('wrong')
    try:
        if value != '' and value4 != '':
            res4 = Decimal(value4) / Decimal(value)
            result4 = str(res4)
            if '.' in result4:
                a = result4
                b = float(a)
                c = round(b, 8)
                ui.lineEdit_28.setText(str(c))
            elif '.' in result4 and result4[-1] == '0':
                result4 = result4[:-1]
                ui.lineEdit_28.setText(result4)
            elif result4[-1] == '.':
                result4 = result4[:-1]
                ui.lineEdit_28.setText(result4)
            else:
                ui.lineEdit_28.setText(result4)
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
    ui.tableWidget.setRowCount(20)
def Cleartable2():
    ui.tableWidget_2.clearContents()
    ui.lineEdit_14.clear()
    ui.lineEdit_11.clear()
    ui.lineEdit_15.clear()
    ui.lineEdit_2.clear()
    ui.tableWidget_2.setRowCount(20)
def Cleartable3():
    ui.tableWidget_3.clearContents()
    ui.lineEdit_20.clear()
    ui.lineEdit_17.clear()
    ui.lineEdit_21.clear()
    ui.lineEdit_3.clear()
    ui.tableWidget_3.setRowCount(20)
def Cleartable4():
    ui.tableWidget_4.clearContents()
    ui.lineEdit_27.clear()
    ui.lineEdit_24.clear()
    ui.lineEdit_28.clear()
    ui.lineEdit_22.clear()
    ui.tableWidget_4.setRowCount(20)

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

ui.lineEdit_9.textChanged.connect(lambda: Tether())
ui.lineEdit_5.textChanged.connect(lambda: Btc())

ui.pushButton_8.clicked.connect(lambda: Tether())
ui.pushButton_3.clicked.connect(lambda: Btc())

ui.lineEdit_4.textChanged.connect(lambda: Prcnt1())
ui.lineEdit_10.textChanged.connect(lambda: Prcnt2())
ui.lineEdit_16.textChanged.connect(lambda: Prcnt3())
ui.lineEdit_23.textChanged.connect(lambda: Prcnt4())

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