from django.shortcuts import render
from .app import MainConfig
from .settings import MAIN_PAGE_ELEMS_IDS


def main_page_view(request):
    app_label = MainConfig.label

    return render(
        request,
        '{label}/main_page.html'.format(label=app_label),
        {'ids': MAIN_PAGE_ELEMS_IDS, 'app_label': app_label}
    )
