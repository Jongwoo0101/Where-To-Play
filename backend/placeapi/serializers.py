from rest_framework import serializers
from .models import PlaceInfo

class PlaceInfoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_empty_file=True, required=False)
    class Meta:
        model = PlaceInfo
        fields = [
            'image',
            'name',
            'created_at',
            'updated_at',
            'lat',
            'lng',
            'address', 
            'contact',
            'homepage',
            'time',
            'description'
        ]

    def create(self, validated_data):
        place = PlaceInfo(
            image=validated_data['image'],
            name=validated_data['name'],
            created_at=validated_data['created_at'],
            updated_at=validated_data['updated_at'],
            lat=validated_data['lat'],
            lng=validated_data['lng'],
            address=validated_data['address'],
            contact=validated_data['contact'],
            homepage=validated_data['homepage'],
            time=validated_data['time'],
            description=validated_data['description'],
        )
        place.save()
        return place