#How to scrape websites with Python and BeautifulSoup
import pandas as pd
import requests

from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint


url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
headers = {"Accept-Language": "en-US, en;q=0.5"}
response = requests.get(url, headers)


html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')

print(type(movie_containers))
print(len(movie_containers))

first_movie = movie_containers[0]
first_name = first_movie.h3.a.text
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year = first_year.text
first_imdb = float(first_movie.strong.text)

first_mscore = first_movie.find('span', class_ = 'metascore favorable')
first_mscore = int(first_mscore.text)

#number of votes
first_votes = first_movie.find('span', attrs = {'name':'nv'})
first_votes = int (first_votes['data-value'])




print(first_name)
print(first_year)
print(first_imdb)
print(first_mscore)
print('number of votes:',first_votes) 

# List to store scraped data 
names = [] 
years = []
imdb_rating = []
metascore = []
votes = []

# Extract data from individual  movie containers

for container in movie_containers:
# if the movie has metascore, then extract
	if container.find('div', class_ = 'ratings-metascore') is not None:
		#Extract the name
		name = container.h3.a.text
		names.append(name)
		
		#Extract year
		year = container.h3.find('span', class_ = 'lister-item-year').text
		years.append(year)
		
		#Extract imdb rating 
		imdb = float(container.strong.text)
		imdb_rating.append(imdb)
		
		#Extract Metascore 
		m_score = container.find('span', class_ = 'metascore').text
		metascore.append(int(m_score))
		
		#Extract number of votes
		vote = container.find('span', attrs = {'name':'nv'})['data-value']
		votes.append(int(vote))
		
test_df = pd.DataFrame({'movie':names,
						'year':years,'imdb':imdb_rating,'votes':votes,
						'metascore':metascore})
print(test_df.info())								
		
# Scraping web with lot of pages
pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2018)]	

	
