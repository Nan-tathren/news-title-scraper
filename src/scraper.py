import requests
import bs4
import csv
from datetime import datetime

result=requests.get("https://www.seznamzpravy.cz/sekce/stalo-se-177")
soup=bs4.BeautifulSoup(result.text,'lxml')
current_news=soup.select('h3')

news_list=[]

for new in current_news:
    article=new.getText()
    news_list.append(article)

with open('news_titles.csv','w',newline='', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['Title', 'Timestamp'])
    
    # Write each title with the current timestamp
    for title in news_list:
        writer.writerow([title, datetime.now()])