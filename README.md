# notion_task

## Description
Given a csv file with a file containing a table with three rows: book name, member name, and book rating, this program will update a Notion database with one row for each book that got at least one rating. Each row in the database will have:

- Book name (normalized for extra whitespace and capitalization)
- Average rating from all members
- Number of members who rated the book 5 stars - which we call favoriting

## Usage
Run the following command line:
```
python3 main.py ratings.csv
```
where the first argument is the csv file what you would like to read.

## My Learning Process
1. Create new integration following: https://www.notion.com/my-integrations 
2. Create database page in Notion
3. Following tutorial to read from Notion page - want to learn how to work with API
4. Following a second tutorial to write to Notion page
- Started with just Title - which is text
- Then wrote to number columns as well - read json output to figure out structure of number column
5. Create function to normalize strings
6. Create function to delete extraneous rows
- Same name and book title → take the last instance
- Execution: use a hashmap
7. Create a function to count the number of favorites
8. Add rows to database
9. Making unit test cases

## Approach
- Reading CSV file: the user inputs csv file in command line argument
  - Other approaches: I considered having the csv file define in main.py but wanted to give user flexibility in the name of the file they are reading so decided to make it an argument.
- Notion SDK: program uses [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)
  - Other approaches: At first I considered writing the code without any SDK at all, but then I realized that an SDK is a helpful resource that makes my code easier to read and easier to write, so I used the SDK recommended by the Notion Task Assignment page.
- Hashmap: I used a hashmap to keep track of book-person reviews.
  - Tradeoffs: Space usage is high because I am storing a tuple as the key for every book-person review.
  - Reason: I used a hashmap because of quick runtime, O(1) look-up. I can also update quickly and ensure that only the last book-person review is kept.
- Methods delete_rows, count_favorites, and find_avg
  - I run delete_rows first so that we have a hashmap that contains one instance of every book-person pair.
  - Then, count_favorites and find_avg will output the right answer because we do not have any duplicate keys in our hashmap.
  - Other approaches: I was going to include these functions in my write_data method, but I decided to abstract out the functions for readability.

## Technical Challenges
- Learning to work with Notion API
  - Structure of content to write row. How to format "properties."
     - I was able to learn by following tutorials online and running my own tests.
     - I was able to understand that the structure is different for different types, like text and numbers have different JSON structures.
  - Error with invalid Notion ID or invalid database ID
     - I realize there are multiple strings of letters and characters in URL links for notion pages and databases, so initially I was struggling to get the correct ID values. I was able to find the correct IDs by rewatching tutorials and testing the lengths to make sure I am grabbing a string of length 32.
- Writing unit test cases
   - It was difficult to know what to include in each test case but I worked with the principal that each test case should be specialized to testing one function. So instead of reading from an csv file in every test case, I only read from an csv file in one test case where I am testing that the reading function works.

## Resources
https://www.youtube.com/watch?v=M1gu9MDucMA&ab_channel=PatrickLoeber
https://www.youtube.com/watch?v=JoCdhP0OkAU&ab_channel=IndyDevDan
https://realpython.com/python-testing/#testing-your-code
https://developers.notion.com/page/examples
