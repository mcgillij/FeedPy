#!/usr/bin/python
""" main class """
import webbrowser
from PyQt4 import QtGui
from PyQt4.QtCore import *
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
        self.makeSysTrayActions()
        self.makeTrayIcon()
        self.systrayIcon.messageClicked.connect(self.messageClicked)
        self.systrayIcon.activated.connect(self.iconActivated)
        self.setIcon()
        self.systrayIcon.show()
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
        self.timer.start(self.settings.refresh_time * 60 * 1000)
        self.feed_reader = FeedReader()
        one_off_timer = QTimer()
        one_off_timer.singleShot(1, self._slotRefresh)
        
    def setVisible(self, visible):
        self.minimizeAction.setEnabled(visible)
        self.maximizeAction.setEnabled(not self.isMaximized())
        self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(MainApp, self).setVisible(visible)

    def closeEvent(self, event):
        if self.systrayIcon.isVisible():
            self.hide()
            event.ignore()

    def setIcon(self):
        icon = QtGui.QIcon('heart.svg')
        self.systrayIcon.setIcon(icon)
        self.setWindowIcon(icon)
        text_string = QString("Here's some tooltip string")
        self.systrayIcon.setToolTip(text_string)

    def iconActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.Trigger:
            if super(MainApp, self).isVisible() and self.systrayIcon.isVisible():
                self.hide()
            else:
                self.show()
        elif reason == QtGui.QSystemTrayIcon.MiddleClick:
            self.showMessage()

    def showMessage(self):
        icon = QtGui.QSystemTrayIcon.MessageIcon()
        duration = 5 * 1000
        self.systrayIcon.showMessage(QString("Test message"), QString("More text"), icon, duration)

    def messageClicked(self):
        QtGui.QMessageBox.information(None, "Systray",
                "Sorry, I already gave what help I could.\nMaybe you should "
                "try asking a human?")

    def makeTrayIcon(self):
        self.systrayMenu = QtGui.QMenu(self)
        self.systrayMenu.addAction(self.minimizeAction)
        self.systrayMenu.addAction(self.maximizeAction)
        self.systrayMenu.addAction(self.restoreAction)
        self.systrayMenu.addSeparator()
        self.systrayMenu.addAction(self.quitAction)
        self.systrayIcon = QtGui.QSystemTrayIcon(self)
        self.systrayIcon.setContextMenu(self.systrayMenu)

    def makeSysTrayActions(self):
        self.minimizeAction = QtGui.QAction("Mi&nimize", self, triggered=self.hide)
        self.maximizeAction = QtGui.QAction("Ma&ximize", self, triggered=self.showMaximized)
        self.restoreAction = QtGui.QAction("&Restore", self, triggered=self.showNormal)
        self.quitAction = QtGui.QAction("&Quit", self, triggered=QtGui.qApp.quit)

    def generate_filter_buttons(self):
        # clear the hbox of widgets before adding new ones.
        self.active_filter = None
        for i in range(self.horizontalLayout.count()):
            self.horizontalLayout.itemAt(i).widget().close()
        exclusive_filters = []
        systray_text_list = []
        for f in self.settings.filters:
            if f['plus']:
                num = self.get_filter_count(f)
                widget_text  = f['filter'] + " (" + str(num) + ")"
                systray_text_list.append(widget_text)
                widget = QtGui.QPushButton(QString(widget_text))
                widget.clicked.connect(functools.partial(self.filter_on, f))
                self.horizontalLayout.addWidget(widget)
            else:
                exclusive_filters.append(f)
        if systray_text_list:
            text_string = QString("\n".join(systray_text_list))
            self.systrayIcon.setToolTip(text_string)
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
        five_hours = 18000
        local_time = time.mktime(time.gmtime())
        start_time = time.time()
        self.statusbar.showMessage("Refreshing feeds")
        self.timer.stop()
        self.listWidgetRss.clear()
        self.feed_reader.parse(self.settings.uri_list)
        temp_list = self.feed_reader.entries[:]
        temp_list = self.filter_out(temp_list)
        import datetime
        has_time = False
        for entry in temp_list:
            item = RssListItem(entry, self.listWidgetRss)
            if 'published_parsed' in item.feed:
                mytime = time.mktime(item.feed['published_parsed'])
                has_time = True
            elif 'updated_parsed' in item.feed:
                mytime = time.mktime(item.feed['updated_parsed'])
                has_time = True
            if has_time:
                has_time = False
                difference = local_time - mytime
                difference = int(difference)
                if difference < five_hours:
                    item.setBackgroundColor(Qt.green)
        self.timer.start(self.settings.refresh_time * 60 * 1000)
        status_string = "Refresh took: " + str(int((time.time()- start_time))) + " seconds."
        self.statusbar.showMessage(status_string, 2000)
        self.generate_filter_buttons()

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
    app.setStyle(QString("macintosh"))
    app.exec_()