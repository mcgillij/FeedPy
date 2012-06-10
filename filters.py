# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filters.ui'
#
# Created: Sat Jun 09 22:01:44 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(348, 300)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.lineEditFilter = QtGui.QLineEdit(Dialog)
        self.lineEditFilter.setObjectName(_fromUtf8("lineEditFilter"))
        self.gridLayout.addWidget(self.lineEditFilter, 0, 1, 1, 1)
        self.pushButtonPlus = QtGui.QPushButton(Dialog)
        self.pushButtonPlus.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButtonPlus.setObjectName(_fromUtf8("pushButtonPlus"))
        self.gridLayout.addWidget(self.pushButtonPlus, 0, 2, 1, 1)
        self.pushButtonMinus = QtGui.QPushButton(Dialog)
        self.pushButtonMinus.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButtonMinus.setObjectName(_fromUtf8("pushButtonMinus"))
        self.gridLayout.addWidget(self.pushButtonMinus, 0, 3, 1, 1)
        self.listWidgetFilter = QtGui.QListWidget(Dialog)
        self.listWidgetFilter.setObjectName(_fromUtf8("listWidgetFilter"))
        self.gridLayout.addWidget(self.listWidgetFilter, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPlus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonMinus.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))

