from rest_framework.response import Response
from rest_framework.views import APIView


class ReturnTrueView(APIView):
    def get(self, request):
        return Response({"result": True})
