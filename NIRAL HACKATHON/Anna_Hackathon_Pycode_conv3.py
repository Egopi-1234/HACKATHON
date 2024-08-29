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
    policy_keywords = ['policy', 'terms', 'conditions', 'warranty', 'insurance', 'financing', 'scheme', 'guidelines', 'for a living']
    policies = []

    for line in hackathon_match.splitlines():
        for keyword in policy_keywords:
            if keyword in line.lower():
                policies.append(line.strip())
                break

    return policies

def extract_company_customer_work(hackathon_match):
    company_side= ['what do you do', 'what is your passion', 'where do you live', 'where do you work', 'Income Tax Return', 'do you own up a home of your own']
    companywords= []

    for line in hackathon_match.splitlines():
        for keyword in company_side:
            if keyword in line.lower():
                companywords.append(line.strip())
                break
            
    return companywords

def extract_user_doubts(hackathon_match):
    user_ques= ['what about the warranty', 'what about my I-20', 'Tiago', 'what are the discount offers that are available', 'how to avail for an EMI buying option']
    userques= []

    for line in hackathon_match.splitlines():
        for key in user_ques:
            if key in line.lower():
                userques.append(line.strip())
                break

    return userques
                
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
Salesperson: Welcome! Let me show you our selection. This is the I-20 model. Are you planning to pay in cash or take a loan?

Customer: I'm looking for a loan.

Salesperson: Great. What do you do for a living? Do you have a regular salary?

Customer: I work in agriculture.

Salesperson: Do you have an Income Tax Return (ITR)?

Customer: No, I don't.

Salesperson: Do you own any land or agricultural property?

Customer: No, I have a loan. This is Bangalore, right?

Salesperson: Yes, it is. Do you have any outstanding loans to pay off?

Customer: Yes, I do.

Salesperson: Do you have a specific budget in mind?

Customer: Yes, I do.

Salesperson: Could you share your mobile number, please?

Customer: It's 1851595.

Salesperson: And your name?

Customer: I'm looking for a petrol vehicle.

Salesperson: Sure, but may I have your name?

Customer: Manoj, Do you have vehicles for daily use?

Salesperson: Yes, we do.

Customer: I have two vehicles already. One is from 2017 and the other from 2014.

Salesperson: This one here is priced at 5,39,000 rupees, and that one is 5,24,000 rupees. Both are West Bengal registered.

Customer: WB registration?

Salesperson: Yes, but we can include Karnataka registration at the same price. However, for diesel vehicles, you might not find many options. You could consider petrol vehicles like the I-10 or Eon.

Customer: The I-10 is too small.

Salesperson: In that case, you might want to look at the Alto. With a budget of 3.5 lakhs, you won't find a Venue or I-20.

Customer: What about petrol options?

Salesperson: The Venue starts from 9 lakhs.

Customer: What?

Salesperson: Yes, the Venue starts from 9 lakhs. The I-20 starts from 5 lakhs minimum. You can consider it.

Customer: What are the benefits?

Salesperson: The engine and gearbox come with a one-year guarantee. Please have a seat. We ensure the vehicle has passed 200 checkpoints, and the RC transfer and one-year insurance are included. If you're not satisfied, you can return the vehicle within 5 days or 300 Km for a full cash refund.

Customer: How much is the vehicle price?

Salesperson: We have diesel options available. What do you think about this vehicle?

Customer: It looks okay, but what about the warranty?

Salesperson: The warranty is for one year. If not, the engine and gearbox are covered for 100,000 Km.

Customer: What about the Swift diesel?

Salesperson: It's available for 100,000 Km. It's a 2011 model with 1,22,000 Km on it.

Customer: And the second one?

Salesperson: That one has 3,21,000 Km on it.

Customer: What about the Tiago?

Salesperson: The Tiago has 16,000 Km on it. It's white, a Tata Tiago, with 86,000 Km. It's a diesel and comes at a fixed price with no negotiation. The warranty covers 10,000 Km, and it's already serviced with an oil change. The name transfer will be done to your home address, and we'll provide you with the agreement.

Customer: Where are you from?

Salesperson: I'm from Mangalore. This is a 2010 model, diesel, priced at Rs. 340,000. The petrol version costs Rs. 662,000. The starting model is Rs. 662,000. How much does a new one cost?

Customer: Around Rs. 12,000.

Salesperson: The new one costs Rs. 18,000. You can take a test drive of the vehicle you like.

Customer: Can I see the car?

Salesperson: Absolutely. Here it is.

Customer: Hmm, the paint job seems a bit off, and there are some scratches. Also, the interior isn't very clean.

Salesperson: I apologize for that. We can have the paint job touched up and the interior thoroughly cleaned before delivery. Would that be acceptable?

Customer: That sounds better. I'll think about it.

Salesperson: Sure, take your time. If you decide to book today, just let us know. We can finalize everything for you.

Customer: Alright, I'll get back to you soon.
"""
#for conv3.txt in Google Docs
# Process the hackathon_match
process_hackathon_match(hackathon_match)
