import pika
import schedule
import time
import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
import os


def movies_list_extract(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', attrs={'class': 'wikitable sortable'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    print("Creating Queue -")

    # read rabbitmq connection url from environment variable
    # amqp_url = os.environ['AMQP_URL']
    url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

    # connect to rabbitmq
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()

    print("Channel Declaration Done!")

    # declare a new queue
    # durable flag is set so that messages are retained
    # in the rabbitmq volume even between restarts
    channel.queue_declare(queue='crawl', durable=True)

    print("Queue Creating Done!")

    for row in rows:
        four_cols = row.find_all('td')
        itr = 1
        # getting list data awards,nomination etc.
        for col in four_cols:
            data_text = (col.text).replace('\n', ' ')
            movie_title = ''
            movie_link = ''
            movie_year = ''
            movie_nomination = ''
            movie_award = ''
            if itr % 4 == 1:
                movie_title = (data_text)
                if col.find('a'):
                    movie_link = (col.find('a').get('href'))
                else:
                    movie_link = (None)
            if itr % 4 == 2:
                movie_year = (data_text)
            if itr % 4 == 3:
                movie_award = (data_text)
            if itr % 4 == 0:
                movie_nomination = (data_text)
            itr += 1

            info = str(movie_title) + '-' + str(movie_link) + '-' + str(movie_year) + '-' + str(movie_award) + '-' + \
                   str(movie_nomination)

            print("Info printing- [%s]", info)
            channel.basic_publish(exchange='', routing_key='pages', body=info)
            print("Done=-=====================")


class Command(BaseCommand):
    help = 'WebScrapper'

    def handle(self, *args, **options):
        urls = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'  # persistent layers

        print("Connecting to RabbitMQ borker")

        movies_list_extract(urls)

        print("Done=====================")
