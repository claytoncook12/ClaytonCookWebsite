# DjangoApp\tunes\test\test_views.py

import pytest

from django.test import Client
from django.urls import reverse

from tunes.tests import factories


@pytest.mark.django_db
class TestList:
    def test_reponse(self):

        client = Client()
        response = client.get(reverse("tunes:list"))

        assert response.status_code == 200,\
            "200 code status for tunes.views.list"


@pytest.mark.django_db
class TestTuneDetail:
    def test_reponse(self):

        obj = factories.TuneFactory()

        client = Client()
        response = client.get(obj.get_absolute_url())

        assert response.status_code == 200,\
            "tunes detail returns 200 status code"

    def test_content(self):

        obj = factories.TuneFactory()

        client = Client()
        response = client.get(obj.get_absolute_url())

        # Test tune.name in title for page
        name = obj.name.title()
        assert name in response.content.decode(), "tune.name is title of page"

        # Test tune.tune_type on page
        tune_type_html = "(" + obj.tune_type.tune_type_char + ")"
        assert tune_type_html in response.content.decode(),\
            "tune.tune_type.tune_type_char in tune detail page content"

    def test_abc_content(self):
        obj1 = factories.TuneFactory()
        obj2 = factories.ABCTuneFactory(
            tune=obj1
        )
        obj3 = factories.ABCTunePieceFactory(
            abc_tune=obj2
        )

        client = Client()
        response = client.get(obj1.get_absolute_url())

        #Test abc piece in present on page
        abc_piece = obj3.abc_piece
        assert abc_piece in response.content.decode(),\
            "abc_piece displayed on tune detail page"
    
    def test_youtube_playthrough(self):
        obj1 = factories.TuneFactory()

        obj2 = factories.YoutubePlaythroughFactory(
            tune=obj1
        )

        client = Client()
        response = client.get(obj1.get_absolute_url())

        #Test YoutunePlaythrough.title present on page
        video_title = obj2.title
        assert video_title in response.content.decode(),\
            "video_title desplayed on tune detail page"