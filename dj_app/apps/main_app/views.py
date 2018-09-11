from django.shortcuts import render


def main_page_view(request):
    return render(request, 'main_app/main_page.html')
