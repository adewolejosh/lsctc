
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class PingView(APIView):

    def get(self, request):
        return Response({"Success": "Successfully pinged lsctc-py-server"}, status=status.HTTP_200_OK)
