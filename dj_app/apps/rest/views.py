from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .settings import HEROKU_APP_NAME, CONFIG_FILE_NAME
import subprocess
import configparser


class ChangeConfigRestView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        if request.GET['id']:
            if request.GET['value'] == 'true':
                self.settings_control(request.GET['id'], True)
            else:
                self.settings_control(request.GET['id'], False)
            return Response(status=200)
        return Response('Incorrect GET request', status=400)

    def settings_control(self, conf_id, enabling:bool):  # Disabling heroku server if django app active
        conf = configparser.ConfigParser()
        conf.read('../' + CONFIG_FILE_NAME)
        conf_names = {
            'index_bot_control': 'index activation mode',
            'binance_bot_control': 'binance activation mode',
            'dj_control': 'django control'
        }

        if enabling:
            conf['Bot section'][conf_names[conf_id]] = 'true'
        else:
            conf['Bot section'][conf_names[conf_id]] = 'false'

        if conf_id == 'dj_control':
            self.django_control(enabling)

        with open('../' + CONFIG_FILE_NAME, 'w') as file:
            conf.write(file)
            file.close()

    @staticmethod
    def django_control(enabling):
        if enabling:
            subprocess.run(['heroku', 'ps:scale', 'clock=0', '-a', HEROKU_APP_NAME])
        else:
            subprocess.run(['heroku', 'ps:scale', 'clock=1', '-a', HEROKU_APP_NAME])


class CurrentConfigStateView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        if not request.GET:
            conf = configparser.ConfigParser()
            conf.read('../' + CONFIG_FILE_NAME)
            index_act_mode = conf['Bot section']['index activation mode']
            bin_act_mod = conf['Bot section']['binance activation mode']
            dj_conf_dom = conf['Bot section']['django control']
            return Response(
                data={
                    'index_bot_control': index_act_mode,
                    'binance_bot_control': bin_act_mod,
                    'dj_control': dj_conf_dom,
                },
                status=200
            )
