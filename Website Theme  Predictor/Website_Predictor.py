import urllib.request
import pickle
from nltk.tokenize import  word_tokenize
from nltk import FreqDist

def word_frequencies(data):
   f = FreqDist(data)
   return f.max()

def removeHTML(data):
    ls = ['script','https','http','span','div','doctype','class','table','Submit',
              'end','endif','link','code','prefetch', 'meta', 'cleartype','url','href'
              ,'img','style','type', 'events', 'treeitem', 'issue', 'tracker', 'treeitem'
              , 'list', 'true', 'data', 'types', 'lists','Event', 'time', 'more', 'menu'
              ,'html','head', 'imagetoolbar', 'false', 'stylesheet', 'default','official',
              'home','black', 'viewport', 'HandheldFriendly', 'True', 'print', 'braille', 'embossed',
              'speech', 'IEMobile', 'screen', 'icon', 'white', 'shape','blue', 'title', 'Welcome',
              'description', 'official', 'home','subnav','nbsp','funtion','RETURN','null']
    ds = [w.lower() for w in ls]
    ls = list(set(ds))
    filtered_sentence = [w for w in data if  w not in ls]
    print(ls)
    return filtered_sentence


def clean(data):
    s = [i.lower() for i in data if i.isalpha() ]
    for i in s :
        if(len(i)<4):
            s=list(filter(lambda a: a != i, s))
    return s

link = 'https://www.python.org/'
with urllib.request.urlopen(link) as response:
   data = str(response.read())

data= word_tokenize(data)
data = clean(data)
data = removeHTML(data)
print(link,"  :  ",word_frequencies(data).upper())
#df = word_frequencies(data)
