#How to scrape websites with Python and BeautifulSoup
import pandas as pd
import requests

from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from warnings import warn
from IPython.core.display import clear_output
from time import time

'''
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

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
'''

# Scraping web with lot of pages
pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2018)]	
headers = {"Accept-Language": "en-US, en;q=0.5"}


# List to store scraped data 
names = [] 
years = []
imdb_ratings = []
metascores = []
votes = []

# Preparing the monitoring of the loop
start_time = time()
requests = 0


# For every year in the interval 2000-2017
for year_url in years_url:

    # For every page in the interval 1-4
    for page in pages:

        # Make a get request
        response = get('http://www.imdb.com/search/title?release_date=' + year_url + 
        '&sort=num_votes,desc&page=' + page, headers = headers)

        # Pause the loop
        sleep(randint(8,15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        #print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)

        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected 
        if requests > 72:
            warn('Number of requests was greater than expected.')  
            break 

        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from a single page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

			
	# For every movie of these 50
        for container in mv_containers:
            # If the movie has a Metascore, then:
            if container.find('div', class_ = 'ratings-metascore') is not None:

                # Scrape the name
                name = container.h3.a.text
                names.append(name)

                # Scrape the year 
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)

                # Scrape the IMDB rating
                imdb = float(container.strong.text)
                imdb_ratings.append(imdb)

                # Scrape the Metascore
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))

                # Scrape the number of votes
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))
				
				
test_df = pd.DataFrame({'movie':names,
						'year':years,'imdb':imdb_ratings,'votes':votes,
						'metascore':metascores})
print(test_df.info())								
		


	
