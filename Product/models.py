from django.db import models
from rest_framework.authtoken.admin import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    parents = models.ForeignKey('self', on_delete=models.CASCADE,
                              null=True, blank=True)
    is_popular = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=80, null=True, blank=False, verbose_name="название")
    description = models.TextField( verbose_name='Описание')
    price = models.FloatField(verbose_name='цена')
    cpu = models.CharField(max_length=50, null=True, blank=False)
    main_camera = models.CharField(max_length=50, null=True, blank=True, verbose_name='основная камера')
    front_camera = models.CharField(max_length=50, null=True, blank=True, verbose_name='фронтальная камера')
    memory = models.PositiveIntegerField(verbose_name='память')
    ram = models.PositiveIntegerField(verbose_name='оперативная память')
    is_hit = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True, blank=True)

    new_price = models.FloatField(default=True, null=True, blank=True)

    def __str__(self):
        return self.title


class LikeProduct(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)


class ImageProduct(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
