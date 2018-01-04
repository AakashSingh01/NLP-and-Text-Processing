

def answer(page):
    x = page.find_all('span',{'class':"ui_qtext_rendered_qtext"})
    for i in x :
        print("\n\nAnswer :")
        print( i.text )


import pickle
from bs4 import BeautifulSoup as soup
import re
import urllib.request

print("Type a question:")
inp = input()
inp = inp.replace('?','')
inp = inp.strip()
inp = inp.replace(' ','-')
link='https://www.quora.com/'+inp


try:
    with urllib.request.urlopen(link) as response:
        data = str(response.read())
        page = soup(data,"html.parser")
        answer(page)
except:
    print('Answer for this question is not present on Quora.')
