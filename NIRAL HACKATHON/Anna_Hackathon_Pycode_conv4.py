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
Salesperson: Good afternoon, sir! How can I assist you today?

Customer: I'm here to check out the car you mentioned over the phone.

Salesperson: Absolutely, sir. The Swift 2019 model, right? Is it the ZXI variant you're interested in?

Customer: Yes, that's correct.

Salesperson: Great! Just to clarify, it's not the WB registeration, it's the KN registeration. You've seen it already, correct?

Customer: Yes, I have. But I noticed something about the paint job.

Salesperson: Ah, I see. The car number is 7064. It has been repainted, but rest assured, it hasn't been in any accidents. There are some scratches and dents, but nothing major. This model is automatic, not manual.

Customer: I see. What about the other details?

Salesperson: This is the 693, 2019 model VXI. It's a single-owner vehicle, Rathombath model, and has been used for 12 years. All modifications, including the roof color and paint, are aftermarket.

Customer: And the key? Can I take a look inside?

Salesperson: Of course, sir. You just need to open it with the key. By the way, this car has already been booked. But let me show you another option. Here we have a 2022 model ZXI, ZXI Plus, priced at 8 lakhs.

Customer: 2022 model? What's the mileage and condition?

Salesperson: Yes, sir. It's a 2022 model with only 16,000 kms on it. It's a single-owner, complete top-end model, ZXI Plus, and the price has dropped to 8 lakhs.

Customer: What about other options?

Salesperson: We also have a 21 model, front VX, R27, 693. It has been repainted and all modifications are aftermarket. You can keep looking around, and I'll be back in 10 minutes after lunch.

Customer: Alright, I'll take a look. Can I get your mobile number?

Salesperson: Sure, sir. It's 575***666. Please keep watching, and take a photo of the number plate if you need. Not all vehicles have been opened yet.

Customer: Thanks. What about this grey VXI from the front? It's a 21 model, right?

Salesperson: Yes, sir. That's correct. Please have a seat in the front. By the way, where's your mobile number? Who took your vehicle?

Customer: My number is 97***906. How much is this one?

Salesperson: It's priced at 50. I've given you all the information about the car. You can stand here while I walk you through the details.

Customer: Do you think the belts are loose?

Salesperson: No, no, sir. That's quite common. The company's code is 21. You'll get around 18 km/l on the highway, 17-18 in Bangalore.

Customer: Alright. Anything else I should know?

Salesperson: Just a tip, sir. Use only your right leg while driving; using the left leg can confuse the system. This car is priced at 6,69,300 and it comes with a 1-year warranty for the engine and gearbox. It's already been serviced at 12,000 kms, and the next service is due at 22,000 kms.

Customer: Sounds good. But why is the booking amount 10,000?

Salesperson: It's because of the loan process, sir. Do you have my number? Please call me if you decide to book.

Customer: Alright, I'll think about it. Thank you.

Salesperson: Thank you, sir. Have a great day!
conv4.txt
Open with Google Docs
 Share
Displaying conv4.txt.
"""
#for conv4.txt in Google Docs
# Process the hackathon_match
process_hackathon_match(hackathon_match)
