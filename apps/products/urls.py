from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.products import views


urlpatterns = [
    path('product/',views.ProductCreateAPIView.as_view(),name="product_create"),
    path('product/',views.ProductList1APIView.as_view(),name="product_list"),
    path('product/',views.ProductUpdateAPIView.as_view(),name="product_update"),
    path('product/',views.ProductDeleteAPIView.as_view(),name="product_delete"),
]
