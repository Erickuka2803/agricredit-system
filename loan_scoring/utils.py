# loan_scoring/utils.py

def calculate_score(farmer):
    score = 0

    # Age criteria
    if 25 <= farmer.age <= 45:
        score += 15
    elif farmer.age > 45:
        score += 10

    # Income criteria
    if farmer.annual_income > 100000:
        score += 20
    elif farmer.annual_income > 50000:
        score += 15
    else:
        score += 5

    # Land size criteria
    if farmer.land_size > 5:  # in acres
        score += 10

    # Loan history criteria
    if farmer.previous_loans == 0:
        score += 20  # Favor new applicants
    elif farmer.previous_loans == 1:
        score += 10

    # Credit score criteria
    if farmer.credit_score >= 700:
        score += 25
    elif farmer.credit_score >= 650:
        score += 15
    else:
        score -= 10  # Penalty for low credit score

    # Final threshold logic
    if farmer.loan_amount_requested > farmer.annual_income * 0.3:
        score -= 15  # Penalty if loan is too high relative to income

    return max(0, min(score, 100))  # Ensure score is between 0 and 100
