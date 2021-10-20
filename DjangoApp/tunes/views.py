from django.shortcuts import get_object_or_404, render

from .models import Tune


def list(request):

    context = {
        "value1": "value1",
    }

    return render(request, "tunes/list.html", context)


def detail(request, pk):

    tune = get_object_or_404(Tune, pk=pk)

    context = {
        "tune": tune,
    }

    return render(request, "tunes/detail.html", context)