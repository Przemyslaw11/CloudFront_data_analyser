import pandas as pd
import unittest
from app import get_freq_endpoints

class TestGetFreqEndpoints(unittest.TestCase):

    def setUp(self):
        # create some sample dataframes for testing
        self.df1 = pd.DataFrame({
            'sc_status': [200, 200, 404, 404, 500],
            'cs_method': ['GET', 'POST', 'GET', 'POST', 'GET'],
            'cs_uri_stem': ['/foo', '/bar', '/foo', '/bar', '/foo']
        })
        self.df2 = pd.DataFrame({
            'sc_status': [200, 200, 404, 404, 500],
            'cs_method': ['GET', 'POST', 'GET', 'POST', 'GET'],
            'cs_uri_stem': ['/foo', '/bar', '/foo', '/bar', '/foo']
        })

    def test_empty_dataframe(self):
        # test the function with an empty dataframe
        self.assertTrue(get_freq_endpoints(pd.DataFrame()).empty)
