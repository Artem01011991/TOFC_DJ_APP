from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from TOFC_ETH.settings import HEROKU_APP_NAME, CONF_PATH, SCHEDULER_IDS
from TOFC_ETH.controling_opirations import modules_manipulations
from dj_app.apps.main_app.settings import MAIN_PAGE_ELEMS_IDS, CONFIG_NAME_BY_ID
import subprocess
import configparser


class ConfRestBaseView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    conf = configparser.ConfigParser()
    conf.read(CONF_PATH)


class ChangeConfigRestView(ConfRestBaseView):
    def get(self, request, format=None):
        if request.GET['id']:
            self.settings_control(request.GET['id'], True if request.GET['value'] == 'true' else False)
            return Response(status=200)
        return Response('Incorrect GET request', status=400)

    def settings_control(self, conf_id, enabling:bool):  # Disabling heroku server if django app active
        self.conf['Bot section'][CONFIG_NAME_BY_ID[conf_id]] = 'true' if enabling else 'false'

        if conf_id == MAIN_PAGE_ELEMS_IDS['django']:
            self.django_control(enabling)
        else:
            modules_manipulations({next(SCHEDULER_IDS[i] for i in SCHEDULER_IDS if i in conf_id): enabling})

        with open(CONF_PATH, 'w') as file:
            self.conf.write(file)
            file.close()

    @staticmethod
    def django_control(enabling:bool):
        subprocess.Popen(['heroku', 'ps:scale', 'clock=1' if enabling else 'clock=0', '-a', HEROKU_APP_NAME])


class CurrentConfigStateView(ConfRestBaseView):
    def get(self, request, format=None):
        if not request.GET:
            data = {k: self.conf['Bot section'][CONFIG_NAME_BY_ID[k]] for k in CONFIG_NAME_BY_ID}
            return Response(data=data, status=200)
        return Response(status=400)
