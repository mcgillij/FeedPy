#!/usr/bin/python
import webbrowser
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from pprint import pprint

# Import the interface class
import untitled
from FeedReader import FeedReader
from RssListItem import RssListItem

class TestWindow(QtGui.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)
        self.setupUi(self)
        # Pass this "self" for building widgets and
        # keeping a reference.
        self.uri_list = []
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionRefresh.triggered.connect(self.refreshStuff)
        self.connect(self.pushButton, SIGNAL("clicked()"), self._slotAddClicked)
        self.listWidget.itemClicked.connect(self._slotItemClicked)
        
        
    def _slotItemClicked(self):
        for item in self.listWidget.selectedItems():
            webbrowser.open(item.link)
        
    def _slotAddClicked(self):
        text = self.lineEdit.text()
        self.listWidget_2.addItem(QListWidgetItem(text))
        text = str(text)
        self.uri_list.append(text)
        self.lineEdit.clear()
        
        
    def refreshStuff(self):
        #dir(self.listWidget))
        self.listWidget.clear()
        pprint(self.uri_list)
        fr = FeedReader(self.uri_list)
        #fr = FeedReader(['http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1'])
        for entry in fr.entries:
            
            RssListItem(entry, self.listWidget)

        
    def main(self):
        self.show()

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    tw = TestWindow()
    tw.main()
    app.exec_()
    # This shows the interface we just created. No logic has been added, yet.
    # ['http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1'] #
      #for item in entries:
         #   #pprint(item)
          #  pprint(item['title'])
           # pprint(item['author'])
           # pprint(item['link'])