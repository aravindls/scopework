from rest_framework.views import APIView
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.http import Http404

class ProductList(APIView):
    queryset = Product.objects.all()
    serializer = ProductSerializer
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self):
        queryset = Product.objects.all()
        category_ids = self.request.query_params.getlist('category')
        if category_ids:
            queryset = queryset.filter(categories__id__in=category_ids)
        return queryset

# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class CategoryList(generics.ListCreateAPIView):
#     # queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def get_queryset(self):
#         return Category.objects.filter(parent_category=None)

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     # queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def get_queryset(self):
#         category = Category.objects.get(pk=self.kwargs['pk'])
#         return category.products.all()