import diag
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SettingsDialogue(QDialog, diag.Ui_Dialog):
    """ this should pop up a settings window """
    def __init__(self, parent=None):
        super(SettingsDialogue, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushAddButton, SIGNAL("clicked()"), self._slotAddClicked)
        self.show()
        
    def _slotAddClicked(self):
        text = self.lineEditUrl.text()
        self.listWidgetUrls.addItem(QListWidgetItem(text))
        text = str(text)
        self.lineEditUrl.clear()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    MA = SettingsDialogue()
    app.exec_()