from django.shortcuts import render

from .apps import MainConfig


def main_page_view(request):
    app_label = MainConfig.label

    return render(
        request,
        '{label}/main_page.html'.format(label=app_label),
        {
            'app_label': app_label,
        }
    )
