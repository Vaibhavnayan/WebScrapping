import requests
import pandas
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import os.path
from os import path
import formatExcel

l=[]
l2=[]
l3=[]
l4=[]
l5=[]
finalDf=[]
#baseurl="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
htmlfile=open("summary.html",'r')
soup=BeautifulSoup(htmlfile,"html.parser")

tables=soup.find_all("table",{"id":"TransactionsTable"})
duration= soup.find_all("div",{"class":"p-2 item"})
stats_name= soup.find_all("div",{"class":"item flex-grow pr-1 statistics-name"})
stats_number= soup.find_all("div",{"class":"item statistic-values flex-grow"})
#print(stats_name)


#transactions table (main)--- Start
for txns in tables:
    
    headings=txns.find_all("th")
    names=txns.find_all("td",{"headers":"LraTransaction Name"})
    minimums=txns.find_all("td",{"headers":"LraMinimum"})
    averages=txns.find_all("td",{"headers":"LraAverage"})
    maximums=txns.find_all("td",{"headers":"LraMaximum"})
    percentiles=txns.find_all("td",{"headers":"Lra90 Percent"})
    sd=txns.find_all("td",{"headers":"LraStd. Deviation"})

    passed=txns.find_all("td",{"headers":"LraPass"})
    failed=txns.find_all("td",{"headers":"LraFail"})
    stopped=txns.find_all("td",{"headers":"LraStop"})


    for heading,name,minimum,average,maximum,sds,percentile,passes,fails,stops in zip(headings,names,minimums,averages,maximums,sd,percentiles,passed,failed,stopped):
        d={}
        #d1={}
        d1 = heading.find("span").text
        d[0]= name.find("div").text
        d[1]= minimum.find("div").text
        d[2]= average.find("div").text
        d[3]= maximum.find("div").text
        d[5]= percentile.find("div").text
        d[4]= sds.find("div").text
        d[6]= passes.find("div").text
        d[7]= fails.find("div").text
        d[8]= stops.find("div").text
       # print(type(d["heading"]))
        l.append(d)
        l2.append(d1)
        #print(l2)
#transactions table (main)--- End

#runtime and duration stats---- Start
for time in duration:
    d3={}
    d3[0] = time.find("div",{"class":"scenario-settings-title"}).text
    d3[1] = time.find("div",{"class":"scenario-settings-data"}).text
    if d3[0] == "SLA":
        pass
    else:
        l3.append(d3)
        #print(l3)
#runtime and duration stats---- End


#VUs,Throughput---- Start
for stat1,stat2 in zip(stats_name,stats_number):
    d4={}
    d4[0] = stat1.text
    d4[1] = stat2.text

    l4.append(d4)
    #print(d4)
#VUs,Throughput---- End

#Comments/description of test--- Start
description= input("Enter Test Description")
d5={}
d5[0] = "Comments/Description"
d5[1] = "This is the sample test" + description
l5.append(d5)
print(l5)
#Comments/description of test--- End


df=pandas.DataFrame(l)
df2=pandas.DataFrame(l2)
df3=pandas.DataFrame(l3)
df4=pandas.DataFrame(l4)
df5=pandas.DataFrame(l5)
df2=df2.T
# print(df2)
# print(df)
# print(df3)


pieces = {'v': df5, 'w': df4, 'x': df3, 'y': df2, 'z': df}
result=pandas.concat(pieces)
#result.to_csv("summary.csv",index=False)
if not(path.exists("summary.xlsx")):
    result.to_excel("summary.xlsx",sheet_name='Sheet_1',index=False)
else:
    result.to_excel("summary1.xlsx",sheet_name='Sheet_1',index=False) 
    data1 = pandas.read_excel("summary1.xlsx")
    data2 = pandas.read_excel("summary.xlsx")
    del data1[0]
    finalDf.append(data2)
    finalDf.append(data1)
    finalDf=pandas.concat(finalDf, axis=1)
    finalDf.to_excel("summary.xlsx",sheet_name='Sheet_1',index=False)

formatExcel.mergeCells("summary1.xlsx")