#!/usr/bin/python
""" main class """
import webbrowser
from PyQt4 import QtGui
from PyQt4.QtCore import QTimer, QString
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
from FilterDialogue import FilterDialogue
import functools

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
        self.actionFilters.triggered.connect(self._slotFilters)
        self.pushRefreshButton.clicked.connect(self._slotRefresh)
        self.listWidgetRss.itemClicked.connect(self._slotItemClicked)
        self.settings_dialogue = SettingsDialogue(self.settings, parent=self)
        self.filter_dialogue = FilterDialogue(self.settings, parent=self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start(self.settings.refresh_time * 60 * 1000)
        self.feed_reader = FeedReader()
        one_off_timer = QTimer()
        one_off_timer.singleShot(1000, self._slotRefresh)
        one_off_timer.singleShot(0, self.generate_filter_buttons)
        
    def refresh(self):
        self._slotRefresh()
        self.statusbar.showMessage("Last refresh at: " + str(time.ctime()))

    def generate_filter_buttons(self):
        # clear the hbox of widgets before adding new ones.
        for i in range(self.horizontalLayout.count()):
            self.horizontalLayout.itemAt(i).widget().close()
            
        for f in self.settings.filters:
            widget = QtGui.QPushButton(QString(f['filter']))
            widget.clicked.connect(functools.partial(self.filter_on, f))
            self.horizontalLayout.addWidget(widget)

    def filter_on(self, filter):
        #pprint (filter)
        pprint(self.feed_reader.entries)
        new_list = []
        for e in self.feed_reader.entries:
            val = check_for_val(e, filter['filter'])
            if val:
                new_list.append(e)
        print "here's the new list"
        if new_list:
            self.listWidgetRss.clear()
            for entry in new_list:
                RssListItem(entry, self.listWidgetRss)

    def _slotFilters(self):
        print "Filters button pushed"
        return_value = self.filter_dialogue.exec_()
        pprint(return_value)
        if return_value == 1:
            self.settings.load_settings()
            pprint(self.settings.filters)
            self.generate_filter_buttons()

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
        start_time = time.time()
        self.statusbar.showMessage("Refreshing feeds")
        self.timer.stop()
        self.listWidgetRss.clear()
        self.feed_reader.parse(self.settings.uri_list)
        for entry in self.feed_reader.entries:
            RssListItem(entry, self.listWidgetRss)
        self.timer.start(self.settings.refresh_time * 60 * 1000)
        status_string = "Refresh took: " + str(int((time.time()- start_time))) + " seconds."
        self.statusbar.showMessage(status_string, 2000)

    def main(self):
        self.show()
        
def check_for_val(entry, pattern):
    for key, value in entry.items():
        result = str(value).lower().find(pattern.lower())
        if result != -1:
            return True
    return False

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()