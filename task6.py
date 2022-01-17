import json
with open("task5.json","r") as file:
    file1=json.load(file)

def analyse_movies_language(movies_list):
    language_dic={}
    real_lang=[]
    for lan in movies_list:
        if "Language" in lan:
            lang=lan["Language"]
        real_lang.append(lang)
    for l in real_lang:
        if l not in language_dic:   
            language_dic[l]=1
        else:
            language_dic[l]+=1 
    # print(language_dic)                                                 
            
    with open("task6.json","w+") as task_6:
        json.dump(language_dic,task_6,indent=4)
    return  language_dic
        

analyse_movies_language(file1)

