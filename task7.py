import json
with open("task5.json","r") as file:
    file1=json.load(file)
def analyse_movies_directors(movies_list):
    # print(movies_list)
    director_count={}
    for one_dic in movies_list:
        # print(one_dic)
        director=one_dic["Director"]
        # print(director)
        for dir in director:
            if dir not in director_count:
                director_count[dir]=1
            else:
                director_count[dir]+=1
    print(director_count)
    with open("task7.json","w+") as file7:
        json.dump(director_count,file7,indent=4)
    return director_count

analyse_movies_directors(file1)