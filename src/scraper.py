import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import concurrent.futures


def movie_desc_extract(movie_url):
    movie_info_dict = {}
    if movie_url is None:
        return db_rows.update({movie_url: movie_info_dict})

    movie_content = requests.get('https://en.wikipedia.org/' + movie_url).text
    soup = bs(movie_content, 'html.parser')
    table = soup.find('table', attrs={'class': 'infobox vevent'})
    if not table.find('tbody'):
        return db_rows.update({movie_url: movie_info_dict})

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        if row.find('th') and row.find('td'):
            key = row.find('th').text.replace('\n', ' ')
            value = row.find('td').text.replace('\n', ' ')
            db_cols.add(key)
            movie_info_dict.update({key: value})

            # print(row.find('th').text, row.find('td').text)

    return db_rows.update({movie_url: movie_info_dict})


def movies_list_extract(url):
    content = requests.get(url).text
    soup = bs(content, 'html.parser')
    table = soup.find('table', attrs={'class': 'wikitable sortable'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    movie_titles = []
    movie_links = []
    movie_years = []
    movie_awards = []
    movie_nominations = []

    for row in rows:
        four_cols = row.find_all('td')
        itr = 1
        # getting list data awards,nomination etc.
        for col in four_cols:
            data_text = (col.text).replace('\n', ' ')
            if itr % 4 == 1:
                movie_titles.append(data_text)
                if col.find('a'):
                    movie_links.append(col.find('a').get('href'))
                else:
                    movie_links.append(None)
            if itr % 4 == 2:
                movie_years.append(data_text)
            if itr % 4 == 3:
                movie_awards.append(data_text)
            if itr % 4 == 0:
                movie_nominations.append(data_text)
            itr += 1

    return movie_titles, movie_links, movie_years, movie_awards, movie_nominations


if __name__ == '__main__':

    """
    PHASE 1
    Scraping Data
    """
    url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
    movie_titles, movie_urls, movie_years, movie_awards, movie_nominations = movies_list_extract(url)

    db_cols = set()
    db_rows = {}
    db = []

    # use concurrency for fast execution
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(movie_desc_extract, movie_urls)
