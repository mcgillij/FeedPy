""" Basic feed parsing """ 
#TODO add some threads to fetch multiple urls at once, but for now its fine 
import feedparser
from pprint import pprint
import Queue
import threading
import time
entries = []
class FeedReader(threading.Thread):
    """ Reads through a list of uri's (rss feeds in theory) """
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = Queue.Queue()
        #lists.append(feedparser.parse(link))
        self.entries = []
        
        #start_time = time.time()
        #for i in range(len(links)):
        
    def parse(self, links):
        global entries
        entries = []
        for i in range(5):
            t = ThreadedParser(self.queue)
            t.setDaemon(True)
            t.start()
            
        for link in links:
            self.queue.put(link)
            
        self.queue.join()
        
        #pprint(entries)
        self.entries = entries
        #print "Elapsed time: %s" % (time.time() - start_time)

                    
class ThreadedParser(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.entries = []

    def run(self):
        while True:
            link = self.queue.get()
            entry = feedparser.parse(link)
            for j in entry['entries']:
                temp_dict = j
                if 'image' in entry['feed']: #check if the feed has an image
                    temp_dict['image'] = entry['feed']['image']
                if temp_dict:
                    global entries
                    entries.append(temp_dict)
            self.queue.task_done()
        

if __name__=='__main__':
    FR = FeedReader(['http://feeds.feedburner.com/RockPaperShotgun?format=xml', 'http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1']) 
    #, 'http://www.reddit.com/r/python/.rss', 'http://rss.slashdot.org/Slashdot/slashdot', 'http://www.1up.com/rss?x=1'
    pprint(FR.entries)