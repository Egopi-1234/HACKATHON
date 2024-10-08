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
Salesperson: Good afternoon, sir. Here we have a Tigor for you. Please note that there are some scratches and this door has been repainted. This is a complete door replacement.

Customer: Tigor? Okay, sir.

Salesperson: Yes, sir. This is a standard Tigor model.

Customer: Is this an exchange model?

Salesperson: Yes, sir. The company claims a mileage of 23 km/l, but realistically, you can expect around 19-20 km/l.

Customer: How is the overall condition?

Salesperson: The visibility is clear, and the wheelbase is quite good.

Customer: Can you show me the service book?

Salesperson: Unfortunately, I don't have the service book with me right now. However, the ground clearance is 165 mm, similar to other Tigor models. It also has a boot space of 345 liters and a 1.5-liter engine with a 37-liter fuel tank capacity. This is a special dark edition.

Customer: Yes, sir.

Salesperson: It features a keyless start and cruise control.

Customer: Cruise control?

Salesperson: Yes, sir. It also has two airbags and an automatic wiper system.

Customer: Yes, sir.

Salesperson: The headlights are automatic, and it comes with both Android Auto and Apple CarPlay, though they are wired. It also has a reverse camera. The vehicle has been regularly serviced.

Customer: What about the previous owner?

Salesperson: The previous owner has been transferred to Rachel, but the car has been well-maintained with a service history up to 34,000 km.

Customer: What different driving modes are available?

Salesperson: It has an eco mode and a city drive mode. In eco mode, you get better mileage.

Customer: Is the engine the same?

Salesperson: Yes, sir. The engine is the same. This is the top-end model, available in XZ and XZ Plus variants.

Customer: What's the difference between XZ and XZ Plus?

Salesperson: The XZ Plus is the top model. Without the top model, you can't start from the bottom.

Customer: Does it come with a sunroof?

Salesperson: Yes, sir. The sunroof is optional and costs an additional 80,000 rupees.

Customer: Can I see the boot space?

Salesperson: Sure, the boot space is 345 liters. The spare tire is new and unused.

Customer: How much does the tire weigh?

Salesperson: The front tire weighs around 50 kg, and the rear tire is about 250 kg. This vehicle comes with a buyback option for 1, 2, or 3 years.

Customer: How does the buyback work?

Salesperson: The buyback is assured by the company. There is no touch-up on the bumper, and the engine is 1.5 liters.

Customer: Is the engine tampered with?

Salesperson: No, sir. The engine is not tampered with. We ensure 100% authenticity. YoCars does not procure tampered vehicles.

Customer: Okay.

Salesperson: Actually, I have a Polo as well.

Customer: Okay.

Salesperson: Yes, it is inside here.

Customer: Okay, sir.

Salesperson: Yes.

Customer: Yes, sir.

Salesperson: Please come with me.

Customer: Sir, what are the scratches?

Salesperson: They cover it with Teflon coating.

Customer: I don't know.

Salesperson: I don't know the price. There is no fixed price negotiation here. The price has already reached Rs. 9,97,000 on the screen. The price has dropped almost to Rs. 47,000. Another problem is that they don't have the body work.

Customer: It's good that you are advertising the price of the car.

Salesperson: There is no body work. Everyone is mentioned here. The door is repainted and the apple is mentioned. The door is repainted. The dent and scratches are not there. We are asking for the comparison. That's why we are asking for the price.

Customer: No sir, there is no negotiation in the price.

Salesperson: Benefits are 1 year warranty plus buyback 3 years, 2 years buyback. If you want 3 years you can extend. You also have extended warranty. Plus RC transfer is included. Plus for this vehicle, comprehensive insurance is valid. So you don't have to pay extra.

Customer: Fine sir.

Salesperson: Ok sir, I will ask.
"""
# for conv7.txt in Google Docs
# Process the hackathon_match
process_hackathon_match(hackathon_match)
