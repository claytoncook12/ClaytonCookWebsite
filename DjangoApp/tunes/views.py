from django.shortcuts import get_object_or_404, render

from .models import Tune, ABCTune, YoutubePlaythrough


def list(request):

    tunes_qs = Tune.objects.all()

    context = {
        "tunes_qs": tunes_qs,
    }

    return render(request, "tunes/list.html", context)


def detail(request, pk):

    tune = get_object_or_404(Tune, pk=pk)
    abc_qs = ABCTune.objects.filter(tune=tune)
    playthrough_video_qs = YoutubePlaythrough.objects.filter(tune=tune)

    context = {
        "tune": tune,
        "abc_list": abc_qs,
        "playthrough_video_qs": playthrough_video_qs,
    }

    return render(request, "tunes/detail.html", context)
