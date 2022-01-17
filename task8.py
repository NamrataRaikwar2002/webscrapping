import json
import requests
import os
with open("task1.json","r") as file:
    file1=json.load(file)
    
def make_folder(movie_detail):
    for detail  in movie_detail:
        
        path="/home/admin123/Documents/task8(ws)"+detail["Name"]+".text"
        if os.path.exists(path):
            pass
        else:
            with open(path,"w") as file_path:
                url=requests.get(detail["URL"])
                file_path.write(url.text)
                
make_folder(file1)