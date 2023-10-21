import requests

NOTION_TOKEN = "secret_nXAejSXmHqLfFz1TXxHgzGtFyfnwM6qR90H4GOZI6xU"
DATABASE_ID = "0bec57ad60ef493b8427f98a20b53a36"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    # print(res.status_code)
    return res

def get_pages(num_pages=None):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    import json
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    results = data["results"]
    return results

pages = get_pages()

for page in pages:
    page_id = page["id"]
    props = page["properties"]
    book_title = props["Book Title"]["title"][0]["text"]["content"]
    print(book_title)
