import requests
import logging

DEFAULT_TIMEOUT = 5  # seconds
logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')

class Proton:
    def __init__(self, prefix_url=None, token=None):
        self.timeout = DEFAULT_TIMEOUT
        self.static_url = 'https://api.proton-graph.cloud/public/static-references/api'
        self.location_base_url = 'https://api.proton-graph.cloud/public/locations/api'

        if token is None:
            raise ValueError("Token must be provided.")
        else:
            self.headers = {
                'Ocp-Apim-Subscription-Key': token
            }

    def get(self, url):
        response = requests.get(url, headers=self.headers)
        logging.info(f'GET request for {url}')
        return response

    def currency(self, id=None):
        if id is None:
            url = f"{self.static_url}/v1/currencies"
        else:
            url = f"{self.static_url}/v1/currencies/{id}"
        currencies = self.get(url)
        return currencies

    def country(self, id=None):
        if id is None:
            url = f"{self.static_url}/v1/countries"
        else:
            url = f"{self.static_url}/v1/countries/{id}"
        countries = self.get(url)
        return countries 

    def language(self, id=None):
        if id is None:
            url = f"{self.static_url}/v1/languages"
        else:
            url = f"{self.static_url}/v1/languages/{id}"
        languages = self.get(url)
        return languages 
        
    def time_zone(self, id=None):
        if id is None:
            url = f"{self.static_url}/v1/timezones"
        else:
            url = f"{self.static_url}/v1/timezones/{id}"
        time_zones = self.get(url)
        return time_zones 



class Location(Proton):
    """
        Reference: https://portal.proton-graph.cloud/docs/locations-journey
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix_url = 'https://api.proton-graph.cloud/public/locations/api'

    def get(self, url=None):
        """
            Return names and numbers only
            Useful for caching purposes
        """
        url = f"{self.prefix_url}/v2/locations/dump"
        return super().get(url)

    def get_location_id(self, id):
        """
            Return locations that corresponds to id provided
        """
        url = f"{self.prefix_url}/v2/locations/{id}"
        return super().get(url)

    def get_location_feature(self, id):
        """
            Gets a single location feature by its key identifier. Location features define special services within a location such as on site lunch bars, showers, parking, gym, etc...
        """
        url = f"{self.prefix_url}/v2/locationfeatures/{id}"
        return super().get(url)


class Booking(Proton):
    """
        Reference: https://portal.proton-graph.cloud/docs/bookings-journey 
    """

    def __init__(self):
        pass
