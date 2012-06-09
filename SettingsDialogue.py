""" Dialogue for entering user settings into the app """
import diag
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Settings import Settings

class SettingsDialogue(QDialog, diag.Ui_Dialog):
    """ this should pop up a settings window """
    def __init__(self, parent=None):
        super(SettingsDialogue, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushAddButton, SIGNAL("clicked()"), self._slotAddClicked)
        self.show()
        self.settings = Settings()
        if self.settings.load_settings():
            self.lineEditRefresh.setText(str(self.settings.refresh_time))
            for u in self.settings.uri_list:
                self.listWidgetUrls.addItem(QListWidgetItem(u))
        self.listWidgetUrls.itemClicked.connect(self._slotItemClicked)

    def _slotItemClicked(self):
        """ clicked on an item in the list widget """
        item = self.listWidgetUrls.takeItem(self.listWidgetUrls.currentRow())
        item = None

    def _slotAddClicked(self):
        """ clicked on the add button """
        text = self.lineEditUrl.text()
        self.listWidgetUrls.addItem(QListWidgetItem(text))
        text = str(text)
        self.settings.uri_list.append(text)
        self.lineEditUrl.clear()

    def accept(self, *args, **kwargs):
        """ Runs when the OK button is pressed and exits the dialogue """
        self.settings.refresh_time = int(self.lineEditRefresh.text())
        self.settings.uri_list = []
        items = self.return_items()
        for i in items:
            item_text = str(i.text()).strip()
            if item_text == '':
                pass
            else:
                self.settings.uri_list.append(str(i.text()))
        self.settings.save_settings()
        return QDialog.accept(self, *args, **kwargs)

    def return_items(self):
        """ Fetch all the items in the list widget """
        for i in xrange(self.listWidgetUrls.count()):
            yield self.listWidgetUrls.item(i)
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    MA = SettingsDialogue()
    app.exec_()