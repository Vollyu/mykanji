import requests
from django.shortcuts import render


# Constants
KANJI_API_URL = "https://kanjiapi.dev/v1/kanji/jlpt-5"
API_TIMEOUT = 8
KANJI_DATA_LIMIT = 30
PAGE_TITLE = "selamat datang di kanji"


def fetch_kanji_data():
    """
    Fetch kanji data from API with proper error handling.
    
    Returns:
        list: Kanji data up to KANJI_DATA_LIMIT, empty list on error.
    """
    try:
        response = requests.get(KANJI_API_URL, timeout=API_TIMEOUT)
        response.raise_for_status()
        return response.json()[:KANJI_DATA_LIMIT]
    except (requests.RequestException, ValueError):
        return []


def index(request):
    """Render home page."""
    template_name = "index.html"
    context = {
        "title": PAGE_TITLE,
    }
    return render(request, template_name, context)


def kanji(request):
    """Render kanji list page with data from API."""
    template_name = "kanji.html"
    context = {
        "title": PAGE_TITLE,
        "data": fetch_kanji_data(),
    }
    return render(request, template_name, context)