import csv

from notion_client import Client
from pprint import pprint

notion_token = 'secret_nXAejSXmHqLfFz1TXxHgzGtFyfnwM6qR90H4GOZI6xU'
database_id = '46db718cda374bc7aa06b551dc18be9a'
notion_page_id = '1093311273cf47a894d7f4b9eeee992e'

# Input: string
# Returns string with capital first character and lower case for all other characters
def capitalize_string(word):
    return str(word[0]).upper() + word[1:]

# Input: string
# Returns normalized string with fixed capitalization and no extra spacing
def normalize_name(name):
    normalized = ""
    prepositions_and_articles = ["of", "to", "the", "a", "and"]
    punctuation = [':', '!', '?']
    words = name.split()
    for word in words:
        word = word.lower()
        # edge case: there may be extra spaces in original string so there will be empty strings after split
        if word == "":
            continue
        # edge case: first word should not have preceding space
        if not normalized == "":
            # all other words will have preceding space
            normalized += " "
        # edge case: hyphenated words should have capitalization after hyphen
        if len(word.split("-")) > 1:
            subwords = word.split("-")
            normalized += capitalize_string(subwords[0]) + "-" + capitalize_string(subwords[1])
            continue
        # edge case: words like 'of' and 'the' should not be capitalized unless at the start or after punctuation
        if word in prepositions_and_articles and not normalized == "" and not normalized[len(normalized)-2] in punctuation:
            normalized += word
        # all other words will be capitalized
        else:
            normalized += capitalize_string(word)
    return normalized

# Input: reader to csv containing rows of book title, person name, rating of book
# Returns a mapping of book title and person name to the person's rating of the book
# Deletes extraneous rows so that only the last rating by a person is remembered
def delete_rows(csvreader):
    book_person_map = {}
    for row in csvreader:
        book_person_pair = (normalize_name(row[0]), normalize_name(row[1]))
        book_person_map[book_person_pair] = float(row[2])
    return book_person_map

# Input: mapping of book title and person name to the person's rating of the book
# Returns mapping of book title to number of people who gave the book a 5 star rating
def count_favorites(book_person_map):
    book_favorites_map = {}
    for key in book_person_map:
        book = key[0]
        if book in book_favorites_map:
            if book_person_map[key] == 5: book_favorites_map[book] += 1
        else:
            if book_person_map[key] == 5: book_favorites_map[book] = 1
            else: book_favorites_map[book] = 0
    return book_favorites_map

# Input: client, database id, data to be added to database row
# Returns no output but writes to one row to Notion database
def write_row(client, database_id, title, rating, favorites):
    client.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            "properties": {
                "Title": {"title": [{"text": {"content": title}}]},
                "Rating": {"number": round(rating, 1)},
                "Favorites": {"number": favorites}
            }
        }
    )

# Input: client, mapping of book title and person name to the person's rating of the book, and mapping of book to number of favorites
# Returns no output but writes formatted data to Notion database
def write_data(client, book_person_map, book_favorites_map):
    book_rating_map = {}
    book_count_map = {}
    for key in book_person_map:
        book = key[0]
        if book in book_rating_map: 
            book_rating_map[book] += book_person_map[key]
            book_count_map[book] += 1
        else: 
            book_rating_map[book] = book_person_map[key]
            book_count_map[book] = 1
    for book in book_rating_map:
        row = [book, book_rating_map[book]/book_count_map[book], book_favorites_map[book]]
        write_row(client, database_id, row[0], row[1], row[2])

def main():
    client = Client(auth=notion_token)
    file = open('ratings.csv')
    csvreader = csv.reader(file)
    book_person_map = delete_rows(csvreader)
    book_favorites_map = count_favorites(book_person_map)
    write_data(client, book_person_map, book_favorites_map)
    file.close()

if __name__ == '__main__':
    main()