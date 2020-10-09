import requests

class Proton:
    BASE_URLS = [
        ''
    def __init__(self, url='https://api.proton-graph.cloud/public/static-references/api', token=None):
        self.url = url
        self.static_reference = 'https://api.proton-graph.cloud/public/static-references/api'
        self.location_base_url = 'https://api.proton-graph.cloud/public/locations/api'   
        self.headers = {
            'Ocp-Apim-Subscription-Key': token
        }

    def get(self, url):
        response = requests.get(url, headers=self.headers)
        return response


class Location(Proton):
    """
        Reference: https://portal.proton-graph.cloud/docs/locations-journey
    """
    def __init__(self):
        pass
