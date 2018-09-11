from django.urls import path
from .views import ChangeConfigRestView, CurrentConfigStateView


urlpatterns = [
    path('', ChangeConfigRestView.as_view()),
    path('/config-current-state', CurrentConfigStateView.as_view())
]
