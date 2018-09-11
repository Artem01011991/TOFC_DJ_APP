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
        if request.GET['dj_control']:
            if request.GET['dj_control'] == 'true':
                self.django_control(True)
            elif request.GET['dj_control'] == 'false':
                self.django_control(False)
            return Response(status=200)
        Response('Incorrect GET request', status=400)

    @staticmethod
    def django_control(enabling:bool):  # Disabling heroku server if django app active
        conf = configparser.ConfigParser()
        conf.read('../' + CONFIG_FILE_NAME)

        if enabling:
            subprocess.run(['heroku', 'ps:scale', 'clock=0', '-a', HEROKU_APP_NAME])
            conf['Bot section']['Django control'] = 'true'
        else:
            subprocess.run(['heroku', 'ps:scale', 'clock=1', '-a', HEROKU_APP_NAME])
            conf['Bot section']['Django control'] = 'false'

        with open('../' + CONFIG_FILE_NAME, 'w') as file:
            conf.write(file)
            file.close()


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
                    'index_act_mode': index_act_mode,
                    'bin_act_mode': bin_act_mod,
                    'dj_conf_mode': dj_conf_dom,
                },
                status=200
            )
