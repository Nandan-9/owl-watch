from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Monitor


class MonitorCreateView(APIView):
    

    def post(self,request):
        data = request.data.get("payload")
        if data == None:
            return Response({
                "message" : "payload is empyt"
            },status=400)
        print(data)
        return Response({
            "message" : "monitor event added successfully"
        },status=200)

