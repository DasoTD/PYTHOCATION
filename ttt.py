import unittest
from unittest.mock import patch
from tt import make_request

class TestMakeRequest(unittest.TestCase):
    @patch('module_to_test.requests')
    def test_make_request(self, mock_requests):
        mock_response = mock_requests.get.return_value
        mock_response.status_code = 200

        status_code = make_request()

        self.assertEqual(status_code, 200)
        mock_requests.get.assert_called_once_with('https://google.com')
    
    test_make_request()