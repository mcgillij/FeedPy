#!/usr/bin/python

from PyQt4 import QtGui, QtCore
import sys
from pprint import pprint

# Import the interface class
import untitled

class TestWindow(QtGui.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)
        self.setupUi(self)
        # Pass this "self" for building widgets and
        # keeping a reference.
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionOpen.triggered.connect(self.openStuff)
        self.actionClose.triggered.connect(self.closeStuff)
        
    def closeStuff(self):
        pprint(dir(self.listWidget))
        list2 = ["hi", "how", "are"]
        self.listWidget.addItems(list2)

    def openStuff(self):
        print "Hi"
        
    def main(self):
        self.show()

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    tw = TestWindow()
    tw.main()
    app.exec_()
    # This shows the interface we just created. No logic has been added, yet.