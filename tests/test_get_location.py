import unittest
from unittest.mock import patch
import json
from io import BytesIO
from app import get_location

class TestGetLocation(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_get_location_with_country(self, mock_urlopen):
        ipwhois = {'country': 'Canada'}
        mock_urlopen.return_value = BytesIO(json.dumps(ipwhois).encode())
        
        self.assertEqual(get_location('8.8.8.8'), 'Canada')

    @patch('urllib.request.urlopen')
    def test_get_location_without_country(self, mock_urlopen):
        ipwhois = {}
        mock_urlopen.return_value = BytesIO(json.dumps(ipwhois).encode())
        
        self.assertEqual(get_location('8.8.8.8'), 'Unknown')




