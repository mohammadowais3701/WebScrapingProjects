from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import re
def getContents(link):
    try:
        url=urlopen(link)
    except HTTPError as e:
        print(str(url))
    try:
        bsObj=BeautifulSoup(url,features="html.parser")
        contents=bsObj.find('div',{"id":"content"})
    except AttributeError as e:
        print(str(e))
        return None
    return contents
l=""
Themes=[]
for i in range(1,21):
    link="http://jekyllthemes.org"+l
    contents=getContents(link)
    if contents is not None:


            contents = contents.find("div", {"class": "gallery"}).find_all("div",{"class":"item"})
           # contents=contents.find_all("div",{"class":"item"})
            for j in contents:
                k={"ThemeName":j.find('a').find("div",{"class":"item-name"}).text,'Link':link+j.find("a")['href']}
              #  print(j.find('a').find("div",{"class":"item-name"}).text)
              #  print(link+j.find("a")['href'])
                Themes.append(k)
    l="/page"+str((i+1))


df=pd.DataFrame(Themes,columns={"ThemeName","Link"})
df.to_csv("Jkyll ThemesOrg.csv")
print("Saved in your directory where you are running your application")

