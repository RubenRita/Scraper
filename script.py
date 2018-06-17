#How to scrape websites with Python and BeautifulSoup

from requests import get
from bs4 import BeautifulSoup


url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)


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
