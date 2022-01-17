from bs4 import BeautifulSoup
import requests
import json
res=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup=BeautifulSoup(res.text,"html.parser")
def scrape_top_list():
    movie_detail=[]
    main_div=soup.find('div', class_="body_main container")
    table1=main_div.find('table',class_="table")
    trs=table1.find_all('tr')
    for tr2 in trs:
        dic1={}
        td1=tr2.find_all('td')
        for j in td1:
            # print(j)
            rank=tr2.find("td",class_="bold").get_text()[:-1]
            dic1["Rank"]=int(rank)
            # print(rank)
            rating=tr2.find("span", class_="tMeterScore").get_text()[:-1]
            dic1["Rating"]=float(rating)
            review=tr2.find("td",class_="right hidden-xs").get_text()
            dic1["Review"]=int(review)
            name=tr2.find("a",class_="unstyled articleLink")["href"][3:]
            dic1["Name"]=name
            url=tr2.find("a",class_="unstyled articleLink")["href"]
            link="https://www.rottentomatoes.com"+url
            dic1["URL"]=link
            year=tr2.find("a",class_="unstyled articleLink").get_text().strip()[-5:-1]
            dic1["Year"]=int(year)
            
        movie_detail.append(dic1)
        if {} in movie_detail:
            movie_detail.remove({})
    with open("task1.json","w+") as file:
        json.dump(movie_detail,file,indent=4)
    return movie_detail
            
print(scrape_top_list())