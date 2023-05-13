import pandas as pd
import unittest
from unittest.mock import patch, MagicMock

# Import the function to test
from app import plot_country_traffic
from app import pie_plot_head

class TestPlotCountryTraffic(unittest.TestCase):
    
    def setUp(self):
        # Create a sample DataFrame for testing
        self.sample_df = pd.DataFrame({
            'c_ip': ['1.2.3.4', '5.6.7.8', '9.10.11.12', '13.14.15.16', '17.18.19.20'],
            'location': ['US', 'US', 'CA', 'CA', 'MX']
        })
     

    def test_missing_c_ip_column(self):
        # Test when the input DataFrame does not have the 'c_ip' column
        df_missing_c_ip = pd.DataFrame({'not_c_ip': ['1.2.3.4', '5.6.7.8']})
        with self.assertRaises(ValueError):
            plot_country_traffic(df_missing_c_ip)
    
