from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Monitor
import requests


class MonitorCreateView(APIView):
    

    def post(self,request):
        data = request.data.get("payload")
        if data == None:
            return Response({
                "message" : "payload is empyt"
            },status=400)
        print(data)
        r = requests.get(data, timeout=5)
        status = r.status_code == 200
        response_time = r.elapsed.total_seconds()
        print(r)
        return Response({
            "response" : {
                "status" : status,
                "reponse_time" : response_time
            } 
        },status=200)

