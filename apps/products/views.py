from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response

from apps.products.models import Products
from apps.products.serializers import ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProductList1APIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        if category_id is None:
            raise Http404("Product ID is required")

        queryset = Products.objects.filter(category=category_id)
        if queryset.exists():
            return queryset

        raise Http404("Products not found")


class ProfileInfoListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            if user.is_superuser:
                return Products.objects.all()
            else:
                return Products.objects.filter(id=user.id)
        else:
            return Products.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductCreateSerializer


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductCreateSerializer
