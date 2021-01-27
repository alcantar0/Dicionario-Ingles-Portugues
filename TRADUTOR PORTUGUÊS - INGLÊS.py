import requests
from bs4 import BeautifulSoup
word=str(input("Qual palavra você quer traduzir?: "))
url=('https://www.linguee.com.br/portugues-ingles/search?source=ingles&query='+ word)
page=requests.get(url)
page2=BeautifulSoup(page.content, 'html.parser')
find=page2.find(class_="dictLink featured")
html=str(find)
size=len(html)
final_word=""
for x in range(0, size):
    if html[x]==">":
        final_word+=html[x+1:-1]
        final_word=final_word.replace("</a", '')
        print(final_word.upper())
        from time import sleep
        sleep(3)
    else:
        x+=1






