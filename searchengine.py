class crawler:
    def __init__(self,dbname):
        pass

    def __del__(self):
        pass
    def dbcommit(self):
        pass
    #get entry id if exists, otherwise, generate a new one
    def getentryid(self,table,field,value,createnew=True):
        return None
    #set up index for each web
    def addtoindex(self,url,soup):
        print 'Indexing %s' % url
    #get only text content from a web
    def gettextonly(self,soup):
        return None
    #split words according to input content
    def seperatewords(self,text):
        return None
    #if index exists return True
    def isindexed(self,url):
        return False
    #add a link between two web
    def addlinkref(self,urlFrom,urlTo,linkText):
        pass
    #