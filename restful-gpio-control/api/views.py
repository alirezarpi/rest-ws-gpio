from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import ARRCModels
from .serializers import ARRCSerializer
from ipware import get_client_ip
from . import arcg

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def all_requests(request):
    ip, is_routable = get_client_ip(request)
    
    if ip is None:
        print("Unable to get Client IP")
    else:
        if is_routable:
            print("IP is routable")
        else:
            print("Client IP: " + ip) 

    if (request.method == 'GET'):
        datas = ARRCModels.objects.all()
        datas_serialized = ARRCSerializer(datas, many=True)
        return JSONResponse(datas_serialized.data)

    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        data_serialized = ARRCSerializer(data=data)
        if ( data_serialized.is_valid() ):
            if ( not (arcg.validate_data(data['data']))):
                print("Data Not Acceptable")
                content = {'response': 'Data Not Acceptable'}
                return JSONResponse(content, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                arcg.change_gpio(data['data'])    
                data_serialized.save()
                return JSONResponse(data_serialized.data, status=status.HTTP_201_CREATED)
        return JSONResponse(data_serialized, status=status.HTTP_400_BAD_REQUEST)
