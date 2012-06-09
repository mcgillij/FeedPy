#!/usr/bin/python
""" main class """
import webbrowser
from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
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
import time

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
        self.pushRefreshButton.clicked.connect(self._slotRefresh)
        self.listWidgetRss.itemClicked.connect(self._slotItemClicked)
        self.settings_dialogue = SettingsDialogue(parent=self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(self.settings.refresh_time * 60 * 1000)
        one_off_timer = QTimer()
        one_off_timer.singleShot(1000, self._slotRefresh)
        
    def refresh(self):
        self._slotRefresh()
        self.statusbar.showMessage("Last refresh at: " + str(time.ctime()))

    def _slotSettings(self):
        """ Clicked on the settings menu item """
        return_value = self.settings_dialogue.exec_()
        pprint(return_value)
        if return_value == 1:
            self.settings.load_settings()
            self._slotRefresh()
        self.statusbar.showMessage('Feeds tracked: ' + str(len(self.settings.uri_list)))

    def _slotItemClicked(self):
        """ RSS list item clicked"""
        for item in self.listWidgetRss.selectedItems():
            webbrowser.open(item.feed.link)

    def _slotRefresh(self):
        """ Refresh button clicked """
        self.timer.stop()
        self.listWidgetRss.clear()
        fr = FeedReader(self.settings.uri_list)
        for entry in fr.entries:
            RssListItem(entry, self.listWidgetRss)
        self.timer.start(self.settings.refresh_time * 60 * 1000)

    def main(self):
        self.show()

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()