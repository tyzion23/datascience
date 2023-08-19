#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Wikipedia'

request = requests.get(url)
html_content = request.content

soup = BeautifulSoup(html_content, 'html.parser')

h_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

h_texts = [tag.get_text() for tag in h_tags]

data = {'Headers': h_texts}
df = pd.DataFrame(data)

df.head()


# In[ ]:





# In[ ]:





# In[5]:


def scrape_and_create_dataframe(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='table')
    data = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        rank = cols[0].text.strip()
        player = cols[1].text.strip()
        country = cols[2].text.strip()
        rating = cols[3].text.strip()
        data.append([rank, player, country, rating])

    columns = ['Rank', 'Player', 'Country', 'Rating']
    df = pd.DataFrame(data, columns=columns)
    return df

base_url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


top_10_teams_df = scrape_and_create_dataframe(base_url, headers)
top_10_batsmen_df = scrape_and_create_dataframe('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting', headers)
top_10_bowlers_df = scrape_and_create_dataframe('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling', headers)

print("Top 10 ODI Teams:")
print(top_10_teams_df)

print("\nTop 10 ODI Batsmen:")
print(top_10_batsmen_df)

print("\nTop 10 ODI Bowlers:")
print(top_10_bowlers_df)


# In[8]:


def scrape_and_create_dataframe(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='table')
    data = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        rank = cols[0].text.strip()
        player = cols[1].text.strip()
        country = cols[2].text.strip()
        rating = cols[3].text.strip()
        data.append([rank, player, country, rating])

    columns = ['Rank', 'Player', 'Country', 'Rating']
    df = pd.DataFrame(data, columns=columns)
    return df

base_url = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


top_10_teams_df = scrape_and_create_dataframe(base_url, headers)
top_10_batting_df = scrape_and_create_dataframe('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting', headers)
top_10_all_rounder_df = scrape_and_create_dataframe('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder', headers)

print("Top 10 Women's ODI Teams:")
print(top_10_teams_df)

print("\nTop 10 Women's ODI Batting Players:")
print(top_10_batting_df)

print("\nTop 10 Women's ODI All-rounders:")
print(top_10_all_rounder_df)


# In[ ]:





# In[8]:


url = 'https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

articles = soup.find_all('div', class_='pod-listing-header')

titles = []
authors_list = []
dates = []
paper_urls = []


for group in articles:
    title = group.find('a', class_='pod-listing-title').text.strip()
    authors = group.find('span', class_='pod-listing-authors').text.strip()
    published_date = group.find('span', class_='pod-listing-pub-date').text.strip()
    paper_url = 'https://www.journals.elsevier.com' + group.find('a', class_='pod-listing-title')['href']
    
    titles.append(title)
    authors_list.append(authors)
    dates.append(published_date)
    paper_urls.append(paper_url)

data = {'Paper Title': titles, 'Authors': authors_list, 'Published Date': dates, 'Paper URL': paper_urls}
df = pd.DataFrame(data)
df


# In[15]:


url = 'https://www.dineout.co.in/delhi-restaurants'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

restaurant_space = soup.find_all('div', class_='restaurantList')

restaurant_names = []
cuisines = []
locations = []
ratings = []
image_urls = []

for items in restaurant_space:
    restaurant_name = items.find('a', class_='restaurantName').text.strip()
    cuisine = items.find('span', class_='double-line-ellipsis').text.strip()
    location = items.find('div', class_='restntLocality').text.strip()
    rating = items.find('span', class_='double-line-ellipsis-rating').text.strip()
    image_url = items.find('img', class_='js-restaurant-logo')['src']
    
    restaurant_names.append(restaurant_name)
    cuisines.append(cuisine)
    locations.append(location)
    ratings.append(rating)
    image_urls.append(image_url)

data = {
    'Restaurant Name': restaurant_names,
    'Cuisine': cuisines,
    'Location': locations,
    'Ratings': ratings,
    'Image URL': image_urls
}
df = pd.DataFrame(data)

df


# In[ ]:




