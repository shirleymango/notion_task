import csv

from notion_client import Client
from pprint import pprint

notion_token = 'secret_nXAejSXmHqLfFz1TXxHgzGtFyfnwM6qR90H4GOZI6xU'
database_id = '46db718cda374bc7aa06b551dc18be9a'
notion_page_id = '1093311273cf47a894d7f4b9eeee992e'

def normalize_title(title):
    normalized = ""
    words = title.split()
    for word in words:
        word = word.lower()
        if word == "":
            continue
        if not normalized == "":
            normalized += " "
        if word == "of" or word == "to" or (word == "the" and not normalized == ""):
            normalized += word
        else:
            normalized += str(word[0]).upper() + word[1:]
    return normalized

def write_row(client, database_id, title, rating, favorites):
    client.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            "properties": {
                "Title": {"title": [{"text": {"content": title}}]},
                "Rating": {"number": rating},
                "Favorites": {"number": favorites}
            }
        }
    )

def main():
    client = Client(auth=notion_token)
    file = open('ratings2.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
        write_row(client, database_id, row[0], float(row[2]), 1)
    file.close()

if __name__ == '__main__':
    main()
          