import feedparser
 
from pprint import pprint

class FeedReader():
    def __init__(self, links):
         
        lists = []
        for link in links:
            lists.append(feedparser.parse(link))
    
        self.entries = []
        for l in lists:
            #pprint(l)
            status = l['status']
            if status == 200:
                #print "success!"
                for j in l['entries']:
                    #pprint(j)
                    self.entries.append({'title': j['title'], 'author': j['author'], 'link': j['link']})
