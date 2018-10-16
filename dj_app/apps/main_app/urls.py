from django.urls import path
from .views import main_page_view


app_name = 'main'
urlpatterns = [
    path('', main_page_view),
]
