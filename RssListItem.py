from PyQt4.QtGui import QListWidgetItem
class RssListItem(QListWidgetItem):
    def __init__(self, item, *args, **kwargs):
        super(RssListItem, self).__init__(*args, **kwargs)
        self.title = item['title']
        self.author = item['author']
        self.link = item['link']
        self.setText(self.title)