from Product.serialisers import (
    ProductSerializers,
    LikeSerializers,
    CategorySerializers,
    BainerySerializers,
    SimilarProductsSerializers,
)
from Product.models import Product, LikeProduct, Category
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ProductCreateListAPIVeiw(ListCreateAPIView):
    queryset = Product.objects.get_queryset().order_by("id")
    serializer_class = ProductSerializers


class ProductDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class LikeProductAPIVeiw(ListCreateAPIView):
    queryset = LikeProduct.objects.all()
    serializer_class = LikeSerializers


class CategoryAPIVeiw(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BayneryAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = BainerySerializers


class BainaryDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = BainerySerializers


class SimilarProductsAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = SimilarProductsSerializers


class SimilarProductsDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = SimilarProductsSerializers
