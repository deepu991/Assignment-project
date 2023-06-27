from django.db import models

class Order(models.Model):
    order_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipped = models.BooleanField()

    def __str__(self):
        return f"Order ID: {self.order_id}"
