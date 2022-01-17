import json
with open("task5.json","r") as file:
    read_file=json.load(file)
    
    
def analyse_movies_genre(movies_list):
    genre_dic={}
    for detail in movies_list:
        
        if "Genre" in detail:
            for gen in detail["Genre"]:
                if gen not in genre_dic:
                    if "," in gen:
                        genre_dic[gen]=1
                    else:
                        genre_dic[gen]=1
                else:
                    genre_dic[gen]+=1
    # print(genre_dic)
    with open ("task11.json","w+") as f:
        json.dump(genre_dic,f,indent=4)
    return genre_dic
analyse_movies_genre(read_file)





