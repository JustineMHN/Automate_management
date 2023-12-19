import os
import json
import random
import datetime
import matplotlib.pyplot as plt
import numpy as np

transaction_data = {
    "transactions": [
        {
            "date": "2023-10-20",
            "product_id": "product_A2",
            "total_amount": 5.18
        },
        {
            "date": "2023-10-20",
            "product_id": "product_A1",
            "total_amount": 5.18
        },
        {
            "date": "2023-10-20",
            "product_id": "product_A5",
            "total_amount": 5.18
        },
        {
            "date": "2023-10-20",
            "product_id": "product_C3",
            "total_amount": 13.6
        },
        {
            "date": "2023-10-20",
            "product_id": "product_C7",
            "total_amount": 2.41
        },
        {
            "date": "2023-10-20",
            "product_id": "product_A6",
            "total_amount": 3.77
        },
        {
            "date": "2023-10-20",
            "product_id": "product_B3",
            "total_amount": 18.59
        },
        {
            "date": "2023-10-20",
            "product_id": "product_B2",
            "total_amount": 19.08
        },
        {
            "date": "2023-10-20",
            "product_id": "product_C5",
            "total_amount": 7.3
        },
        {
            "date": "2023-10-19",
            "product_id": "product_A1",
            "total_amount": 3.77
        },
        {
            "date": "2023-10-19",
            "product_id": "product_B7",
            "total_amount": 18.59
        },
        {
            "date": "2023-10-19",
            "product_id": "product_B1",
            "total_amount": 19.08
        },
        {
            "date": "2023-10-19",
            "product_id": "product_C7",
            "total_amount": 7.3
        },
        {
            "date": "2023-10-19",
            "product_id": "product_A6",
            "total_amount": 3.77
        },
        {
            "date": "2023-10-19",
            "product_id": "product_B3",
            "total_amount": 18.59
        },
        {
            "date": "2023-10-19",
            "product_id": "product_B2",
            "total_amount": 19.08
        },
        {
            "date": "2023-10-19",
            "product_id": "product_C5",
            "total_amount": 7.3
        },
        {
            "date": "2023-10-19",
            "product_id": "product_C3",
            "total_amount": 5.05
        },
        {
            "date": "2023-10-18",
            "product_id": "product_B5",
            "total_amount": 1.36
        },
        {
            "date": "2023-10-18",
            "product_id": "product_A5",
            "total_amount": 5.18
        },
        {
            "date": "2023-10-18",
            "product_id": "product_C3",
            "total_amount": 13.6
        },
        {
            "date": "2023-10-18",
            "product_id": "product_C7",
            "total_amount": 2.41
        },
        {
            "date": "2023-10-18",
            "product_id": "product_B4",
            "total_amount": 3.15
        },
        {
            "date": "2023-10-17",
            "product_id": "product_C3",
            "total_amount": 2.21
        },
        {
            "date": "2023-10-17",
            "product_id": "product_A2",
            "total_amount": 18.96
        },
        {
            "date": "2023-10-17",
            "product_id": "product_C3",
            "total_amount": 3.4
        },
        {
            "date": "2023-10-17",
            "product_id": "product_C5",
            "total_amount": 3.29
        },
        {
            "date": "2023-10-17",
            "product_id": "product_B3",
            "total_amount": 17.8
        },
        {
            "date": "2023-10-17",
            "product_id": "product_C2",
            "total_amount": 11.3
        },
        {
            "date": "2023-10-16",
            "product_id": "product_A6",
            "total_amount": 1.18
        },
        {
            "date": "2023-10-16",
            "product_id": "product_A5",
            "total_amount": 4.24
        },
        {
            "date": "2023-10-16",
            "product_id": "product_B6",
            "total_amount": 17.69
        },
        {
            "date": "2023-10-16",
            "product_id": "product_B4",
            "total_amount": 4.58
        }
    ],
    "billings": [
        {
            "date": "2023-10-16",
            "total_amount": 3.0,
            "payment_method": "Credit Card"
        },
        {
            "date": "2023-10-15",
            "total_amount": 2.5,
            "payment_method": "Cash"
        }
    ]
}
information_data = {
    "available_products": {
        "product_A1": {
            "name": "Soda",
            "quantity": 10,
            "price": 1.5
        },
        "product_A2": {
            "name": "Chips",
            "quantity": 10,
            "price": 2.0
        },
        "product_A3": {
            "name": "Candy Bar",
            "quantity": 0,
            "price": 1.0
        },
        "product_A4": {
            "name": "Bottled Water",
            "quantity": 10,
            "price": 1.0
        },
        "product_A5": {
            "name": "Coffee",
            "quantity": 10,
            "price": 1.8
        },
        "product_A6": {
            "name": "Tea",
            "quantity": 10,
            "price": 1.2
        },
        "product_A7": {
            "name": "Juice",
            "quantity": 10,
            "price": 2.5
        },
        "product_B1": {
            "name": "Cookies",
            "quantity": 10,
            "price": 1.3
        },
        "product_B2": {
            "name": "Sandwich",
            "quantity": 10,
            "price": 4.0
        },
        "product_B3": {
            "name": "Fruit Salad",
            "quantity": 10,
            "price": 3.5
        },
        "product_B4": {
            "name": "Energy Drink",
            "quantity": 10,
            "price": 2.7
        },
        "product_B5": {
            "name": "Muffin",
            "quantity": 10,
            "price": 1.7
        },
        "product_B6": {
            "name": "Popcorn",
            "quantity": 10,
            "price": 1.5
        },
        "product_B7": {
            "name": "Ice Cream",
            "quantity": 10,
            "price": 3.2
        },
        "product_C1": {
            "name": "Yogurt",
            "quantity": 10,
            "price": 2.3
        },
        "product_C2": {
            "name": "Pizza Slice",
            "quantity": 10,
            "price": 3.8
        },
        "product_C3": {
            "name": "Salad",
            "quantity": 10,
            "price": 4.5
        },
        "product_C4": {
            "name": "Fruit Juice",
            "quantity": 10,
            "price": 1.9
        },
        "product_C5": {
            "name": "Pretzels",
            "quantity": 10,
            "price": 1.2
        },
        "product_C6": {
            "name": "Cupcakes",
            "quantity": 10,
            "price": 2.2
        },
        "product_C7": {
            "name": "Granola Bar",
            "quantity": 10,
            "price": 1.1
        }
    },
    "last_restock_date": "2023-10-15",
    "status": "Available"
}
price_data = {
    "product_A1": 1.5,
    "product_A2": 2.0,
    "product_A3": 1.0,
    "product_A4": 1.0,
    "product_A5": 1.8,
    "product_A6": 1.2,
    "product_A7": 2.5,
    "product_B1": 1.3,
    "product_B2": 4.0,
    "product_B3": 3.5,
    "product_B4": 2.7,
    "product_B5": 1.7,
    "product_B6": 1.5,
    "product_B7": 3.2,
    "product_C1": 2.3,
    "product_C2": 3.8,
    "product_C3": 4.5,
    "product_C4": 1.9,
    "product_C5": 1.2,
    "product_C6": 2.2,
    "product_C7": 1.1
}

#Creation du server
os.mkdir('Server')

# Creation des dossiers machine sur le server
for i in range(1, 16):
    lat = round(random.uniform(40.3045, 72.2345), 8)
    lon = round(random.uniform(-179.4357, -110.0987), 8)
    ID = str(lat) + '_' + str(lon) + '_1'
    os.mkdir('Server/'+ID)

#Creation du dossier ip_config dans le server
os.mkdir('Server/ip_config')

# Creation des fichiers des dossiers machine
for i in os.listdir('Server'):
    transaction = json.dumps(transaction_data, indent=4)
    information = json.dumps(information_data, indent=4)
    price = json.dumps(price_data)
    open('Server/' + i + '/Transaction.json', "w+").write(transaction)
    open('Server/' + i + '/Information.json', "w+").write(information)
    if i == 'ip_config':
        os.remove('Server/' + i + '/Transaction.json')
        os.remove('Server/' + i + '/Information.json')
        open('Server/' + i + '/Prices.json', "w+").write(price)


def Add(ID):
    if not os.path.exists('Server/' + ID):
        os.mkdir('Server/' + ID)
        open('Server/' + ID).write(json.dumps(transaction_data, indent=4))
        open('Server/' + ID).write(json.dumps(information_data, indent=4))
        print("Machine : " + ID + " has been successfully created in the Server")
    else:
        print("Machine : " + ID + " already existed in the Server")


def Repricing(XI, price):
    som = 0
    with open('Server/ip_config/Prices.json', 'r') as price_file:
        try:
            prices = json.load(price_file)
            for product_name in prices:
                if XI == product_name:
                    prices[str(product_name)] = price
                    price_file = open('Server/ip_config/Prices.json', 'w')
                    json.dump(prices, price_file, indent=4)
                    print("Product " + XI + "'price successful updated in the prices.json file")
                    for id in os.listdir('Server'):
                        if os.path.isdir('Server/' + id) and os.path.exists('Server/' + id + '/Information.json'):
                            with open('Server/' + id + '/Information.json', 'r') as info_file:
                                data = json.load(info_file)
                                for product_name in data['available_products']:
                                    if product_name == XI:
                                        data['available_products'][str(XI)]['price'] = price
                                        info_file = open('Server/' + id + '/Information.json', 'w')
                                        json.dump(data, info_file, indent=4)
                                        som += 1
                                    else:
                                        continue
                    print("Product " + XI + "'price has been successful updated in", som, "machines\n")
                    return
                else:
                    continue
            print("Product " + XI + " doestn't exist in the server!")
            return
        except :
            print("File cannot be read or doesn't exist")


def Sell(ID, Xi):
    infofilepath = 'Server/' + ID + '/Information.json'
    transfilepath = 'Server/' + ID + '/Transaction.json'
    if os.path.isdir('Server/' + ID) and os.path.exists(infofilepath):
        with open(infofilepath, 'r') as info_file:
            data = json.load(info_file)
            for product in data['available_products']:
                if product == Xi:
                    qty = data['available_products'][str(product)]['quantity']
                    if qty > 0:
                        print(datetime.datetime.now(), Xi, 'sold in machine', ID, 'for',
                              data['available_products'][str(product)]['price'], 'euro')
                        qty = qty - 1
                        data['available_products'][str(product)]['quantity'] = qty
                        info_file = open(infofilepath, 'w')
                        json.dump(data, info_file, indent=4)
                        transfile = open(transfilepath, 'r')
                        transdata = json.load(transfile)
                        trans_file = open(transfilepath, 'w+')
                        product_found = False
                        for item in range(len(transdata['transactions'])):
                            if transdata['transactions'][item]['date'] == str(datetime.date.today()) and \
                                    transdata['transactions'][item]['product_id'] == Xi:
                                transdata['transactions'][item]['total_amount'] += round(
                                    data['available_products'][str(product)]['price'], 3)
                                product_found = True
                                break
                        if not product_found:
                            sale_data = {
                                "date": str(datetime.date.today()),
                                "product_id": Xi,
                                "total_amount": data['available_products'][str(product)]['price']
                            }
                            transdata['transactions'].append(sale_data)
                        json.dump(transdata, trans_file, indent=4)
                    else:
                        print("Stock terminé")
                else:
                    continue
    else:
        print('Machine ' + ID + ' does not exist')


def Refill_(ID, Xi, Date=datetime.date.today()):
    recharges = False
    XI = []
    if ID == -1:
        for id in os.listdir('Server'):
            if os.path.isfile('Server/' + id + '/Information.json'):
                XI.append(id)
    else:
        XI = ID

    for id in XI:
        if os.path.isfile('Server/' + id + '/Information.json'):
            with open('Server/' + id + '/Information.json', 'r') as info_file:
                data = json.load(info_file)
                for item in Xi:
                    for product in data['available_products']:
                        if item == product and data['available_products'][str(product)]['quantity'] < 10:
                            qty = data['available_products'][str(product)]['quantity']
                            data['available_products'][str(product)]['quantity'] = (10 - qty) + qty
                            data['last_restock_date'] = str(Date)
                            info_file = open('Server/' + id + '/Information.json', 'w')
                            json.dump(data, info_file, indent=4)
                            recharges = True
        else:
            if id == 'ip_config':
                continue
            else:
                print("File", 'Server/' + id + '/Information.json', "doesn't exist or unreadable")
    print("Machine(s) recharged") if recharges else print("Machine(s) not recharged")


def Revenues(ID, Xi, Date_start, Date_end):
    total_revenue = 0
    dates = []
    product_list = []
    Id = ['Server/'+machine+'/Transaction.json' for machine in os.listdir('Server')] if ID == -1 else [ID]
    for id in Id:
        ID = str(id.split('Server/')[1].split('/Transaction.json')[0])
        total_revenue = 0
        if os.path.exists(id) and os.path.isfile(
                id):
            with open(id, 'r') as trans_file:
                data = json.load(trans_file)
                XI = [product['product_id'] for product in data['transactions']] if Xi == -1 else Xi
                for item in XI:
                    revenue = 0
                    for product in data['transactions']:
                        if item == str(product['product_id']) and Date_start <= product['date'] <= Date_end:
                            revenue += product['total_amount']
                            total_revenue += product['total_amount']
                            dates.append(product['date'])
                            dates = list(set(dates))
                            dates.sort()
                    product_list.append(f"{item} => {revenue}")
                print('Machine:', ID, 'Total.Revenue:', total_revenue)
                print(product_list)
                print("*********************************")
                product_dict = [i.split('=>')[0] for i in product_list]
                print(product_dict)
                revenue_dict = [i.split('=>')[1] for i in product_list]
                print(revenue_dict)
                product_list.clear()
                # Sort the data in ascending order based on revenue
                sorted_data = sorted(zip(product_dict, revenue_dict), key=lambda x: x[1])
                # Unzip the sorted data
                product_dict, revenue_dict = zip(*sorted_data)
                plt.title('Revenue per product ID:'+ID)
                plt.bar(product_dict, revenue_dict)
                plt.xlabel('Product')
                plt.ylabel('Revenue')
                plt.xticks(rotation=45)
                plt.show()

        else:
            if id == 'Server/ip_config/Transaction.json':
                continue
            else:
                print("Machine",ID, "doesn't exist or unreadable")


def Available(ID, Xi):
    XI = []
    product_list = []
    if ID == -1:
        for id in os.listdir('Server'):
            if os.path.isfile('Server/' + id + '/Information.json'):
                Id = 'Server/' + id + '/Information.json'
                XI.append(Id)
    else:
        XI = ID

    for id in XI:
        if os.path.isfile(str(id)):
            with open(str(id), 'r') as info_file:
                data = json.load(info_file)
                for item in Xi:
                    for product in data['available_products']:
                        if item == product:
                            qty = data['available_products'][str(product)]['quantity'] * 100 / 10
                            product_list.append(f"{item} => {qty}%")

                        else:
                            continue
                print(id)
                print(product_list)
                product_list.clear()
        else:
            if id == 'ip_config':
                continue
            else:
                print("File", 'Server/' + id + '/Information.json', "doesn't exist or unreadable")

def Scan_to_refill(percentage, Xi):
    product_list = []
    for id in os.listdir('Server'):
        if os.path.isfile('Server/' + id + '/Information.json'):
            with open('Server/' + id + '/Information.json', 'r') as info_file:
                data = json.load(info_file)
                for item in Xi:
                    for product in data['available_products']:
                        if item == product:
                            qty = data['available_products'][str(product)]['quantity'] * 100 / 10
                            if qty > percentage:
                                product_list.append(product)
                        else:
                            continue
            print('Machine',id)
            print(product_list)
            product_list.clear()
            print("**********************")
        else:
            if id == 'ip_config':
                continue
            else:
                print("File", 'Server/' + id + '/Information.json', "doesn't exist or unreadable")


def Revenues_(ID,Xi,Date_start,Date_end):
    Id = [machine for machine in os.listdir('Server')] if ID == -1 else [ID]
    for id in Id:
        filepath = 'Server/'+id+'/Transaction.json'
        dates = []
        somme = 0
        if os.path.exists(filepath) and os.path.isfile(filepath):
            with open(filepath, 'r') as trans_data:
                data = json.load(trans_data)
                XI = [product['product_id'] for product in data['transactions']] if Xi == -1 else Xi
                for trans in data['transactions']:
                        if Date_start <= str(trans['date']) <= Date_end:
                            dates.append(trans['date'])
                            dates = list(set(dates))
                            dates.sort()
                revenues ={str(date):0.0 for date in dates}
                keys = list(revenues.keys())
                for productXi in XI:
                    for product in data['transactions']:
                        for date in dates:
                            if product['product_id'] == productXi and product['date'] == date:
                                somme+=product['total_amount']
                                for key in keys:
                                    if key == date:
                                        revenues[date] += product['total_amount']
                                        break
                                break
                revenue_date = keys
                revenue = [revenues[key] for key in keys]
                print('Machine : ',id)
                print('Total Revenue: ', somme)
                print('Revenue over time: ',revenues)
                print('******************************')
                plt.figure(figsize=(10,6))
                plt.plot(revenue_date, revenue)
                plt.title('Machine '+id+' Revenue Over Time: '+str(somme))
                plt.xlabel('Date')
                plt.ylabel('Revenue')
                plt.show()


print("____________________________________________________________________________________________________________\n")
print("__________________________________________AUTOMATE MANAGEMENT________________________________________________\n")
print("______________________________________________________________________________________________________________\n")

list_product = ["product_A5", "product_A1", "product_A3", "product_B1", "product_B3", "product_C3",
                "product_C7"]

list_machine = ['42.0448121_-147.45602335_1', '44.10261877_-164.66253273_1', '49.36263074_-148.3519846_1',
                '49.92641943_-174.0807346_1', '52.30527823_-156.27766111_1', '53.05555044_-148.3027917_1',
                '57.48466265_-125.08071602_1', '65.09144709_-129.71793261_1', '66.29431935_-179.00075778_1']

print("New machine added")
#Add("40.05207288_-129.40752718_1")
print("________________________________________________________________________________________________")
print("Repricing ")
#Repricing('product_A3', 2.0)
print("________________________________________________________________________________________________")
print("Selling ")
#Sell("42.0448121_-147.45602335_1", "product_C4")
print("________________________________________________________________________________________________")
print("Refilling ")
#Refill_(-1, list_product)
print("________________________________________________________________________________________________")
print("Revenues ")
Revenues(-1, -1, "2023-10-16", "2023-10-21")
print("________________________________________________________________________________________________")
print("Available products ")
#Available(-1, list_product)
print("________________________________________________________________________________________________")
print("Scan to refill ")
#Scan_to_refill(50, list_product)
print("________________________________________________________________________________________________")
#Revenues_('42.0448121_-147.45602335_1', list_product, "2023-10-16", "2023-10-20")
#Revenues_(-1, -1, "2023-10-16", "2023-10-20")




