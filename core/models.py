from django.db import models

class CurrencyModel(models.Model):
    currency_name = models.CharField(max_length=10)

class CommissionPerOrder(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    order_name = models.CharField(max_length=255)
    order_status = models.CharField(max_length=50)
    status_updated_at = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_in_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.ForeignKey(CurrencyModel, on_delete=models.SET_NULL, null=True)
    client_id = models.CharField(max_length=50)
    client_name = models.CharField(max_length=255)
    client_image = models.URLField(null=True, blank=True)
    staff_id = models.CharField(max_length=50)
    staff_name = models.CharField(max_length=255)
    staff_email = models.EmailField()
    region = models.CharField(max_length=50)
    commission_status = models.CharField(max_length=50, default='new')
    commission = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class PaymentDetails(models.Model):
    payment_uuid = models.CharField(max_length=50, unique=True)
    commission_order = models.ForeignKey(CommissionPerOrder, on_delete=models.CASCADE)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_currency = models.ForeignKey(CurrencyModel, on_delete=models.SET_NULL, null=True)
    payment_reference = models.CharField(max_length=255)
    payment_date = models.DateField()
    payment_channel = models.CharField(max_length=50)
    received_amount = models.DecimalField(max_digits=10, decimal_places=2)
    adjustment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
