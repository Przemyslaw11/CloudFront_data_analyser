import pandas as pd
import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch
from app import show_edge_traffic

class TestShowEdgeTraffic(unittest.TestCase):
    
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'x_edge_location': ['edge1', 'edge2', 'edge3', 'edge4', 'edge5', 'edge1', 'edge1', 'edge2']}
        self.df = pd.DataFrame(data)
        
    def tearDown(self):
        plt.clf()
        
    def test_show_edge_traffic(self):
        # Test case 1: Verify if the function can generate a pie chart for the top N edge locations.
        with patch('matplotlib.pyplot.savefig') as mock_show:
            show_edge_traffic(self.df, top_n=2)
            self.assertEqual(mock_show.call_count, 1)
        
       # Test case 2: Verify if the function can handle an empty DataFrame.
        with patch('matplotlib.pyplot.savefig') as mock_show:
            data = {'x_edge_location': []}
            df = pd.DataFrame(data)
            with self.assertRaises(ValueError):
                show_edge_traffic(df, top_n=10)
            
        # Test case 3: Verify if the function can handle a DataFrame with no edge location data.
        with patch('matplotlib.pyplot.savefig') as mock_show:
            data = {'x_edge_location': []}
            df = pd.DataFrame(data)
            with self.assertRaises(ValueError):
                show_edge_traffic(df, top_n=10)
