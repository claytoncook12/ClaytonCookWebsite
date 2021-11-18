# DjangoApp\tunes\test\test_views.py

import pytest

from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

PASSWORD = "password"

@pytest.mark.django_db
class TestTunesHome:
    def test_reponse(self):

        client = Client()
        response = client.get(reverse("main:music_home"))

        assert response.status_code == 200,\
            "200 code status for tunes.views.tunes_list"

@pytest.mark.django_db
class TestAdminLinksTab:
    def test_admin_links_view_normal_user(Self):
        client = Client()
        response = client.get(reverse('main:admin_links'))

        assert response.status_code == 302, "302 status for main.views.adminlinks when user is not superuser in"
    
    def test_admin_links_view_superuser_user(Self):
        # Create SuperUser for testing
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', PASSWORD)
        
        client = Client()
        # You'll need to log him in before you can send requests through the client
        client.login(username=my_admin.username, password=PASSWORD)
        
        response = client.get(reverse('main:admin_links'))
        assert response.status_code == 200, "200 status for main.views.adminlinks when user is superuser"
