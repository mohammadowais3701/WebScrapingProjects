from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import re

def getNews(link):
    try:
       html=urlopen(link)
    except HTTPError as e:
        print(str(e))
        return None
    try:
        bsObj=BeautifulSoup(html.read(),features="html.parser")
        news=bsObj.find('table',{'class':'itemlist'}).find_all("tr",{"class":"athing"})

    except AttributeError as e:
        print(str(e))
    return news
data=[]
#data=pd.DataFrame([{'index':'','VoteLinks':'','StoryLink':'','Title':'','SiteLink':''}])

for i in range(1,16):
    news=getNews("https://news.ycombinator.com"+"/news?p="+str(i))
    for i in news:

        try:

            k={'Index': i.find('td',{'class':'title'}).text, 'VoteID': i.find('td',{'class':'votelinks'}).a['id'][3:], 'StoryLink': i.find('a',{'class':'storylink'})['href'], 'Title': i.find('a', {'class': 'storylink'}).text, 'SiteLink': i.find('span', {'class': 'sitestr'}).text}
            data.append(k)
           # print(i.find('td',{'class':'title'}).text)
           # print(i.find('td',{'class':'votelinks'}).a['id'][3:])
           # print(i.find('a',{'class':'storylink'})['href'])
           # print(i.find('a', {'class': 'storylink'}).text)
           # print(i.find('span', {'class': 'sitestr'}).text)
        except AttributeError as e:
            continue


data=pd.DataFrame(data)
data.set_index('Index',inplace=True)
data.to_csv('HackerNews.csv')
print("....................SAVED.......................")