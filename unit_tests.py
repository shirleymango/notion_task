import csv
import unittest

from main import count_favorites
from main import delete_rows
from main import find_avg

class TestSum(unittest.TestCase):

    # Should correctly count number of 5 star ratings for each book
    def test_count_favorites(self):
        book_person_map = {('Primed to Perform', 'Alma W'): 5.0, ('Primed to Perform', 'Jordan S'): 3.0, ('Primed to Perform', 'David B'): 3.5, ('The Tangled Web', 'Eva Z'): 3.0, ('The Art of Computer Programming', 'Zach S'): 3.5, ('The Art of Computer Programming', 'Alma W'): 5.0}
        correct_book_favorites_map = {'Primed to Perform': 1, 'The Tangled Web': 0, 'The Art of Computer Programming': 1}
        self.assertEqual(count_favorites(book_person_map), correct_book_favorites_map, "Should be {'Primed to Perform': 1, 'The Tangled Web': 0, 'The Art of Computer Programming': 1}")
    
    # Should only take last input by user on book
    def test_delete_rows(self):
        file = open('unit_test_repeats.csv')
        csvreader = csv.reader(file)
        book_person_map = delete_rows(csvreader)
        file.close()
        correct_book_person_map = {('Primed to Perform', 'Alma W'): 5.0, ('Primed to Perform', 'Jordan S'): 4.0, ('The Tangled Web', 'Eva Z'): 2.5, ('The Art of Computer Programming', 'Zach S'): 3.5}
        self.assertEqual(book_person_map, correct_book_person_map, "Should be {('Primed to Perform', 'Alma W'): 5.0, ('Primed to Perform', 'Jordan S'): 4.0, ('The Tangled Web', 'Eva Z'): 2.5, ('The Art of Computer Programming', 'Zach S'): 3.5}")
    
    # Should calculate book averages to nearest one place after decimal
    def test_avg(self):
        book_person_map = {('Primed to Perform', 'Alma W'): 5.0, ('Primed to Perform', 'Jordan S'): 3.0, ('Primed to Perform', 'Eva Z'): 3.0, ('The Art of Computer Programming', 'Zach S'): 3.5, ('The Art of Computer Programming', 'Jordan S'): 4.0}
        book_avg_map = find_avg(book_person_map)
        correct_book_avg_map = {'Primed to Perform': 3.7, 'The Art of Computer Programming': 3.8}
        self.assertEqual(book_avg_map, correct_book_avg_map, "Should be {'Primed to Perform': 3.7, 'The Art of Computer Programming': 3.8}")
    
    def test_string_normalization(self):
        file = open('unit_test_string_normalization.csv')
        csvreader = csv.reader(file)
        book_person_map = delete_rows(csvreader)
        correct_book_person_map = {('Extreme Ownership', 'Alex M'): 1.0, ('Design Patterns: Elements of Reusable Object-Oriented Software', 'Alex M'): 0.5, ('Designing Data-Intensive Applications', 'Eva Z'): 0.5, ("Computer Systems: A Programmer's Perspective", 'Gabby H'): 0.5, ('The Art of Computer Programming', 'Zach S'): 3.5, ("Gödel's Proof", 'Gabriel B'): 0.5, ('Refactoring', 'Sherly T'): 0.5}
        self.assertEqual(book_person_map, correct_book_person_map, "Error in string normalization")
        file.close()
        
if __name__ == '__main__':
    unittest.main()