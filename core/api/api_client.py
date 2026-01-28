import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)