from django.urls import path
from .views import ChangeConfigRestView, CurrentConfigStateView

app_name = 'rest'
urlpatterns = [
    path('', ChangeConfigRestView.as_view(), name='main'),
    path('config-current-state', CurrentConfigStateView.as_view(), name='conf-cur-state')
]
