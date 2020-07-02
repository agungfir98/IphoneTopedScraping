import requests
from bs4 import BeautifulSoup
import pandas as pd

URL ="https://www.tokopedia.com/search?q=iphone%2011&source=universe&st=product&page=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


laman = requests.get(URL, headers=headers)
soup = BeautifulSoup(laman.content, 'html.parser')

konten = soup.find_all('div', class_="css-1g20a2m")


# Menggunakan panda untuk membuat dataframe
nama_produk = []
harga_produk = []

for kontens in konten:
    prod_name = kontens.find(class_="css-1bjwylw").get_text()
    prod_price = int(kontens.find('span', class_='css-o5uqvq').get_text().replace('Rp','').replace('.',''))
    # print(prod_price,end='\n'*2)
    nama_produk.append(prod_name)
    harga_produk.append(prod_price)

prod_dict = {'nama':nama_produk, 'harga':harga_produk}
df = pd.DataFrame(data=prod_dict, columns= ['nama', 'harga'])

df.sort_values('harga',ascending=True)
df.to_csv("Daftar.csv")