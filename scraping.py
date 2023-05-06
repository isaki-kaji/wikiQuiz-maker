import requests
from bs4 import BeautifulSoup

def getTitleList(url):
    titleList=set()
    load_url=url
    html=requests.get(load_url)
    soup= BeautifulSoup(html.content,"html.parser")
    topic=soup.find(class_="mw-parser-output")
    for element in topic.find_all("a"):
        titleList.add(element.text)
    returnList=list(titleList)
    return returnList