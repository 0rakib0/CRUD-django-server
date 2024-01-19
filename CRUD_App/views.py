from django.shortcuts import render
from .models import Employe
from .Sirializer import EmployeSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.

def employeList(request):
    employe = Employe.objects.all()
    Sirialize_employe = EmployeSerializer(employe, many=True)
    return JsonResponse(Sirialize_employe.data, content_type='application/json', safe=False)


def singleEmploye(request, id):
    employe = Employe.objects.get(id=id)
    Sirialize_employe = EmployeSerializer(employe)
    return JsonResponse(Sirialize_employe.data, content_type='application/json', safe=False)

@csrf_exempt
def AddEmploye(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializeData = EmployeSerializer(data = pythonData)
        print(serializeData)
        if serializeData.is_valid():
            serializeData.save()
            res = {'msg':'Employe Successfully added!'}
            return JsonResponse(res, content_type='application/json')
        
@csrf_exempt
def updateEmploye(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        employe = Employe.objects.get(id=id)
        serializeData = EmployeSerializer(employe, data=python_data, partial=True)
        if serializeData.is_valid():
            serializeData.save()
            res = {'msg':'Employe Successfully update!'}
            return JsonResponse(res, content_type='application/json')
        
        
@csrf_exempt
def deleteEmploye(request, id):
    print(id)
    if request.method == 'DELETE':
        employe = Employe.objects.get(id=id)
        print(employe)
        employe.delete()
        res = {'msg':'employe Sucessfully Deleted!'}
        return JsonResponse(res, content_type='application/json')