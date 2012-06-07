#!/usr/bin/python
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
class MainApp(QtGui.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        # Pass this "self" for building widgets and
        # keeping a reference.
        self.uri_list = []
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionSave_Url_List.triggered.connect(self._slotSaveClicked)
        self.actionLoad_Url_List.triggered.connect(self._slotLoadClicked)
        self.connect(self.pushRefreshButton, SIGNAL("clicked()"), self._slotRefresh)
        self.connect(self.pushAddButton, SIGNAL("clicked()"), self._slotAddClicked)
        self.listWidgetRss.itemClicked.connect(self._slotItemClicked)
    def _slotSaveClicked(self):
        print "Save"
        if not self.uri_list:
            print "There's no list entries, not saving"
        else:
            save_file = file("urls.dat", "wb")
            pickle.dump(self.uri_list, save_file, 2)
            save_file.close()

    def _slotLoadClicked(self):
        print "Load"
        if check_for_save_file():
            self.uri_list = []
            self.listWidgetUrls.clear()
            load_file = file('urls.dat', "rb")
            self.uri_list = pickle.load(load_file)
            load_file.close()
            for item in self.uri_list:
                self.listWidgetUrls.addItem(QListWidgetItem(item))
        else:
            print "No save file found"
        


    def _slotItemClicked(self):
        for item in self.listWidgetRss.selectedItems():
            webbrowser.open(item.link)

    def _slotAddClicked(self):
        text = self.lineEditUrl.text()
        self.listWidgetUrls.addItem(QListWidgetItem(text))
        text = str(text)
        self.uri_list.append(text)
        self.lineEditUrl.clear()
        
    def _slotRefresh(self):
        self.listWidgetRss.clear()
        pprint(self.uri_list)
        fr = FeedReader(self.uri_list)
        #fr = FeedReader(['http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1'])
        for entry in fr.entries:
            RssListItem(entry, self.listWidgetRss)

    def main(self):
        self.show()

def check_for_save_file():
    """ check for the existence of a save """
    path = "./"
    for cur_file in glob.glob(os.path.join(path, "*.dat")):
        return True
    return False


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    MA = MainApp()
    MA.main()
    app.exec_()