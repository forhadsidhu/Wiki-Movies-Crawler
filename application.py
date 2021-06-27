import argparse
from subprocess import call

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--id', choices=['parse','serve'], default='parse')

    args = parser.parse_args()

    # Variable definitions
    if args.id == "parse":
        call(['python', 'src/scraper.py'])
        print("Web Scrapping Done!")
    if args.id == "serve":
        call(['python', 'movie_api/manage.py','runserver'])
