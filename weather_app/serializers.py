from djangorestframework import serializers
from models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'date', 'lat', 'lon', 'city', 'state','temperature']