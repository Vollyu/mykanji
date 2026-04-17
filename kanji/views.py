import requests
from django.shortcuts import render


KANJI_API_URL = "https://kanjiapi.dev/v1/kanji/jlpt-5"


def index(request):
    template_name = "index.html"
    context = {
        "title": "selamat datang di kanji",
    }
    return render(request, template_name, context)


def kanji(request):
    template_name = "kanji.html"
    response = requests.get(KANJI_API_URL, timeout=8)

    context = {
        "title": "selamat datang di kanji",
        "data": response.json()[:30] if response.status_code == 200 else [],
    }
    return render(request, template_name, context)