from django.shortcuts import render


def list(request):

    context = {
        "value1": "value1",
    }

    return render(request, "tunes/list.html", context)


def detail(request, pk):

    context = {
        "value1": "value1",
    }

    return render(request, "tunes/detail.html", context)