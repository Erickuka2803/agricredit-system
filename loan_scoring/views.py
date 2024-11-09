from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Farmer, LoanApplication
from .utils import calculate_score

def apply_for_loan(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    score = calculate_score(farmer)
    is_approved = score >= 50  # Example threshold for loan approval

    # Save the loan application
    loan_application = LoanApplication.objects.create(
        farmer=farmer,
        score=score,
        is_approved=is_approved
    )

    return JsonResponse({
        'farmer': farmer.name,
        'score': score,
        'is_approved': is_approved
    })
