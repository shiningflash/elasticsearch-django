from .models import Student
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import StudentDocument


class StudentDocumentSerializer(DocumentSerializer):
    
    class Meta:
        model = Student
        document = StudentDocument

        fields = ('name', 'color', 'info')

        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}