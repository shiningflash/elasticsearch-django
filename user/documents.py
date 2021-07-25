from django_elasticsearch_dsl import (
    Document, fields, Index
)
from .models import Student


PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings(
    number_of_shards = 1,
    number_of_replicas = 1
)


@PUBLISHER_INDEX.doc_type
class StudentDocument(Document):
    
    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        fields = {
            "raw": {
                "type": 'keyword'
            }
        }
    )

    color = fields.TextField(
        fields = {
            "raw": {
                "type": 'keyword'
            }
        }
    )
    
    info = fields.TextField(
        fields = {
            "raw": {
                "type": 'keyword'
            }
        }
    )

    class Django(object):
        model = Student