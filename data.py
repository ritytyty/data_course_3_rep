import pandas as pd

prices = pd.read_csv('data/prices.csv', sep = ",")
daily_sales = pd.read_csv('data/daily_sales.csv', sep = ",")
products = pd.read_json('data/products.json')

#daily_sales['date'] = pd.to_datetime(daily_sales['date'])
#daily_sales['date'] = daily_sales['date'].dt.date
#daily_sales['dw'] = pd.to_datetime(daily_sales['date']).dt.day_of_week

#daily_sales['date'] = daily_sales['date'].apply(lambda x: str(x)[:10])
daily_sales_dateqty  = daily_sales.groupby('date').agg(sum_sales =('unit_sold' ,'sum')).reset_index()
daily_sales_dateqty['date'] = daily_sales_dateqty['date'].apply(lambda x: str(x)[:10])
#sales_df['sku'] = sales_df['sku'].astype('str')
#print(daily_sales_dateqty)
#daily_sales_dateqty  = daily_sales.groupby('date').agg(sum_sales =('unit_sold' ,'sum')).reset_index()

