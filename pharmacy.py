import requests
import pandas as pd 

pharmacy_data = []

for i in range(1, 100):
    url = f'https://pharmeasy.in/api/otc/getCategoryProducts?categoryId=113&page={i}'

    response = requests.get(url)
    json_data = response.json()
    products = json_data['data']['products']

    
    for i in range(20):
        name = products[i]['name']
        price = products[i]['mrpDecimal']
        discount = products[i]['discountDecimal']
        image = products[i]['damImages'][0]['url']

        pharmacy_data.append([name, price, discount, image])
    df = pd.DataFrame(pharmacy_data, columns=['Name', 'Price', 'Discount', 'Image'])
    df.to_csv('Pharmacy-details.csv', index=False)

    print(pharmacy_data)