from django.shortcuts import get_object_or_404, render

from .models import Tune, ABCTune


def list(request):

    context = {
        "value1": "value1",
    }

    return render(request, "tunes/list.html", context)


def detail(request, pk):

    tune = get_object_or_404(Tune, pk=pk)
    abc_qs = ABCTune.objects.filter(tune=tune)

    context = {
        "tune": tune,
        "abc_list": abc_qs,
    }

    return render(request, "tunes/detail.html", context)
