from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from .models import Product, LikeProduct, ImageProduct


class BainerySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = 'id image title price'.split()

class SimilarProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = 'id title image price '.split()

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.LikeProduct
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


def velidate_director_id(category_id):
    if Product.objects.filter(id=category_id).count() == 0:
        raise ValidationError(f'Category with id={category_id} not found!')
    return category_id


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()
    paret = serializers.IntegerField()


class ProductValidateSerializer(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    cpu = serializers.CharField()
    main_camera = serializers.CharField()
    front_camera = serializers.CharField()
    memory = serializers.IntegerField()
    ram = serializers.IntegerField()
    is_hit = serializers.BooleanField()

    def velidate_director_id(self, product_id):
        if Product.objects.filter(id=product_id).count() == 0:
            raise ValidationError(f'Product with id={product_id} not found!')
        return product_id


class LikeValidateSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    user = serializers.IntegerField()

    def validate_movie_id(self, like_id):
        if LikeProduct.objects.filter(id=like_id).count() == 0:
            raise ValidationError(f'Like with id={like_id} not found!')
        return like_id


class ImageValidateSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    image = serializers.ImageField()

    def velidate_director_id(self, Image_id):
        if ImageProduct.objects.filter(id=Image_id).count() == 0:
            raise ValidationError(f'Category with id={Image_id} not found!')
        return Image_id
