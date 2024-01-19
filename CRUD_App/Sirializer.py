from rest_framework import serializers
from .models import Employe


class EmployeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Employe
        fields = ['id', 'name', 'email', 'phone', 'salary', 'dob']