from rest_framework import serializers
from .models import PlaceInfo

class PlaceInfoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    image = serializers.ImageField(
        allow_empty_file=True,
        required=False,
        use_url=True,
        max_length=None
        )
    def get_image_url(self, obj):   
        return obj.image.url
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
            'description',
            'image_url'
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