from django.db import models

class Payment(models.Model):
    order_id = models.IntegerField()  # در حالت واقعی FK به Order
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ], default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.status}"
