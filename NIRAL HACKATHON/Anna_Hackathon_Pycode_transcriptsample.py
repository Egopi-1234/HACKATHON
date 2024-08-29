import re
import os
def extract_customer_data1(hackathon_match):
    requirements_keywords = ['looking for', 'interested in', 'require', 'want', 'need', 'searching up for', 'willing to buy', 'taking interests in buying']
    requirements = []

    for line in hackathon_match.splitlines():
        for keyword in requirements_keywords:
            if keyword in line.lower():
                requirements.append(line.strip())
                break

    return requirements

def extract_company_data1(hackathon_match):
    policy_keywords = ['policy', 'terms', 'conditions', 'warranty', 'insurance', 'financing', 'scheme', 'guidelines']
    policies = []

    for line in hackathon_match.splitlines():
        for keyword in policy_keywords:
            if keyword in line.lower():
                policies.append(line.strip())
                break

    return policies
                
def extract_customer_data2(hackathon_match):
    objection_keywords = ['but', 'however', 'concern', 'issue', 'problem', 'worry', 'perhaps', 'troublesome', 'awkward', 'prickly', 'complicated']
    objections = []

    for line in hackathon_match.splitlines():
        for keyword in objection_keywords:
            if keyword in line.lower():
                objections.append(line.strip())
                break

    return objections

def process_hackathon_match(hackathon_match):
    customer_data1 = extract_customer_data1(hackathon_match)
    company_data1 = extract_company_data1(hackathon_match)
    customer_data2 = extract_customer_data2(hackathon_match)

    print("\nCustomer Requirements for Car:")
    for req in customer_data1:
        print("-", req)

    print("\nCompany Policies Discussed:")
    for policy in company_data1:
        print("-", policy)

    print("\nCustomer Objections:")
    for objection in customer_data2:
        print("-", objection)

# Example conversation hackathon_match
hackathon_match = """
Customer: I'm willing to buy a car with a 7-seater capacity.
Salesperson: We have several models that are of larger seating capacities.
Customer: I'm also interested in a car with a high-mileage and diesel type variant.
Salesperson: We do have car models that offer the seating capacities and the diesel variant that you are looking for. However, they come in hand with an additional cost and incremented taxes altogether.
Customer: That might be a concern for me. What about financing options and guidelines to buy a car that will cost less?
Salesperson: We offer various financing policies and also provide suitable schemes under which you can buy them at a minimal cost. You can choose one that suits your budget.
Customer: I'm worried about the maintenance costs in the long run.
Salesperson: Our cars come with a 5-year warranty which covers most maintenance issues.
"""
#for conv.txt samples in Google Docs
# Process the hackathon_match
process_hackathon_match(hackathon_match)
