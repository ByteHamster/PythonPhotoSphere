#!/usr/bin/python
import os
import sys

from renderer import Window


fileUrl = ""


def main():
    Window(640, 480).open(fileUrl)


def qtmain():
    from PyQt5 import QtGui, QtCore, QtWidgets
    class Example(QtWidgets.QWidget):

        def __init__(self):
            super(Example, self).__init__()
            self.setWindowFlags(QtCore.Qt.Dialog)

            self.initUI()

        def initUI(self):

            self.btn = QtWidgets.QPushButton('OK', self)
            self.btn.move(20, 20)
            self.btn.clicked.connect(self.showDialog)

            self.le = QtWidgets.QLineEdit(self)
            self.le.move(130, 22)

            self.fdBtn = QtWidgets.QPushButton('Choose', self)
            self.fdBtn.move(280, 20)
            self.fdBtn.clicked.connect(self.chooseFile)

            self.setGeometry(100, 100, 390, 60)
            self.setWindowTitle('Input dialog')
            self.show()

        def chooseFile(self):
            sFileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "","Files (*.*)" )
            if not sFileName: return
            self.le.setText("file:///"+sFileName)
            self.showDialog()

        def showDialog(self):
            global fileUrl
            text = (str(self.le.text()))
            fileUrl = text
            QtCore.QCoreApplication.instance().quit()

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ret = app.exec_()
    return ret




if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            fileUrl = "file://{0}".format(os.path.abspath(sys.argv[1]))
        elif sys.argv[1].startswith("file:///"):
            fileUrl = sys.argv[1]
        else:
            ret = qtmain()
        main()
        ret = 0
    else:
        ret = qtmain()
        # Your code that must run when the application closes goes here
        main()
    sys.exit(ret)
