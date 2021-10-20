from django.shortcuts import render, get_object_or_404


def home(request):

    return render(request, 'home.html')


def music_home(request):

    context = {}

    return render(request, "music_home.html", context)
