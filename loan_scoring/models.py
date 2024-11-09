from django.db import models

# Create your models here.
from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    location = models.CharField(max_length=255)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    land_size = models.DecimalField(max_digits=6, decimal_places=2)
    loan_amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    previous_loans = models.IntegerField(default=0)
    credit_score = models.IntegerField()

    def __str__(self):
        return self.name

class LoanApplication(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan Application for {self.farmer.name}"
