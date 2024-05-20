import pandas as pd

#Загружаю данные
prices = pd.read_csv('data/prices.csv', sep = ",")
costs = pd.read_csv('data/costs.csv', sep = ",")
daily_sales = pd.read_csv('data/daily_sales.csv', sep = ",")
products = pd.read_json('data/products.json')

#Преобразую данные перед мерджем в датовый тип 
daily_sales['date'] = pd.to_datetime(daily_sales['date'])
prices['date'] = pd.to_datetime(prices['date'])
costs['date'] = pd.to_datetime(costs['date'])

#Подтягиваю данные о себестоимости, розничной цене, наименовании товара, на основе этих данныз буду строить графики
daily_sales = daily_sales.merge(prices, on=['sku','date'], how ='inner')
daily_sales = daily_sales.merge(costs, on=['sku','date'], how ='inner')
daily_sales = daily_sales.merge(products, on=['sku'], how ='inner')

#Преобразую дату в красивый вид
daily_sales['date'] = daily_sales['date'].apply(lambda x: str(x)[:10])

