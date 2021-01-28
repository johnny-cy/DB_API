from django.shortcuts import render
from django.http.response import JsonResponse
from django.core import serializers
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework import status
from rest_framework.decorators import api_view

from db_api.models import DomainTestLog
from db_api.serializers import DomainTestLogSerializer
from db_api.models import DomainListAll
from db_api.serializers import DomainListAllSerializer
from db_api.models import DomainListDT3
from db_api.serializers import DomainTestLogDT3Serializer
from db_api.models import DomainTestLogDT3
from db_api.serializers import DomainListDT3Serializer



import time
import json

# Create your views here.
'''
1: domaintestlog
2: domainlistall

'''

type_ = [[DomainTestLog, DomainTestLogSerializer],
         [DomainListAll, DomainListAllSerializer],
         [DomainTestLogDT3, DomainTestLogDT3Serializer],
         [DomainListDT3, DomainListDT3Serializer]]


@api_view(['POST'])
def C_data(request):
    ''' add new data to database.'''
    data = JSONParser().parse(request)
    if request.method == 'POST':
        if 'tablename' not in data:
            return JsonResponse({"message": "Body:tablename"})
        tablename = data['tablename'].lower()
        input_ = data['data']
        model, serializers = main(tablename)
        if not model or not serializers:
            return JsonResponse({"message": "model or serializers not found."})

        if tablename == "domaintestlog":
            data_serializer = serializers(data=input_, many=True)  
            if data_serializer.is_valid():  
                data_serializer.save()
                return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)
            return JsonResponse(data_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        elif tablename == "domainlistall":
            data_serializer = serializers(data=input_, many=True)
            if data_serializer.is_valid():
                data_serializer.save()
                return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)
            return JsonResponse(data_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({"message": "Table doesn't exist."})


@api_view(['GET'])
def R_data(request):
    '''show data'''
    if request.method == 'GET':
        tablename = request.GET.get("tablename", None)
        filter_data = request.GET.get("filter_data", None)
        if not tablename:
            return JsonResponse({'message': 'Params:tablename'})
        tablename = tablename.lower()
        status, data , err_msg = getData(tablename=tablename, filter_data=filter_data)
        if status:
            return JsonResponse({"results": data}, safe=False)
        else:
            return JsonResponse({"status": "error", 'message': f'{err_msg}'})
        


@api_view(['PUT'])
def U_data(request, id_):
    ''' update specific data using id. '''
    data = JSONParser().parse(request)
    if request.method == 'PUT':
        if 'data' not in data:
            return JsonResponse({"message": "{data:[{}]..}"})
        if 'tablename' not in data:
            return JsonResponse({"message": "Body:tablename"})
        tablename = data['tablename'].lower()
        input_ = data['data'][0]
        model, serializers = main(tablename)
        if tablename == "domaintestlog":
            domaintestlog = model.objects.using('default').get(id=id_)
            # print(domaintestlog.CDN)
            # domaintestlog.TestTime = data["TestTime"]
            # domaintestlog.save()
            data_serializer = serializers(domaintestlog, data=input_)
            if data_serializer.is_valid():
                data_serializer.save()
                successed = {"successed": data_serializer.data}
                return JsonResponse(successed, status=status.HTTP_200_OK)
            return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif tablename == "domainlistall":
            domainlistall = model.objects.using('default').get(id=id_)
            data_serializer = serializers(domainlistall, data=input_)
            if data_serializer.is_valid():
                data_serializer.save()
                successed = {"successed": data_serializer.data}
                return JsonResponse(successed, status=status.HTTP_200_OK)
            return JsonResponse(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({"message": "Table doesn't exist."})


@api_view(['DELETE'])
def D_data(request, tablename, id_):
    ''' delete specific data using id. '''
    # data = JSONParser().parse(request)
    # tablename = data['tablename']
    if request.method == 'DELETE':

        model, serializers = main(tablename)
        if tablename == "domaintestlog":
            try:
                domaintestlog = model.objects.using('default').get(id=id_)
                domaintestlog.delete()
                return JsonResponse({"message": f"ID {id_} was deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
            except:
                return JsonResponse({"message": "ID doesn't exist"}, status=status.HTTP_204_NO_CONTENT)
        elif tablename == "domainlistall":
            try:
                domainlistall = model.objects.using('default').get(id=id_)
                domainlistall.delete()
                return JsonResponse({'message': f'ID: {id_} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            except:
                return JsonResponse({"message": "ID doesn't exist"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({"message": "Table doesn't exist."})


@api_view(['DELETE'])
def D_all_data(request, tablename):
    ''' delete all. '''
    # data = JSONParser().parse(request)
    # tablename = data['tablename']
    if request.method == 'DELETE':

        model, serializers = main(tablename)
        if tablename == "domaintestlog":
            count = model.objects.all().using('default').delete()
            if count[1]["db_api.DomainTestLog"] == 0:
                return JsonResponse({'message': 'Database was already empty.'})
            return JsonResponse({'message': f'Total {count[0]} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        elif tablename == "domainlistall":
            count = model.objects.all().using('default').delete()
            if count[1]["db_api.DomainListAll"] == 0:
                return JsonResponse({'message': 'Database was already empty.'})
            return JsonResponse({'message': f'Total {count[0]} was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({"message": "Table doesn't exist."})


def main(tablename):
    if tablename == "domaintestlog":
        model = type_[0][0]
        serializers = type_[0][1]
    elif tablename == "domainlistall":
        model = type_[1][0]
        serializers = type_[1][1]
    elif tablename == 'domaintestlogdt3':
        model= type_[2][0]
        serializers = type_[2][1]
    elif tablename == 'domainlistdt3':
        model= type_[3][0]
        serializers = type_[3][1]
    else:
        model = None
        serializers = None
    return model, serializers

def getData(tablename=tablename, filter_data=filter_data):
    model, serializers = main(tablename)
    if not model or not serializers:
        err_msg = "model or serializers not found."
        return False, [], err_msg

    if filter_data:
        data = json.loads(filter_data)
        try:
            queryset = model.objects.using('slave').complex_filter(data)
        except Exception as e:
            err_msg = f'{e}'
            return False, [], err_msg
    else:
        queryset = model.objects.using('slave').all()

    if queryset.count() == 0:
        err_msg = 'No data'
        return False, [], err_msg

    data_serializer = serializers(queryset, many=True)
    data = data_serializer.data
    return True, data, ""
