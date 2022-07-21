from django.contrib import admin
from . import models
from . import serialisers

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.ImageProduct)
admin.site.register(models.LikeProduct)





