from bs4 import BeautifulSoup
import json
from task1 import scrape_top_list
from task2 import group_by_year
def group_by_decade(movies):
    year_list=[]
    decade_dic={}
    for year in movies:
        mod=year%10
        decade=year-mod
        if decade not in year_list:
            year_list.append(decade)
    year_list.sort()
    for dec in year_list:
        decade_dic[dec]=[]
    for dd in decade_dic:
        dec_year=dd+9
        for y in movies:
            if y>=dd and y<=dec_year:
                for group_dec in movies[y]:
                    decade_dic[dd].append(group_dec)
    # print(decade_dic) 
    with open("task3.json","w+") as file:
        json.dump(decade_dic,file,indent=4)
    return decade_dic
group_by_decade(group_by_year(scrape_top_list()))
    