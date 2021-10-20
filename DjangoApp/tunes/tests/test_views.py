# DjangoApp\tunes\test\test_views.py

import pytest

from django.test import Client
from django.urls import reverse

from tunes.tests import factories

@pytest.mark.django_db
class TestTuneDetail:
    def test_reponse(self):

        obj = factories.TuneFactory()

        client = Client()
        response = client.get(obj.get_absolute_url())

        assert response.status_code == 200, "tunes detail returns 200 status code"