from showplace.models import Showplace
from rest_framework import serializers
from category.serializers import CategorySerializer

class ShowplaceSerializer(serializers.ModelSerializer):
    category_id=CategorySerializer()
    class Meta:
        model = Showplace
        fields = ["id", "name", "category_id"]