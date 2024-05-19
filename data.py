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


#Для второго графика рассчитываю суммы ТО и себестоимости продаж, далее рассчитываю revenue (прибыль)
daily_sales['sales'] = daily_sales['unit_sold'] * daily_sales['price']
daily_sales['cost'] = daily_sales['unit_sold'] * daily_sales['cost']
daily_sales['revenue'] = daily_sales['sales']  - daily_sales['cost']

#Преобразую дату в красивый вид
daily_sales['date'] = daily_sales['date'].apply(lambda x: str(x)[:10])
 #Для первого графика (динамика продаж в руб.) делаю фрейм с суммой продаж по дням
daily_sales_date = daily_sales.groupby('date').agg(sum_sales =('sales' ,'sum'), 
                                                   sum_cost =('cost' ,'sum'),
                                                   sum_revenue =('revenue' ,'sum')
                                                   ).reset_index()

#Для третьего рассчитываю ТН,%
daily_sales_date['tn'] = 100 * (daily_sales_date['sum_revenue'] / daily_sales_date['sum_cost'])
 
#Для четвертого графика рассчитаю изменение средней стоимости реализации товара
daily_sales['sale_price'] = daily_sales['sales']/daily_sales['unit_sold']

prices_avg = daily_sales.groupby('date').agg(avg_price =('sale_price','mean')).reset_index().sort_values(by='date')
prices_avg['old_price'] = prices_avg['avg_price'].shift(1)
prices_avg['price_delta'] = prices_avg['avg_price'] - prices_avg['old_price']
prices_avg.dropna()

#prices_avg['date'] = prices_avg['date'].apply(lambda x: str(x)[:10])
#print(daily_sales_date['sum_sales'].loc[daily_sales_date['date']=='2024-04-30'])

 