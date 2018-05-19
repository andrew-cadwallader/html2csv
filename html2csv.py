import requests, csv
from bs4 import BeautifulSoup as bs
url = "https://www.w3schools.com/html/html_tables.asp"
text = requests.get(url).text
html = bs(text, "html.parser")
table = html.find('table', id='customers')
data = [[td.text for td in tr.find_all('td')] for tr in table.find_all('tr')]
f = open('output.csv','w')
w = csv.writer(f)
for row in data:
    w.writerow(row)
f.close()
