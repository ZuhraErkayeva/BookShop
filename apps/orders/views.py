from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['book', 'status']
    filter_fields = ['status']
    ordering_fields = ['quantity']