import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPushButton
app = QtGui.QApplication(sys.argv)
win = QtGui.QMainWindow()
win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
button = QPushButton("Hello World!")
button.show()
#win.show()
sys.exit(app.exec_())
#win.show()