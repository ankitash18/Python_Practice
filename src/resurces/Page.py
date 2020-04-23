import requests

class PageRequest:
    def __init__(self,url):
        self.url = url

    def get(self):
        return requests.get(self.url).content
    