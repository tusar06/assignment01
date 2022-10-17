import random
mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}
#  Your Code Starts from here
#Random number generate
random_number_sequence = [0,1,2,3,4,5]
i=random.choice(random_number_sequence)

#Row wise mobile data
row_mobile_data= (mobile_data['data'][i])

#distinguish usd amount from strong
bdt_amount=''.join([i for i in row_mobile_data.get('price') if i.isdigit()])
#USD to bdt currency conversion
in_bd_tk=round(float(bdt_amount)*mobile_data['exchnage_rate'])

#Main template
template=f'''{row_mobile_data.get('name')} is made in {row_mobile_data.get('made')}. The price is {row_mobile_data.get('price')} Which is almost equal to {(in_bd_tk)} BDT.'''
print(template)