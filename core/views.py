from rest_framework import generics
from .models import CommissionPerOrder, PaymentDetails
from .serializers import CommissionPerOrderSerializer, PaymentDetailsSerializer

class YourAPIView(generics.GenericAPIView):
    serializer_class = CommissionPerOrderSerializer
    
    def get_queryset(self):
        # Implement filtering logic here
        pass

    def perform_create(self, serializer):
        # Handle creation logic
        pass

    def perform_update(self, serializer):
        # Handle update logic
        pass

    def perform_destroy(self, instance):
        # Handle delete logic
        pass
