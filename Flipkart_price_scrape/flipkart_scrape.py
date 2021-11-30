from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

products = []
prices = []
driver.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

for a in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}):
    name = a.find('div', attrs={'class':'_4rR01T'})
    price = a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})


    products.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({'Product Name':products, 'Price':prices})

df.to_csv('products.csv', index=False, encoding='utf-8')
    
