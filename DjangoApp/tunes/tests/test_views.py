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
    
    def test_content(self):

        obj = factories.TuneFactory()

        client = Client()
        response = client.get(obj.get_absolute_url())

        # Test tune.name in title for page
        name = obj.name.title()
        assert name in response.content.decode(), "tune.name is title of page"

        # Test tune.tune_type on page
        tune_type_html = "type: " + obj.tune_type.tune_type_char
        assert tune_type_html in response.content.decode(),\
            "tune.tune_type.tune_type_char in tune detail page content"
