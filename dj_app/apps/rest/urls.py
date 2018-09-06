from django.urls import path
from .views import ChangeConfigRestView


urlpatterns = [
    path('', ChangeConfigRestView.as_view())
]
