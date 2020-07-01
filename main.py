import requests
from bs4 import BeautifulSoup

# keyword = input("Apa yang kamu cari? ")
URL = "https://shopee.co.id/Handphone-Aksesoris-cat.40"#+keyword

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

sesiFS = soup.findAll(attrs={"shopee-search-item-result__item"})
print(sesiFS)