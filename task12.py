import requests
from bs4 import BeautifulSoup
import json

url="https://www.rottentomatoes.com/m/soul_2020"
def scrape_movie_cast(url1):
    req=requests.get(url1)
    soup=BeautifulSoup(req.text,"html.parser")
    
    cast_list=[]
    main_div=soup.find("div",class_="castSection")
    name=main_div.find_all("div",class_="cast-item media inlineBlock")
    more_name=main_div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    for n in name:
        cast_dic={}
        a=n.find("a")["href"][11:]
        cast_dic["Name"]=a
        cast_list.append(cast_dic)
    for more in more_name:
        cast_dic={}
        more_a=more.find("a")["href"][11:]
        cast_dic["Name"]=more_a
        cast_list.append(cast_dic)
    with open("task12.json","w+") as file:
        json.dump(cast_list,file,indent=4)
        
    return cast_list
scrape_movie_cast(url)


