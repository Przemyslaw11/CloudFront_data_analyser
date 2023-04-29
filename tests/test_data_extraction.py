import unittest
import pandas as pd
from app import extract_data

class TestDataExtraction(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'date': ['2022-01-01', '2022-01-02'],
            'time': ['00:00:00', '01:00:00'],
            'x_edge_location': ['edge1', 'edge2'],
            'c_ip': ['127.0.0.1', '127.0.0.2'],
            'cs_method': ['GET', 'POST'],
            'sc_status': [200, 404],
            'cs_uri_stem': ['/index.html', '/page.html']
        })

    def test_extract_data(self):
        expected_output = pd.DataFrame({
            'datetime': pd.to_datetime(['2022-01-01 00:00:00', '2022-01-02 01:00:00']),
            'x_edge_location': ['edge1', 'edge2'],
            'c_ip': ['127.0.0.1', '127.0.0.2'],
            'cs_method': ['GET', 'POST'],
            'sc_status': [200, 404],
            'cs_uri_stem': ['/index.html', '/page.html']
        })
        output = extract_data(self.df)
        pd.testing.assert_frame_equal(output, expected_output)