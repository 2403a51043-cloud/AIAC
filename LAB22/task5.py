# ============================================
# Task 5 – AI in Decision-Making
# Interactive Loan Approval System (Explainable AI)
# ============================================

def loan_decision(income, credit_score, loan_amount, employment_years):
    """
    Simple AI rule-based model for loan approval.
    Also returns reasoning for transparency.
    """
    reasons = []
    
    # Rule 1: Check income
    if income < 20000:
        reasons.append("Income is below the required minimum of 20,000.")
    
    # Rule 2: Check credit score
    if credit_score < 650:
        reasons.append("Credit score is too low (needs to be at least 650).")
    
    # Rule 3: Check employment stability
    if employment_years < 1:
        reasons.append("Employment duration is less than 1 year.")
    
    # Rule 4: Loan amount limit
    if loan_amount > income * 10:
        reasons.append("Loan amount is too high compared to income.")

    # Final Decision
    if reasons:
        decision = "❌ Loan Rejected"
    else:
        decision = "✅ Loan Approved"

    return decision, reasons


def main():
    print("=====================================")
    print("   🏦 AI LOAN APPROVAL SYSTEM")
    print("=====================================\n")

    name = input("Enter your name: ")
    income = float(input("Enter your annual income (in ₹): "))
    credit_score = int(input("Enter your credit score (300–900): "))
    loan_amount = float(input("Enter desired loan amount (in ₹): "))
    employment_years = float(input("Enter your years of employment: "))

    print("\nAnalyzing your loan eligibility...\n")

    decision, reasons = loan_decision(income, credit_score, loan_amount, employment_years)

    print("=====================================")
    print(f"Applicant Name: {name}")
    print(f"Annual Income: ₹{income}")
    print(f"Credit Score: {credit_score}")
    print(f"Loan Amount Requested: ₹{loan_amount}")
    print(f"Employment Years: {employment_years}")
    print("-------------------------------------")
    print(f"Final Decision: {decision}")
    
    if reasons:
        print("\nReason(s) for Decision:")
        for r in reasons:
            print(f" - {r}")
    else:
        print("\nAll eligibility criteria met successfully.")
    
    print("-------------------------------------")
    print("🤖 Transparency Note:")
    print("This AI system bases decisions on income, credit score, employment stability, and loan-to-income ratio.")
    print("Final approval must still be reviewed by a human loan officer.")
    print("=====================================\n")


if __name__ == "__main__":
    main()
