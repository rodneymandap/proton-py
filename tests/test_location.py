import pytest
from proton import Proton

class TestLocation:
    id = 6700
    client = Proton(token='test')
    location = client.location()

    def test_get_location_by_id(self):
        url = 'https://api.proton-graph.cloud/public/locations/api/v2/locations/{id}'.format(id=self.id)
        assert self.location.get_location_by_id(self.id) == url

    def test_get_location_feature_by_id(self):
        url = 'https://api.proton-graph.cloud/public/locations/api/v2/locationfeatures/{id}'.format(id=self.id)
        assert self.location.get_location_feature_by_id(self.id) == url
