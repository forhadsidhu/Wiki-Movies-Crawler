import pika
import requests
from bs4 import BeautifulSoup


def handler(ch, method, properties, url):
    print("starting : [%s]" % (url))
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    print("Extracted: %s" % soup.html.head.title)
    print('Done: [%s]' % url)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
print("Hadnling messages")

channel.basic_consume('pages', handler, auto_ack=True)
channel.start_consuming()
