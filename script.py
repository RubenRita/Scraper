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
print(first_name)
print(first_year)