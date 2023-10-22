from notion_client import Client
from pprint import pprint

notion_token = 'secret_nXAejSXmHqLfFz1TXxHgzGtFyfnwM6qR90H4GOZI6xU'
database_id = '46db718cda374bc7aa06b551dc18be9a'
notion_page_id = '1093311273cf47a894d7f4b9eeee992e'

def write_row(client, database_id, title):
    client.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            "properties": {
                "Title": {"title": [{"text": {"content": title}}]}
            }
        }
    )

def main():
    client = Client(auth=notion_token)
    write_row(client, database_id, "test")

if __name__ == '__main__':
    main()
          