import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Sending get request to server
response = requests.get(
    "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response.status_code)  # The response must be always 200
soup = BeautifulSoup(response.content, "html.parser")

# Creating lists for storing data
product_title = []
price_list = []
reviews_list = []

# getting data from websites (response)

names = soup.find_all("div", class_='_4rR01T')
for i in range(0, len(names)):
    product_title.append(names[i].get_text())

price = soup.find_all("div", class_="_30jeq3 _1_WHN1")
for i in range(0, len(price)):
    price_list.append(price[i].get_text())

reviews = soup.find_all("span", class_="_2_R_DZ")
for i in range(0, len(reviews)):
    reviews_list.append(reviews[i].get_text())

# Creating a CSV file to store data in readable format
file = pd.DataFrame({'Product name': product_title,
                     'Price': price_list,
                     'Reviews': reviews_list})
file.to_csv('Flipkart_data3.csv')
