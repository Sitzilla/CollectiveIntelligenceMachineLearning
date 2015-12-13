

class crawler:
    # Initialize the crawler with the names of the DB
    def __init__(selfself, dbname):
        pass

    def __del__(self):
        pass

    def dbcomit(self):
        pass

    # Auxilliary function for getting entry id and adding it if
    # it isnt present

    def getentryid(self, table, field, value, createnew=True):
        return None

    # Index to an individual page
    def addtoindex(self, url, soup):
        print 'Indexing %s' % url

    # Extract the tags from an html page (no tags)
    def gettextonly(self, soup):
        return None

    # Separate the words by any non-whitespace character
    def separatewords(self, text):
        return None

    # Return true if url is already indexed
    def isindexed(self, url):
        return False

    # Add a link between two pages
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    # Starting with a list of pages, do a breadth-first search to the given
    # depth, indexing pages as it goes
    def crawl(self, page, depth = 2):
        pass

    # Create the DB tables
    def createindextable(self):
        pass

    #endasd