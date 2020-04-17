from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
def getContents(url):
    try:
        link=urlopen(url)
    except HTTPError as e:
        print(str(e))
        return
    try:
        bsObj=BeautifulSoup(link,features="html.parser")
        contents=bsObj.find('div',{"id":"fsb"})

        #contents=bsObj.find_all("h3",{'name':re.compile("row[0-9]*")})
    except AttributeError as e:
        print(str(e))
    return contents
link="https://blog.feedspot.com/pakistan_blogs/"
contents=getContents(link)
BlogsData=[]
if contents is not None:
  #  contents=contents.find_all({'h3'})
    #print(contents.find_all({'h3'}))
    #for i in range(len(contents)):
    #contents=contents.find_all({'h3'})
    for i in contents.find_all({'h3'}):
        try:
            id=i['name']

            k={'Serial No':(i.text).split('.')[0],'Topic':(i.text).split('.')[1],'About Blog':' '.join(contents.find('p', {'id': id}).text.split('.')[0].split(' ')[3:])+'.','Blog':contents.find('p', {'id': id}).find('a', {'class': 'ext'})['href'],'Also In':(link+contents.find('p', {'id': id}).find_next('a', {'class':''})['href'])}
           # print((i.text).split('.')[0])
           # print((i.text).split('.')[1])
            #print(' '.join(contents.find('p', {'id': id}).text.split('.')[0].split(' ')[3:])+'.')
            # print()
            #print(contents.find('p', {'id': id}).find('a', {'class': 'ext'})['href'])

         
            BlogsData.append(k)
        except AttributeError as e:
            continue


df=pd.DataFrame(BlogsData,columns={'Serial No','Topic','Blog','Also In','About Blog'})
print(df['Also In'])
df.set_index('Serial No',inplace=True)
df.to_csv('Top Pakistani Bloggers.csv')
print('Done')


