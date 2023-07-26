import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

for i in range(2,20):
    url="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"+str(i)
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

    Product_Des=[]
    Product_price=[]
    Product_review=[]
    Product_rating=[]


    r=requests.get(url, headers=HEADERS)
    #print(r)

    soup=BeautifulSoup(r.text,"html.parser")
    #box=soup.find("div",class_="sg-col-inner")
    #print(soup)

    #Function for extract name of product
    name=soup.findAll("h2",class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
    for i in name:
        names=i.text
        Product_name.append(names)
    print(Product_name)

    #Function for extract prize of product
    price=soup.findAll("span",class_="a-price-whole")
    for i in price:
        prices=i.text
        Product_price.append(prices)
    print(Product_price)

    #Function for extract Rating of product
    rating=soup.findAll("span",class_="a-icon-alt")
    for i in rating:
        ratings=i.text
        Product_rating.append(ratings)
    print(Product_rating)

    #function for extracting review of product
    review=soup.findAll("span",class_="a-size-base s-underline-text")
    for i in review:
        reviews=i.text
        Product_review.append(reviews)
    print(Product_review)

# Find the maximum size among the lists
max_size = max(len(Product_name), len(Product_price), len(Product_review),len(Product_rating))


# Pad the lists to the maximum size with empty strings
Product_name += [''] * (max_size - len(Product_name))
Product_price += [None] * (max_size - len(Product_price))
Product_rating += [''] * (max_size - len(Product_rating))
Product_review +=  [''] * (max_size - len(Product_review))

# Save the data to a CSV file
with open('D:/Python code/Analyst/amazondata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Name', 'Product Price', 'Product rating',"Product Review"])
    for i in range(max_size):
        writer.writerow([Product_name[i], Product_price[i], Product_rating[i],Product_review[i]])



#create dataframe
#df=pd.DataFrame({
    #'ProductName' : Product_name,
    #'ProductPrice' : Product_price,
    #'ProductRating' : Product_review,
    #'ProductReview' : Product_rating
#})
#print(df)
#df['Product Name'].replace('', np.nan, inplace=True)
#df = df.dropna(subset=['Product Name'])
#to_csv=df.to_csv("D:/Python code/Analyst/amazondata.csv",header=True,index=False)



