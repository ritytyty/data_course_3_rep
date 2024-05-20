import pandas as pd
from data_read_and_process import daily_sales, prices


#Для второго графика рассчитываю суммы ТО и себестоимости продаж, далее рассчитываю revenue (прибыль)
daily_sales['sales'] = daily_sales['unit_sold'] * daily_sales['price']
daily_sales['cost'] = daily_sales['unit_sold'] * daily_sales['cost']
daily_sales['revenue'] = daily_sales['sales']  - daily_sales['cost']


 #Для первого графика (динамика продаж в руб.) делаю фрейм с суммой продаж по дням
daily_sales_date = (
    daily_sales.groupby("date")
    .agg(
        sum_sales=("sales", "sum"),
        sum_cost=("cost", "sum"),
        sum_revenue=("revenue", "sum"),
    )
    .reset_index()
)

#Для третьего рассчитываю ТН,%
daily_sales_date['tn'] = 100 * (daily_sales_date['sum_revenue'] / daily_sales_date['sum_cost'])
 
#Для четвертого графика рассчитаю изменение средней стоимости реализации товара
daily_sales['sale_price'] = daily_sales['sales']/daily_sales['unit_sold']

prices_avg = daily_sales.groupby('date').agg(avg_price =('sale_price','mean')).reset_index().sort_values(by='date')
prices_avg['old_price'] = prices_avg['avg_price'].shift(1)
prices_avg['price_delta'] = prices_avg['avg_price'] - prices_avg['old_price']
prices_avg.dropna(inplace=True)

#Рассчитаем общую ТН по компании, воспользуюсь суммами по датафрейму и возьму последнюю ТН
tn_df = 100* (daily_sales_date['sum_revenue'].cumsum()/ daily_sales_date['sum_cost'].cumsum())
tn_df  = tn_df.tail(1)

#Рассчитаем остаток товаров  на складе по датам:

min_date = daily_sales.groupby(['sku']).agg(min_date=('date', 'min')).reset_index()
min_date['start_sumqty'] = 3000

daily_sales['day_saldo'] = daily_sales['delivered_units']  - daily_sales['unit_sold'] +  daily_sales['returns']
daily_sales['sum_day_saldo'] = daily_sales.groupby('sku')['day_saldo'].cumsum()
daily_sales = daily_sales.merge(min_date[['sku','start_sumqty']], on = 'sku', how = 'left')
daily_sales['day_sumqty'] = daily_sales['start_sumqty'] + daily_sales['sum_day_saldo']

sumqty_df = daily_sales.groupby('date').agg(sum_qty_day = ('day_sumqty', 'sum')).reset_index().sort_values(by='date')
sumqty_df['old_sumqty'] = sumqty_df['sum_qty_day'].shift(1)


