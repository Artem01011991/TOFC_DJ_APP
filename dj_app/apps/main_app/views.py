from django.shortcuts import render
from .settings import MAIN_PAGE_ELEMS_IDS


def main_page_view(request):
    return render(request, 'main_app/main_page.html', {'ids': MAIN_PAGE_ELEMS_IDS})
