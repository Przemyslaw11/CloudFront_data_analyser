import unittest
import pandas as pd
import numpy as np
from app import find_unique_addresses

class TestFindUniqueAddresses(unittest.TestCase):
    
    def setUp(self):
        # create a sample DataFrame for testing
        self.df = pd.DataFrame({
            'c_ip': ['1.2.3.4', '1.2.3.4', '5.6.7.8', '9.10.11.12', '5.6.7.8']
        })
    
    def test_find_unique_addresses(self):
        expected = np.array(['1.2.3.4', '5.6.7.8', '9.10.11.12'])
        result = find_unique_addresses(self.df)
        self.assertCountEqual(expected, result)
        
    def test_find_unique_addresses_empty_dataframe(self):
        df = pd.DataFrame(columns=['c_ip'])
        expected = np.array([])
        result = find_unique_addresses(df)
        self.assertCountEqual(expected, result)
        
    def test_find_unique_addresses_missing_column(self):
        df = pd.DataFrame({
            'foo': ['bar', 'baz']
        })
        with self.assertRaises(KeyError):
            find_unique_addresses(df)
