from rest_framework import serializers
from .models import CommissionPerOrder, PaymentDetails

class CommissionPerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionPerOrder
        fields = '__all__'

    def validate(self, data):
        if data.get('total_amount') < 0:
            raise serializers.ValidationError("Total amount cannot be negative")
        return data

    def update(self, instance, validated_data):
        if validated_data.get('commission_status') == 'eligible':
            # Perform commission calculation
            pass
        return super().update(instance, validated_data)

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

    def validate(self, data):
        # Implement custom validation logic
        return data
