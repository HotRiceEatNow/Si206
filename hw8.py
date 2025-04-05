import sqlite3
import matplotlib.pyplot as plt
import unittest
import os
import shutil
import re

def fix_charli_xcx_name(db):
    """
    Updates specifically "Charli XCX" to "Charli xcx" if it exists.
    
    Args:
        db (str): Path to the SQLite database file
    """
    pass

def get_top_songs(db):
    """
    Returns the top 5 most-played songs and creates a bar chart.
    
    Args:
        db (str): Path to the SQLite database file
    Returns:
        dict: Dictionary with song names as keys and play counts as values
    """
    pass

def get_top_artists(db):
    """
    Returns the top 5 most-played artists.
    
    Args:
        db (str): Path to the SQLite database file
    Returns:
        dict: Dictionary with artist names as keys and play counts as values
    """
    pass


def find_featured_artists(db):
    """
    Finds all songs where Charli xcx has featured artists and returns a list of unique collaborators.
    
    Args:
        db (str): Path to the SQLite database file
    Returns:
        list: Sorted list of unique featured artists from Charli xcx's songs
    """
    pass


class TestSpotifyWrapped(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Path to the original and fixed databases
        cls.original_db = "2025_listening_data.db"
        cls.fixed_db = "fixed_listening_data.db"

        if os.path.exists(cls.fixed_db):
            os.remove(cls.fixed_db)

        if os.path.exists('top_songs.png'):
            os.remove('top_songs.png')
        
        # Create a fixed version of the database for other tests
        shutil.copy2(cls.original_db, cls.fixed_db)
        # Fix the Charli XCX name in this copy
        fix_charli_xcx_name(cls.fixed_db)

    def setUp(self):
        # Create fresh connections for each test
        self.original_conn = sqlite3.connect(self.original_db)
        self.fixed_conn = sqlite3.connect(self.fixed_db)
        self.original_cursor = self.original_conn.cursor()
        self.fixed_cursor = self.fixed_conn.cursor()

    def tearDown(self):
        # Close connections after each test
        self.original_conn.close()
        self.fixed_conn.close()
                

    def test_fix_charli_xcx_name(self):
        # Check initial state in original database
        self.original_cursor.execute("SELECT COUNT(*) FROM artists WHERE name LIKE 'Charli%xcx' OR name LIKE 'Charli%XCX'")
        initial_count = self.original_cursor.fetchone()[0]
        self.assertGreater(initial_count, 1, "Should have multiple Charli XCX entries initially")
        
        # Check final state in fixed database
        self.fixed_cursor.execute("SELECT COUNT(*) FROM artists WHERE name LIKE 'Charli%xcx' OR name LIKE 'Charli%XCX'")
        final_count = self.fixed_cursor.fetchone()[0]
        self.assertEqual(final_count, 1, "Should have only one Charli xcx entry after fix")
        
        # Check if the name is standardized to "Charli xcx"
        self.fixed_cursor.execute("SELECT name FROM artists WHERE name LIKE 'Charli%xcx' OR name LIKE 'Charli%XCX'")
        name = self.fixed_cursor.fetchone()[0]
        self.assertEqual(name, 'Charli xcx')
        
    def test_get_top_songs(self):
        top_songs = get_top_songs(self.fixed_db)
        
        # Check if returns exactly 5 songs
        self.assertEqual(len(top_songs), 5)
        
        # Verify expected top songs
        expected_songs = {
            'Abracadabra': 56,
            'B2b': 49,
            'eat, sleep, slay, 🔁': 41,
            'materiaL hor$e': 40,
            'Revolving Door': 39
        }
        
        self.assertEqual(top_songs, expected_songs)
        
        # Check if visualization file was created
        self.assertTrue(os.path.exists('top_songs.png'))
        
        # Check if the values are in descending order
        plays = list(top_songs.values())
        self.assertEqual(plays, sorted(plays, reverse=True))

    def test_get_top_artists(self):
        top_artists = get_top_artists(self.fixed_db)
        
        # Verify expected top artists
        expected_artists = {
            'Bad Bunny': 236,
            'Lady Gaga': 225,
            'Tate McRae': 224,
            'FKA twigs': 186,
            'Charli xcx': 181
        }
        
        self.assertEqual(top_artists, expected_artists)
        
        # Check if values are in descending order
        plays = list(top_artists.values())
        self.assertEqual(plays, sorted(plays, reverse=True))

    def test_find_featured_artists(self):
        featured = find_featured_artists(self.fixed_db)
        
        # Test that it returns a list
        self.assertIsInstance(featured, list)
        
        # Test for some known featured artists
        expected_artists = [
            'A. G. Cook',
            'Troye Sivan',
            'Caroline Polachek',
            'Lizzo'
        ]
        
        for artist in expected_artists:
            self.assertIn(artist, featured)
        
        # Test that all entries are strings and non-empty
        for artist in featured:
            self.assertIsInstance(artist, str)
            self.assertGreater(len(artist), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)

