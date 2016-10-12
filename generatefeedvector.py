import feedparser
import re

#return a dict containing RSS feed subscription title and key words count
def getwordcounts(url):
    d=feedparser.parse(url)
    wc={}
    try:
        success=re.compile(r'^[2-3]\d\d$').match(str(d['status']))
        if success!=None:

            #go through all content entries
            for e in d.entries:
                if 'summary' in e: summary=e.summary
                else: summary=e.description

                #generate a words list
                words=getwords(e.title+' '+summary)
                for word in words:
                    wc.setdefault(word,0)
                    wc[word]+=1
            if d['feed']['title']!='':
                title=d['feed']['title']
            else:
                title=d['feed']['subtitle']
            return title,wc
        else:
            return False
    except: return False

def getwords(html):
    #get rid of all HTML tag
    txt=re.compile(r'<[^>]+>').sub('',html)
    #using all non characters to select words
    words=re.compile(r'[^A-Z^a-z]+').split(txt)
    #transfer to lower case
    return [word.lower() for word in words if word!='']

apcount={}
wordcounts={}
feedlist=[line for line in file('feedlist.txt')]
for feedurl in feedlist:
    if getwordcounts(feedurl)==False: continue
    else:
        title,wc=getwordcounts(feedurl)
        if title=='':
            title='No title availiable'
        wordcounts[title]=wc
        for word,count in wc.items():
            apcount.setdefault(word,0)
            if count>1:
                apcount[word]+=1
wordlist=[]
for w,bc in apcount.items():
    frac=float(bc)/len(feedlist)
    if frac>0.05 and frac<0.3:
        wordlist.append(w)

out=file('blogdata.txt','w')
out.write('blog')
for word in wordlist: 
    out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wc: 
            out.write('\t%d' % wc[word])
        else: 
            out.write('\t0')
    out.write('\n')



