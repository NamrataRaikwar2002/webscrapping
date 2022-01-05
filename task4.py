from bs4 import BeautifulSoup
import requests
import json
url="https://www.rottentomatoes.com/m/ernest_and_celestine"

def scrape_movie_details(movie_url):
    req=requests.get(movie_url)
    soup=BeautifulSoup(req.text,"html.parser")
    movie_name=soup.find("h1", class_="scoreboard__title").get_text()
    li=soup.find_all('li',class_="meta-row clearfix")
    detail_dic={}
    detail_dic["Name"]=movie_name
    for detail in li:
        d=detail.text
        spi=d.split()
        if "Rating:" in spi:
            detail_dic["Rating"]=spi[1]                               
        elif "Genre:" in spi:
            detail_dic["Genre"]=spi[1:]
        elif "Language:" in spi:
            detail_dic["Language"]=spi[2:]
        elif "Runtime:" in spi:
            time=spi[1:]
            hour=int(time[0][:-1])
            min=int(time[1][:-1])
            minutes=hour*60+min
            detail_dic["Runtime"]=minutes
        elif "Director:" in spi:
            dnamelist=spi[1:]
            i=0
            name_surname_list=[]
            while i<len(dnamelist):
                j=i
                name_surname=""
                while j<i+2:
                    if j==i:
                        name_surname=name_surname+dnamelist[j]
                    else:
                        name_surname=name_surname+" "+dnamelist[j]
                    j=j+1
                name_surname_list.append(name_surname)
                i=i+2
            detail_dic["Director"]=name_surname_list
        elif "Producer:" in spi:
            pro=spi[1:]
            print(pro)
            if len(pro)%2==0:
                i=0
                producer_list=[]
                while i<len(pro):
                    j=i
                    pro_name=""
                    while j<i+2:
                        if j==0:
                            pro_name=pro_name+pro[j]
                        else:
                            pro_name=pro_name+" "+pro[j]
                        j=j+1
                    producer_list.append(pro_name)
                    i=i+2
                detail_dic["Producer"]=producer_list
            else:
                oname=""
                n=-3
                while n<=-1:
                    oname=oname+" "+pro[n]
                    n=n+1
                print(oname)
                i=0
                producer_list=[]
                while i<len(pro)-3:
                    j=i
                    pro_name=""
                    while j<i+2:
                        if j==0:
                            pro_name=pro_name+pro[j]
                        else:
                            pro_name=pro_name+" "+pro[j]
                        j=j+1
                    producer_list.append(pro_name)
                    i=i+2
                producer_list.append(oname)
                print(producer_list)
                detail_dic["Producer"]=producer_list
                
    print(detail_dic)
    with open("task4.json","w+") as file:
        json.dump(detail_dic,file,indent=4)
        
scrape_movie_details(url)


    
        
    









