#JSON format for conv1 evaluation summary
#Team 17- Rishikesha S B , Gopi E
#for Conv1-11 in Google Docs:
Customer_Extract1=  {}
Customer_Extract1['Car_Info']= {
    'Car_Type': 'Hatchback',
    'Car_Color': 'Black',
    'Car_Name': 'I-20',
    'Fuel_Type': 'Diesel Variant',
    'Mileage': '50 km/l',
    'Fuel_TankCapacity': '60 litres',
    'Distance_Travelled': '5755 kms',
    'Make_Year': '2020',
    'Transmission_Type': 'Automation Transmission'
}
Salesperson_Extract= {}
Salesperson_Extract['Policies']= {
    'Vehicle_Select': 'Hatchback',
    'Finance_Option': 'Loan on Interest',
    'Trade-in_Exchange': 'Old Tiago in Replacement for new I-20',
    'Insurance_Discussion': '2 years worth of Insurance funding scheme',
    'Pricing_Negotiation': '12,000 rs. to 32,000 rs. deduction from 6,00,000 rs',
    'Documentation': 'Buyer Agrees to Buy the Car',
    'Delivery': 'Car Delivery done in 1 week',
    'Sales_Support_Contact': 'Assistance and Call Customer Service provided',
    'Customer_Satisfaction': '8/10',
    'Performance': 'Well managed in selling the Car to the customer'
    }
Customer_Objections= {}
Customer_Objections['ReportObjectives']= {
    'Price': '5,68,000',
    'Finance': 'Interest of 6.5% with a 2 year extra allowance',
    'Trade-inValue': 'Tiago sold for 2,00,000 rs. against valued 1,20,000 rs.',
    'Insurance_Scheming': 'Lower Cost of Insurance accessed for the Car Purchase',
    'Features': 'Added Features to the new Car',
    'Maintanance': 'Additional Maintance and Services provided',
    'Fuel': 'Changed to Diesel Variant',
    }
import json
X= json.dumps(Customer_Extract1)
Y= json.dumps(Salesperson_Extract)
Z= json.dumps(Customer_Objections)
print("Customer Info Details in JSON as: ", X,"\n\nSalespersons Info Details in JSON as: ",Y,"\n\nCustomer Objections Info Details in JSON as: ",Z)

    
