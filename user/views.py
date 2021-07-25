from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Student


def generate_random_data():
    f = open('data.json',)
    data = json.load(f)
    print('OK')
    
    for student in data:
        Student.objects.create(
            name = student.get('Name'),
            color = student.get('Color'),
            info = student.get('Info')
        )
    f.close()

def index(request):
    generate_random_data()
    return JsonResponse({
        'status': 200
    })