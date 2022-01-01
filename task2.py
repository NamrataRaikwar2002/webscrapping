from bs4 import BeautifulSoup
import json
from task1 import scrape_top_list

def  group_by_year(movies):
    year_list=[]
    
    for movie_detail in movies:
        year=movie_detail["Year"]
        if year not in year_list:
            year_list.append(year)
    yeargroup_dic={}
    for key_year in year_list:
        same_year_list=[]
        for detail in movies:
            if key_year==detail["Year"]:
                if detail not in same_year_list:
                    same_year_list.append(detail)
        yeargroup_dic[key_year]=same_year_list        
        print(yeargroup_dic)
    with open("task2.json","w+") as file2:
        json.dump(yeargroup_dic,file2,indent=4)
    return yeargroup_dic
                


group_by_year(scrape_top_list())
    