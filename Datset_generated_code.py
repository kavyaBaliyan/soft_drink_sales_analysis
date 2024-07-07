#!/usr/bin/env python
# coding: utf-8

# In[3]:


from faker import Faker
import random
from openpyxl import Workbook
from datetime import datetime, time

fake = Faker()

# Function to generate a sequential transaction ID
def generate_transaction_id(index):
    return index + 1  # Start from 1 onwards

# Function to generate a random transaction date
def generate_transaction_date():
    start_date = datetime(2022, 4, 1).date()  # Financial year start date (April 1, 2022)
    end_date = datetime(2023, 3, 31).date()   # Financial year end date (March 31, 2023)
    return fake.date_between_dates(date_start=start_date, date_end=end_date)

# Function to generate a random transaction time
def generate_transaction_time():
    return fake.time_object().strftime('%H:%M:%S')

# Function to generate a random store ID (unique)
store_ids = set()
def generate_store_id():
    store_id = random.randint(1, 10000)
    while store_id in store_ids:
        store_id = random.randint(1, 10000)
    store_ids.add(store_id)
    return store_id

# Function to generate a random store location
def generate_store_location():
    return fake.city()

# Function to generate a random product ID (unique)
product_ids = set()
def generate_product_id():
    product_id = random.randint(1, 10000)
    while product_id in product_ids:
        product_id = random.randint(1, 10000)
    product_ids.add(product_id)
    return product_id

# Function to generate a random unit price
def generate_unit_price():
    return round(random.uniform(10, 100), 2)

# Function to generate a random product category, type, and name
def generate_product_details():
    categories = [
        "Carbonated Soft Drinks (CSDs)",
        "Non-Carbonated Soft Drinks",
        "Energy and Sports Drinks",
        "Juice and Juice Drinks",
        "Water and Sparkling Water",
        "Dairy and Plant-Based Beverages",
        "Specialty Drinks"
    ]

    types = {
        "Carbonated Soft Drinks (CSDs)": ["Cola", "Fruit Flavor", "Root Beer", "Ginger Ale"],
        "Non-Carbonated Soft Drinks": ["Iced Tea", "Coffee", "Juice Drink", "Energy Drink"],
        "Energy and Sports Drinks": ["Energy Drink", "Sports Drink"],
        "Juice and Juice Drinks": ["Fruit Juice", "Juice Blend", "Nectar Drink"],
        "Water and Sparkling Water": ["Still Water", "Sparkling Water", "Flavored Seltzer Water"],
        "Dairy and Plant-Based Beverages": ["Milk", "Yogurt Drink", "Plant-Based Milk"],
        "Specialty Drinks": ["Fermented Drink", "Vegetable Juice", "Coconut Water"]
    }

    product_names = {
        "Cola": ["Coca-Cola", "Pepsi"],
        "Fruit Flavor": ["Sprite", "Fanta"],
        "Root Beer": ["A&W", "Barq's"],
        "Ginger Ale": ["Canada Dry", "Vernors"],
        "Iced Tea": ["Lipton", "Arizona"],
        "Coffee": ["Starbucks", "Dunkin'"],
        "Juice Drink": ["Minute Maid", "Tropicana"],
        "Energy Drink": ["Red Bull", "Monster"],
        "Sports Drink": ["Gatorade", "Powerade"],
        "Fruit Juice": ["Orange Juice", "Apple Juice"],
        "Juice Blend": ["Fruit Punch", "Tropical"],
        "Nectar Drink": ["Apricot Nectar", "Peach Nectar"],
        "Still Water": ["Aquafina", "Dasani"],
        "Sparkling Water": ["Perrier", "San Pellegrino"],
        "Flavored Seltzer Water": ["LaCroix", "Spindrift"],
        "Milk": ["Whole Milk", "Skim Milk"],
        "Yogurt Drink": ["Smoothie", "Kefir"],
        "Plant-Based Milk": ["Almond Milk", "Soy Milk"],
        "Fermented Drink": ["Kombucha", "Kefir"],
        "Vegetable Juice": ["V8", "Tomato Juice"],
        "Coconut Water": ["Zico", "Vita Coco"]
    }

    category = random.choice(categories)
    product_type = random.choice(types[category])
    product_name = random.choice(product_names[product_type])

    return category, product_type, product_name

# Generate dataset of soft drink sales
num_records = 10000
sales_data = []

for index in range(num_records):
    category, product_type, product_name = generate_product_details()
    record = {
        'transaction_id': generate_transaction_id(index),
        'transaction_date': generate_transaction_date(),
        'transaction_time': generate_transaction_time(),
        'transaction_qty': random.randint(1, 50),
        'store_id': generate_store_id(),
        'store_location': generate_store_location(),
        'product_id': generate_product_id(),
        'unit_price': generate_unit_price(),
        'product_category': category,
        'product_type': product_type,
        'product_name': product_name
    }
    sales_data.append(record)

# Write data to an Excel file
excel_filename = 'soft_drink_sales_dataset.xlsx'
wb = Workbook()
ws = wb.active
ws.append(list(sales_data[0].keys()))  # Append header row

for data in sales_data:
    ws.append(list(data.values()))

wb.save(excel_filename)

print(f"Dataset generated and saved to '{excel_filename}'")


# In[ ]:




