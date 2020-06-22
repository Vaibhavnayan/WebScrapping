import requests
import pandas
from bs4 import BeautifulSoup

l=[]
#baseurl="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
htmlfile=open("summary.html",'r')
for page in range(0,10,10):
    #r = requests.get(baseurl+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    #c=r.content
    soup=BeautifulSoup(htmlfile,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        
        try:
            d["beds"]=item.find("span",{"class":"infoBed"}).text
        except:
            d["beds"]= "Data Not Available"

        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for fgroup, fname in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in fgroup.text:
                    d["Lot Size"]= fname.text
        l.append(d)

#print(l)
df=pandas.DataFrame(l)
print(df)
df.to_csv("summary.csv")