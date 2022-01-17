import json
import requests
import os
import time
import random
with open("task1.json","r") as file:
    file1=json.load(file)
    
def make_folder(movie_detail):
    random_sec=random.randint(1,3)
    for detail  in movie_detail:
        
        path="/home/admin123/Documents/task9(ws)"+detail["Name"]+".json"
        if os.path.exists(path):
            pass
        else:
            with open(path,"w") as file_path:
                url=requests.get(detail["URL"])
                file_path.write(url.text)
        time.sleep(random_sec)
                
make_folder(file1)