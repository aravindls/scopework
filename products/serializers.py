from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.StringRelatedField(many=True)
    products = serializers.StringRelatedField(many=True)
    
    def get_sub_categories(self, obj):
        serializer = self.__class__(obj.sub_categories.all(), many=True)
        serializer.bind('', self)
        return serializer.data
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent_category', 'sub_categories', 'products')


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'categories')
