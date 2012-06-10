""" Derived class that will hold the filter items """
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QListWidgetItem
class FilterListItem(QListWidgetItem):
    """ Container class for a feed item """
    def __init__(self, value, plus, *args, **kwargs):
        super(FilterListItem, self).__init__(*args, **kwargs)
        self.setText(value)
        self.value = value
        self.plus = plus
        if self.plus:
            self.setBackgroundColor(Qt.green)
        else:
            self.setBackgroundColor(Qt.red)
        
