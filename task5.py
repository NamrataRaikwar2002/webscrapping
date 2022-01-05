import json
from task1 import scrape_top_list
from task4 import scrape_movie_details

def get_movie_list_details(movies_list):
    detail_10_list=[]
    for detail in movies_list:
        url1=detail["URL"]
        detail_10_dic=scrape_movie_details(url1)
        detail_10_list.append(detail_10_dic)
    with open("task5.json","w+") as file:
        json.dump(detail_10_list,file,indent=4)
    return detail_10_list
    
    
top_movie=scrape_top_list()
get_movie_list_details(top_movie[:10])


