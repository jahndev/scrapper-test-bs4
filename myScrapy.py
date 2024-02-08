import requests
from bs4 import BeautifulSoup

url = "https://notebookspro.ar/categoria-producto/notebooks/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

products = []
for product in soup.find_all("div", class_="box-text box-text-products text-center grid-style-2"):
    name = product.find("a",attrs={'text': True})
    products.append({"name": name})

# Print or further process the extracted product data
print(products)

