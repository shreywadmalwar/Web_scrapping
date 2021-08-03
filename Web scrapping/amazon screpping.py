import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.amazon.in/s?k=iphone&ref=nb_sb_noss_2")
# print(response.status_code)
soap = BeautifulSoup(response.content, "html.parser")

product_title = []
price_list = []
reviews_list = []

names = soap.find_all("span", class_='a-size-medium a-color-base a-text-normal')
for i in range(0, len(names)):
    product_title.append(names[i].get_text())
print(product_title)

price = soap.find_all("span", class_="a-price-whole")
for i in range(0, len(price)):
    price_list.append(price[i].get_text())
print(price_list)

reviews = soap.find_all("span", class_="a-size-base")
for i in range(0,len(reviews)):
    reviews_list.append(price[i].get_text())
print(reviews_list)
