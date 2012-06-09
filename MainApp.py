#!/usr/bin/python
""" main class """
import webbrowser
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from pprint import pprint
import os, glob
# Import the interface class
import untitled
from FeedReader import FeedReader
from RssListItem import RssListItem
import pickle
from Settings import Settings
from SettingsDialogue import SettingsDialogue

class MainApp(QtGui.QMainWindow, untitled.Ui_MainWindow):
    """ MainApp Class thats generated from the untitled.ui and converted to python """
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.settings = Settings()
        self.settings.load_settings()
        self.statusbar.showMessage('Feeds tracked: ' + str(len(self.settings.uri_list)))
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionSettings.triggered.connect(self._slotSettings)
        self.connect(self.pushRefreshButton, SIGNAL("clicked()"), self._slotRefresh)
        self.listWidgetRss.itemClicked.connect(self._slotItemClicked)
        self._slotRefresh()
        
        
    def _slotSettings(self):
        diag = SettingsDialogue()
        return_value = diag.exec_()
        pprint(return_value)
        if return_value == 1:
            self.settings.load_settings()
            self.statusbar.showMessage('Feeds tracked: ' + str(len(self.settings.uri_list)))

    def _slotItemClicked(self):
        for item in self.listWidgetRss.selectedItems():
            webbrowser.open(item.feed.link)

    def _slotRefresh(self):
        self.listWidgetRss.clear()
        fr = FeedReader(self.settings.uri_list)
        #fr = FeedReader(['http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1'])
        for entry in fr.entries:
            RssListItem(entry, self.listWidgetRss)

    def main(self):
        self.show()

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()