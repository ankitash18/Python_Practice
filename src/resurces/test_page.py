from unittest import  TestCase
from unittest.mock import patch
from  src.resurces.Page import PageRequest

class TestPageRequest(TestCase):
    def setup(self):
        self.page = PageRequest("http://google.com")

    def test_mak_request(self):
        with patch("requests.get") as mocked_get:
            response =  self.page.get()

