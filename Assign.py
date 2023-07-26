from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv

# add your user agent
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

# The webpage URL
URL = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

# HTTP Request
r = requests.get(URL, headers=HEADERS)

# Soup Object containing all data
soup = BeautifulSoup(r.text, "html.parser")

# Fetch links as List of Tag Objects
links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

 #store the links
links_list = []

# Loop for extracting links from Tag Objects
for link in links:
    links_list.append(link.get('href'))

d = {"title": [], "price": [], "rating": [], "reviews": []}


# Function to extract Product Title
def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("h2",class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')

        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span",class_='a-price')

    except AttributeError:

       # try:
            # If there is some deal price
          #  price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        #except:
            price = ""

    return price


# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("div",class_= 'a-row a-size-small')

    except AttributeError:
       try:
           rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
       except:
           rating = ""

    return rating


# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style")

    except AttributeError:
        review_count = ""

    return review_count






# Loop for extracting product details from each link
for link in links_list:
    new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

    new_soup = BeautifulSoup(new_webpage.content, "html.parser")

    # Function calls to display all necessary product information
    d['title'].append(get_title(soup))
    d['price'].append(get_price(soup))
    d['rating'].append(get_rating(soup))
    d['reviews'].append(get_review_count(soup))
    #d['availability'].append(get_availability(new_soup))

#amazon_df = pd.DataFrame.from_dict(d)
#amazon_df['title'].replace('', np.nan, inplace=True)
#amazon_df = amazon_df.dropna(subset=['title'])
#amazon_df.to_csv("D:/Python code/Analyst/amazon_data.csv", header=True, index=False)


# Find the maximum size among the lists
max_size = max(len(get_title()), len(get_price()), len(get_rating()),len(get_review_count()))

# Pad the lists to the maximum size with empty strings
title += [''] * (max_size - len(names))
ages += [None] * (max_size - len(ages))
occupations += [''] * (max_size - len(occupations))

# Save the data to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'Occupation'])
    for i in range(max_size):
        writer.writerow([names[i], ages[i], occupations[i]])


