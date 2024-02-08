import requests
import json

from bs4 import BeautifulSoup

url = "https://pronotebooks.com.ar/tienda/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

products = []

#for div_element in soup.find_all("div", class_="product-small box"):
#    span_element = div_element.find("span", class_="gtm4wp_productdata")
#    name = span_element.get("data-gtm4wp_product_name")
#    price = span_element.get("data-gtm4wp_product_price")
#    product_url = span_element.get("data-gtm4wp_product_url")
#    products.append({"name": name,"price": price, "product" : product_url})

# Print or further process the extracted product data
#data = json.loads(products)



# Find all div elements with class 'product-small box'
product_boxes = soup.find_all('div', class_='product-small box')

# Iterate over each product box
for box in product_boxes:
    # Find the img tag within the current product box
    img_tag = box.find('img', class_='attachment-woocommerce_thumbnail')
    if img_tag:
        # Extract the src attribute
        #img_src = img_tag['src']
        img_src = img_tag.get("data-src")
        # Find the a element within the current product box
        a_tag = img_tag.parent
        # Extract the aria-label attribute
        aria_label = a_tag['aria-label'] if 'aria-label' in a_tag.attrs else 'No Aria Label Found'
        print("Image Source:", img_src)
        print("Aria Label:", aria_label)
        print()

#print(products)

