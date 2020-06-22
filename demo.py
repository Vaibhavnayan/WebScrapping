import bs4
import pandas as pd

htmlfile = open("summary.html")

page = bs4.BeautifulSoup(htmlfile, 'html.parser')

table = page.find('table', id='TransactionsTable')
# print(table)

headers = table.find_all('span', class_='Verdana2')
# print(headers)
headers_list = []
for i in range(len(headers)):
    headers_list.append(headers[i].text.strip())

# print(headers_list)
divList = table.find_all('div')

# print(divList)
# print(len(divList))

results = []
start = 0
results_len = len(divList) / len(headers_list)
end = len(headers_list)
num = 1
while len(results) < results_len:
    res = []
    for i in range(start,end):
        res.append(divList[i].text)
    results.append(res)
    start = num * len(headers_list) 
    end = num * len(headers_list)
    num += 1

df = pd.DataFrame(results)
print(df)
