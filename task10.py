import json
from os import path
with open("task5.json","r") as file:
    read_file=json.load(file)
def analyse_language_and_directors(movie_detail):
    lan_count=0
    # print(movie_detail)
    dir_dic={}
    for detail in movie_detail:
        lan_dic={}
        if "Language" in detail:
            for dir in detail["Director"]:
                for det in movie_detail:
                    if dir in det["Director"]:
                        if det["Language"] not in lan_dic:
                            lan_dic[det["Language"]]=1
                            dir_dic[dir]=lan_dic
                        else:
                            lan_dic[det["Language"]]+=1
                            dir_dic[dir]=lan_dic
        
    with open("task10.json","w+") as f:
        json.dump(dir_dic,f,indent=4)
            
            
        
analyse_language_and_directors(read_file)