import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getContent(link):
    try:
        url=urlopen(link)
    except HTTPError as e:
        print(str(e))
        return None
    try:
        bsObj=BeautifulSoup(url,features='html.parser')
        contents=bsObj.find_all('article',{"class":"border rounded-1 box-shadow bg-gray-light my-4"})
    except AttributeError as e:
        print(str(e))
    return contents
data=[]
link="https://github.com/topics/jekyll-themes"
contents=getContent(link)
print(len(contents))
if contents is not None:
    for i in contents:
        star=i.find('div', {'class': 'd-flex flex-items-start ml-3'}).find("a", {'class': 'social-count float-none'}).text
        star=star.replace(" ","").replace("\n","")
        k={"URL":link+i.find('div',{'class':'d-flex flex-items-start ml-3'}).find("a",{'class':'social-count float-none'})['href'],"Stars":star}
       # print(link+i.find('div',{'class':'d-flex flex-items-start ml-3'}).find("a",{'class':'social-count float-none'})['href'])
        #print(i.find('div', {'class': 'd-flex flex-items-start ml-3'}).find("a", {'class': 'social-count float-none'}).text)

        data.append(k)
df=pd.DataFrame(data)
df.to_csv("JkeyllThmes.csv")
print("Saved in your directory where you are running your application")