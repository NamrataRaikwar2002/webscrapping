from os import name
from bs4 import BeautifulSoup
import requests
import json
url="https://www.rottentomatoes.com/m/toy_story_4"

def scrape_movie_details(movie_url):
    req=requests.get(movie_url)
    soup=BeautifulSoup(req.text,"html.parser")
    movie_name=soup.find("h1", class_="scoreboard__title").get_text()
    li=soup.find_all('li',class_="meta-row clearfix")
    detail_dic={}
    detail_dic["Name"]=movie_name
    for detail in li:
        d=detail.text
        if "Producer" in d:
            d=d.replace("\n","")
            spi=d.split(":")
        else:
            spi=d.split()
            
        
        # print(spi)
        if "Rating:" in spi:
            detail_dic["Rating"]=spi[1]                               
        elif "Genre:" in spi:
            gen_list=[]
            gen=spi[1:]
            for g in gen:
                if "," in g:
                    ge=g[:-1]
                    gen_list.append(ge)
                else:
                    if g=="&":
                        continue
                    else:
                        gen_list.append(g)
            detail_dic["Genre"]=gen_list
            
        elif "Language:" in spi:
            detail_dic["Language"]=spi[2]
        elif "Runtime:" in spi:
            time=spi[1:]
            hour=int(time[0][:-1])
            min=int(time[1][:-1])
            minutes=hour*60+min
            detail_dic["Runtime"]=minutes
        elif "Director:" in spi:
            dnamelist=spi[1:]
            i=0
            name_surname=""
            name_surname_list=[]
            while i<len(dnamelist):
                name_surname=name_surname+dnamelist[i]+" "
                # print(len(name_surname))
                
                
                    # else:
                        # name_surname=name_surname+" "+dnamelist[j]
                i=i+1
            split_name=name_surname.split(",")
            strip_name=[]
            for name in split_name:
                strip_name.append(name.strip())
            # print(strip_name)
                
            
            # print(split_name)
            # name_surname_list.append(split_name)
            # print(name_surname_list)
            
            detail_dic["Director"]=strip_name
            # print(detail_dic)
        elif "Producer" in spi:
            producers=spi[1].split(":")
            # print(producers)
            
            # pro=spi[1:]
            # if len(pro)%2==0:
            #     i=0
            #     producer_list=[]
            #     while i<len(pro):
            #         j=i
            #         pro_name=""
            #         while j<i+2:
            #             if j==0:
            #                 pro_name=pro_name+pro[j]
            #             else:
            #                 pro_name=pro_name+" "+pro[j]
            #             j=j+1
            #         producer_list.append(pro_name)
            #         i=i+2
            #     detail_dic["Producer"]=producer_list
            # else:
            #     oname=""
            #     n=-3
            #     while n<=-1:
            #         oname=oname+" "+pro[n]
            #         n=n+1
            #     i=0
            #     producer_list=[]
            #     while i<len(pro)-3:
            #         j=i
            #         pro_name=""
            #         while j<i+2:
            #             if j==0:
            #                 pro_name=pro_name+pro[j]
            #             else:
            #                 pro_name=pro_name+" "+pro[j]
            #             j=j+1
            #         producer_list.append(pro_name)
            #         i=i+2
            #     producer_list.append(oname)
                # detail_dic["Producer"]=spi[1:]
    with open("task4.json","w+") as file:
        json.dump(detail_dic,file,indent=4)
    return detail_dic
        
scrape_movie_details(url)


    
        
    









