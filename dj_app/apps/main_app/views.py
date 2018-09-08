from django.views.generic import View, FormView
from django.shortcuts import render
import configparser


class MainPageView(View):
    conf_file = configparser.ConfigParser()

    def get(self, request, *args, **kwargs):
        self.conf_file.read('../config.ini')  # TODO change 'config.ini' to setting value
        dj_control_state = self.conf_file['Bot section']['Django control']
        return render(request, 'main_app/main_page.html', {'data': {'dj_control_state': dj_control_state}})


class ChangeConfigView(FormView):
    pass
