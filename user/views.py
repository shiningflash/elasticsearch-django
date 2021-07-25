import json

from django.http import JsonResponse
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)

from .models import Student
from .documents import StudentDocument
from .serializers import StudentDocumentSerializer


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


class PublisherDocumentView(DocumentViewSet):
    document = StudentDocument
    serializer_class = StudentDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    ]

    search_fields = ('name', 'color', 'info')
    multi_match_search_fields = ('name', 'color', 'info')
    filter_fields = {
        'name': 'name',
        'color': 'color',
        'info': 'info'
    }
