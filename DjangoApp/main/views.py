import sys
import os
from pathlib import Path
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.core.management import call_command
from django.conf import settings


def home(request):

    return render(request, 'home.html')


def music_home(request):

    context = {}

    return render(request, "music_home.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_links(request):

    return render(request, 'admin_links.html')

@user_passes_test(lambda u: u.is_superuser)
def dbjson(request):

    # Make File Name
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    json_file_name = f'{date_time}claytoncook_comdb.json'
    path = Path(settings.BASE_DIR) / 'datadump'
    json_file = path / json_file_name

    # Point SystemOutput to file, write to file, and close
    sys.stdout = open(json_file, 'w+') # Point stdout at a file for dumping data too.
    call_command('dumpdata', indent=3)
    sys.stdout.close()

    # Write File Contents to Temp File
    with open(json_file, 'r') as f:
        file_data = f.read()

    # Delete Out File Location
    os.remove(json_file)

    # Create Reponse to Send
    response = HttpResponse(file_data, content_type="text/plain")
    response['Content-Disposition'] = f'attachment; filename={json_file_name}'

    return response
