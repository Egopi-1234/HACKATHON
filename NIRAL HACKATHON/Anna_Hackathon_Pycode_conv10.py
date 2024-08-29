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

    print("\nCustomer Requirements:")
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
Salesperson: Hello sir, how are you today?

Customer: I'm good, thank you. What will be the registration process?

Salesperson: We will get the vehicle registered to KN. It's included in the price. Everything is included.

Customer: Okay, can we take a test drive of your car?

Salesperson: Yes, of course. Please have a seat. Have you visited YoCars Park before?

Customer: No, no. This is for my family. They want to check it out.

Salesperson: Alright, please have a seat. Who assisted you earlier?

Customer: Prashant.

Salesperson: Great. Prashant is one of our best. Please have a seat. Prashant, I am Pooch Rai. They are interested in a second car and they like YoCars.

Customer: They said Prashant. Who assisted you?

Salesperson: Prashant. Can I ask you something?

Customer: No, no. They want a family King Out Auto. Hasn't it started yet?

Salesperson: Yes, sir. Could I have your contact number for our records?

Customer: 7******139.

Salesperson: Thank you. No problem, just for logging purposes. Do you have a shortlist of cars you're interested in?

Customer: Just give me two minutes, ma'am. I will get the vehicle and I will call you.

Salesperson: Okay, I will call you.

Salesperson: Sir, we kept it just for display purposes. Sir, there is a stone. I think it will hit there.

Customer: Slowly, sir.

Salesperson: I have left you, ma'am.

Customer: Sir?

Salesperson: It has been leaked for the first time. It's too loose. There was greasing and all.

Customer: Is it too loose?

Salesperson: No, no. I mean, we brought an item. So, we have compared it. It differs from brand to brand. The steering is a bit tight in the Volkswagen, but it depends on the company. In the Tata, it is much smoother. I can turn it with one finger.

Customer: What is the vibration? Light vibration?

Customer: Clutch in the lower gear is vibrating. Do you want to try?

Salseperon: No, you stop here near the tree. We will check the engine and boot space.

Custoemr: No, you want to try once?

Salesperson: No, it's okay. You can see the engine from the inside. Start the engine from the inside.

Salesperson: It is not in gear. It started. You can see the power of the accelerator. It is 1.2. It is a powerful engine.

Customer: No, you stop here. You can turn the car.

Salesperson: No, you stop here. You can see the power of the accelerator.

Customer: No, you start from the inside.

Salesperson: No, you start from the inside.

Customer: No, you start from the inside.

Salesperson: You just drive.

Customer: I will.

Salesperson: No, you stop here.

Customer: I don't want to talk.

Salesperson: No, you stop here.

Customer: Then it will stand.

Salesperson: No, you stop here.

Customer: You stand.

Salesperson: Then I will move.

Customer: No, you speak.

Salesperson: No, you speak.

Customer: Then it will take a while.

Salesperson: No, you speak.

Customer: By the way, I find the price a bit expensive. Is there any room for negotiation?

Salesperson: I understand your concern, sir. However, our prices are fixed. But let me assure you, the price includes all the features and benefits our company offers. From registration to after-sales service, everything is covered.

Customer: Hmm, I see. That does sound comprehensive.

Salesperson: Absolutely, sir. We believe in providing value for your money. You won't have to worry about any hidden costs or additional charges later on.

Customer: Alright, that's good to know. Thank you.

Salesperson: You're welcome, sir. Now, shall we continue with the test drive?

Customer: Yes, let's do that.
"""
#for conv10.txt in Google Docs
# Process the hackathon_match
process_hackathon_match(hackathon_match)
