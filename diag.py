# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diag.ui'
#
# Created: Thu Jun 14 22:20:09 2012
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
        Dialog.resize(537, 376)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.listWidgetUrls = QtGui.QListWidget(Dialog)
        self.listWidgetUrls.setObjectName(_fromUtf8("listWidgetUrls"))
        self.gridLayout.addWidget(self.listWidgetUrls, 2, 0, 1, 2)
        self.pushAddButton = QtGui.QPushButton(Dialog)
        self.pushAddButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushAddButton.setObjectName(_fromUtf8("pushAddButton"))
        self.gridLayout.addWidget(self.pushAddButton, 1, 3, 1, 1)
        self.lineEditUrl = QtGui.QLineEdit(Dialog)
        self.lineEditUrl.setObjectName(_fromUtf8("lineEditUrl"))
        self.gridLayout.addWidget(self.lineEditUrl, 1, 0, 1, 2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(100, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEditRefresh = QtGui.QLineEdit(Dialog)
        self.lineEditRefresh.setMaximumSize(QtCore.QSize(25, 16777215))
        self.lineEditRefresh.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEditRefresh.setObjectName(_fromUtf8("lineEditRefresh"))
        self.gridLayout.addWidget(self.lineEditRefresh, 4, 1, 1, 1)
        self.lineEditAlertAt = QtGui.QLineEdit(Dialog)
        self.lineEditAlertAt.setMaximumSize(QtCore.QSize(25, 16777215))
        self.lineEditAlertAt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEditAlertAt.setObjectName(_fromUtf8("lineEditAlertAt"))
        self.gridLayout.addWidget(self.lineEditAlertAt, 5, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Alert every (Minutes):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushAddButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "RSS url to add to monitoring:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Click item to remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Refresh (Minutes): ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "0 for Off", None, QtGui.QApplication.UnicodeUTF8))

