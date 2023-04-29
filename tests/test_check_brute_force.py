import pandas as pd
import unittest
from datetime import datetime, timedelta
from app import check_brute_force

class TestCheckBruteForce(unittest.TestCase):
    def setUp(self):
        # Create test data for the DataFrame
        self.df = pd.DataFrame({'cs_uri_stem': ['/', '/about', '/contact', '/about', '/'],
                                'datetime': [datetime(2023, 4, 29, 12, 0, 0),
                                             datetime(2023, 4, 29, 12, 2, 0),
                                             datetime(2023, 4, 29, 12, 3, 0),
                                             datetime(2023, 4, 29, 12, 4, 0),
                                             datetime(2023, 4, 29, 12, 6, 0)]})
    
    def test_check_brute_force(self):
        # Test with default threshold
        result = check_brute_force(self.df)
        expected = []
        self.assertEqual(result, expected)

        
    