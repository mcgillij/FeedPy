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
import string

class MainApp(QtGui.QMainWindow, untitled.Ui_MainWindow):
    """ MainApp Class thats generated from the untitled.ui and converted to python """
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.active_filter = None
        self.exclusive_filters = None
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
        self.timer.timeout.connect(self._slotRefresh)
        self.timer.start(self.settings.refresh_time * 60 * 100)
        self.feed_reader = FeedReader()
        one_off_timer = QTimer()
        one_off_timer.singleShot(100, self._slotRefresh)
        one_off_timer.singleShot(1000, self.generate_filter_buttons)
    def generate_filter_buttons(self):
        # clear the hbox of widgets before adding new ones.
        self.active_filter = None
        for i in range(self.horizontalLayout.count()):
            self.horizontalLayout.itemAt(i).widget().close()
        exclusive_filters = []
        for f in self.settings.filters:
            if f['plus']:
                num = self.get_filter_count(f)
                widget_text  = f['filter'] + " (" + str(num) + ")"
                widget = QtGui.QPushButton(QString(widget_text))
                widget.clicked.connect(functools.partial(self.filter_on, f))
                self.horizontalLayout.addWidget(widget)
            else:
                exclusive_filters.append(f)
        if exclusive_filters:
            self.exclusive_filters = exclusive_filters
        else:
            self.exclusive_filters = None

    def get_filter_count(self, pattern):
        count = 0
        for entry in self.feed_reader.entries:
            contains = check_for_val(entry, pattern['filter'])
            if contains:
                count = count + 1
        return count

    def filter_on(self, pattern):
        self.active_filter = pattern
        temp_list = []
        self.listWidgetRss.clear()
        for entry in self.feed_reader.entries:
            contains = check_for_val(entry, pattern['filter'])
            if contains:
                temp_list.append(entry)
        temp_list = self.filter_out(temp_list)
        for i in temp_list:
            RssListItem(i, self.listWidgetRss)

    def filter_out(self, list):
        if self.exclusive_filters:
            temp_list = []
            for entry in list:
                flagged = False
                for pattern in self.exclusive_filters:
                    contains = check_for_val(entry, pattern['filter'])
                    if contains:
                        flagged = True
                if not flagged:
                    temp_list.append(entry)
            return temp_list
        else: 
            return list

    def _slotFilters(self):
        return_value = self.filter_dialogue.exec_()
        if return_value == 1:
            self.settings.load_settings()
            self.generate_filter_buttons()

    def _slotSettings(self):
        """ Clicked on the settings menu item """
        return_value = self.settings_dialogue.exec_()
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
        temp_list = self.feed_reader.entries[:]
        temp_list = self.filter_out(temp_list)
        for entry in temp_list:
            RssListItem(entry, self.listWidgetRss)
        self.timer.start(self.settings.refresh_time * 60 * 1000)
        status_string = "Refresh took: " + str(int((time.time()- start_time))) + " seconds."
        self.statusbar.showMessage(status_string, 2000)

    def main(self):
        self.show()
        
def check_for_val(entry, pattern):
    for key, value in entry.items():
        if isinstance(value, dict):
            continue
        else:
            try:
                value = str(value).encode('utf-8')
                result = value.lower().find(pattern.lower())
                if result != -1:    
                    return True
            except UnicodeEncodeError:
                pass
    return False

def is_ascii(s):
    s = str(s)
    for c in s:
        if c not in string.ascii_letters:
            return False
    return True

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()