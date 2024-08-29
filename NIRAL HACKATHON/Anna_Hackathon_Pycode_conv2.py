import re
import os
def extract_customer_data1(hackathon_match):
    requirements_keywords = ['looking for', 'interested in', 'require', 'want', 'need', 'searching up for', 'willing to buy', 'taking interests in buying', 'budget of']
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
#for conv2.txt in Google Docs
# Example conversation hackathon_match
hackathon_match = """
alesperson: Good afternoon, sir. How can I assist you today?
Customer: Good afternoon. I'm looking for a car within a budget of Rs. 600,000. My primary concerns are safety and proper maintenance. I don't have any specific preference for the vehicle size or type.
Salesperson: Understood, sir. We have a variety of options that might suit your needs. Are you looking for an automatic or manual transmission?
Customer: I don't have a preference for that either. Just show me what fits my budget and requirements.
Salesperson: Certainly, sir. We ensure that all our vehicles undergo a thorough 200-point inspection to guarantee they are non-accidental, non-meter tampered, and have a complete service history. This way, you can be assured of the vehicle's condition.
Customer: That's good to know. What kind of warranty do you offer after purchase?
Salesperson: Once you purchase a vehicle, you will have a one-year or 15,000 kilometers warranty on the engine and gearbox. Additionally, for three months or 5,000 kilometers, we cover the AC, electrical, and fuel systems. We also offer a five-day money-back guarantee if you are not satisfied with the vehicle.
Customer: That sounds reassuring. So, what options do you have in my budget?
Salesperson: Let me show you a few options. We have both budget and assured categories. The budget vehicles might have higher mileage and more owners, while the assured ones are well-maintained and in showroom condition. 
Customer: I see. Can you show me a sedan? I prefer something at least the size of a Fabia.
Salesperson: Absolutely, sir. Here is a 2015 Honda City. It's a well-maintained sedan with 1,20,000 kilometers on it. 
Customer: How much is it?
Salesperson: This one is priced at Rs. 6,97,000. However, I must mention that it has a few minor scratches and the paint job isn't perfect. But mechanically, it's in excellent condition.
Customer: Hmm, the scratches and paint job are a bit concerning. Do you have anything else?
Salesperson: We also have a 2014 Maruti Suzuki Ciaz. It's slightly older but has fewer kilometers on it. The paint and exterior are in better condition compared to the Honda City.
Customer: What about the engine and overall maintenance?
Salesperson: Both vehicles have been thoroughly inspected and are in good mechanical condition. The Ciaz has a quieter engine and a cleaner interior.
Customer: That's good to hear. What about the resale value after three years?
Salesperson: For assured vehicles, we offer a buy-back guarantee. For example, if you choose the Honda City, after one year, we will buy it back for Rs. 5,00,000, after two years for Rs. 4,32,000, and after three years for Rs. 4,00,000. This is subject to the vehicle not exceeding 10,000 kilometers per year and being serviced at authorized centers.
Customer: That sounds fair. Can I take a test drive?
Salesperson: Of course, sir. You can either come to our showroom or book a home test drive. The home test drive slots are available within one or two days.
Customer: I live about five kilometers from here. Can we arrange a home test drive?
Salesperson: Certainly, sir. I will book a slot for you. You will receive a confirmation shortly.
Customer: Thank you. I appreciate your help.
Salesperson: My pleasure, sir. If you have any other questions or need further assistance, feel free to contact us. Have a great day!
Customer: Thank you. Goodbye.
Salesperson: Goodbye, sir.
"""

# Process the hackathon_match
process_hackathon_match(hackathon_match)
