from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response


class ChangeConfigRestView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        print('========', request)
        return Response(status=200)
