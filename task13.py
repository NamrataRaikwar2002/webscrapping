import json
from task4 import scrape_movie_details
from task12 import scrape_movie_cast


url="https://www.rottentomatoes.com/m/chicken_run"

def final_movies(url1):
    task_4=scrape_movie_details(url1)
    task_12=scrape_movie_cast(url1)
    task_4["cast"]=task_12
    list1=[]
    list1.append(task_4)
    with open("task13.json","w+") as file:
        json.dump(list1,file,indent=4)
    return list1
    
final_movies(url)                                                                               



