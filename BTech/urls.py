"""BTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

from Product import views
from User import views as user_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/bainary/", views.BayneryAPIView.as_view()),
    path("api/v1/bainary/<int:pk>/", views.BainaryDetailUpdateDestroyAPIView.as_view()),
    path("api/v1/similar/", views.SimilarProductsAPIView.as_view()),
    path(
        "api/v1/similar/<int:pk>/",
        views.SimilarProductsDetailUpdateDestroyAPIView.as_view(),
    ),
    path("api/v1/register/", user_views.RegisterAPIView.as_view()),
    path("api/v1/login/", user_views.AuthorizationAPIView.as_view()),
    path("api/v1/product/", views.ProductCreateListAPIVeiw.as_view()),
    path("api/v1/product/<int:pk>/", views.ProductDetailUpdateDestroyAPIView.as_view()),
    path("api/v1/like/", views.LikeProductAPIVeiw.as_view()),
    path("api/v1/category/", views.CategoryAPIVeiw.as_view()),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
