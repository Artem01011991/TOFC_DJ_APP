from django.urls import path
from .views import MainPageView, ChangeConfigView


urlpatterns = [
    path('', MainPageView.as_view()),
    path('change_config', ChangeConfigView.as_view())
]
