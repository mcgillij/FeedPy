# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diag.ui'
#
# Created: Sun Jun 10 04:00:29 2012
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
        Dialog.resize(537, 300)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidgetUrls = QtGui.QListWidget(Dialog)
        self.listWidgetUrls.setObjectName(_fromUtf8("listWidgetUrls"))
        self.gridLayout.addWidget(self.listWidgetUrls, 2, 0, 1, 2)
        self.pushAddButton = QtGui.QPushButton(Dialog)
        self.pushAddButton.setObjectName(_fromUtf8("pushAddButton"))
        self.gridLayout.addWidget(self.pushAddButton, 1, 2, 1, 1)
        self.lineEditUrl = QtGui.QLineEdit(Dialog)
        self.lineEditUrl.setObjectName(_fromUtf8("lineEditUrl"))
        self.gridLayout.addWidget(self.lineEditUrl, 1, 0, 1, 2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEditRefresh = QtGui.QLineEdit(Dialog)
        self.lineEditRefresh.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEditRefresh.setObjectName(_fromUtf8("lineEditRefresh"))
        self.gridLayout.addWidget(self.lineEditRefresh, 4, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAddButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "RSS url to add to monitoring:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Click item to remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Refresh (Minutes): ", None, QtGui.QApplication.UnicodeUTF8))

