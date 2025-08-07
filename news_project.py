import requests
from bs4 import BeautifulSoup

url="https://www.ndtv.com/"

response=requests.get(url)

if response.status_code==200:
    print("Page is successfully fetch")
    html_content=response.text

    soup=BeautifulSoup(html_content,'html.parser')
    page_title=soup.title.string
    print("Title of the Page :",page_title)

    headlines=soup.find_all(['h3','h2'])

    headline_list=[]
    for i in headlines:
        text=i.get_text(strip=True)
        if text and text not in headline_list:
            headline_list.append(text)

    print("\n Top Headlines:\n")
    for i , headline in enumerate(headline_list[:10],start=1):
        print(f"{i}.{headline}")


    with open("headlines.txt",'w')as f:
        for i,headline in enumerate(headline_list[:20],start=1):
            f.write(f"{i}.{headline}\n")




else:
    print(f"failed to fetch page. Status code:{response.status_code}")


