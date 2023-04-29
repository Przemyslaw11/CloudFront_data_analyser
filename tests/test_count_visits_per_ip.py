import pandas as pd
import unittest
from app import count_visits_per_ip

class TestCountVisitsPerIP(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'c_ip': ['10.0.0.1', '10.0.0.2', '10.0.0.1', '10.0.0.3'],
            'page': ['/home', '/about', '/home', '/contact']
        })

    def test_without_ip_address(self):
        expected_result = pd.Series({'10.0.0.1': 2, '10.0.0.2': 1, '10.0.0.3': 1})
        result = count_visits_per_ip(self.df)
        self.assertTrue(expected_result.equals(result))

    def test_with_existing_ip_address(self):
        expected_result = 2
        result = count_visits_per_ip(self.df, '10.0.0.1')
        self.assertEqual(expected_result, result)

    def test_with_nonexisting_ip_address(self):
        expected_result = 0
        result = count_visits_per_ip(self.df, '10.0.0.4')
        self.assertEqual(expected_result, result)
