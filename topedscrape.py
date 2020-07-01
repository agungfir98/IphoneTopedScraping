import requests
from bs4 import BeautifulSoup

URL ="https://www.tokopedia.com/search?q=iphone%2011&source=universe&st=product&page=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


laman = requests.get(URL, headers=headers)
soup = BeautifulSoup(laman.content, 'html.parser')

konten = soup.find_all('div', class_="css-1g20a2m")

for kontens in konten:
    prod_name = kontens.find(class_="css-1bjwylw")
    prod_price = kontens.find('span', class_='css-o5uqvq')
    print(prod_name.text,prod_price.text,end='\n'*2)