from django.shortcuts import render
from .models import Employe
from .Sirializer import EmployeSerializer
from django.http import JsonResponse
# Create your views here.

def employeList(request):
    employe = Employe.objects.all()
    Sirialize_employe = EmployeSerializer(employe, many=True)
    return JsonResponse(Sirialize_employe.data, content_type='application/json', safe=False)
