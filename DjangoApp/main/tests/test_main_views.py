# DjangoApp\tunes\test\test_views.py

import pytest

from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestTunesHome:
    def test_reponse(self):

        client = Client()
        response = client.get(reverse("main:music_home"))

        assert response.status_code == 200,\
            "200 code status for tunes.views.tunes_list"
