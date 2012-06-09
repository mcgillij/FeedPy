""" Basic feed parsing """ 
#TODO add some threads to fetch multiple urls at once, but for now its fine 
import feedparser
 
from pprint import pprint

class FeedReader():
    """ Reads through a list of uri's (rss feeds in theory) """
    def __init__(self, links):
        lists = []
        for link in links:
            lists.append(feedparser.parse(link))
        self.entries = []
        for l in lists:
            for j in l['entries']:
                temp_dict = j
                if 'image' in l['feed']: #check if the feed has an image
                    temp_dict['image'] = l['feed']['image']
                if temp_dict:
                    self.entries.append(temp_dict)

if __name__=='__main__':
    FR = FeedReader(['http://www.reddit.com/r/python/.rss', 'http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1'])
    pprint(FR.entries)