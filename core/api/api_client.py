import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    
    def post(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=json)
    
    def put(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, json=json)
    
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url)