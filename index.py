from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from app import app
from data import daily_sales_date, daily_sales, prices_avg

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    df = daily_sales[daily_sales.date == value]

    return px.bar(df.sort_values(by = 'revenue', ascending = False), 
                  x = 'name', 
                  y='revenue', 
                  color = 'name',
                  title = 'Прибыль по товарам, руб. в разрезе дней', 
                  labels={'revenue':'Прибыль, руб.', 'name':'Наименование товара'},
                  text = df['revenue'].apply(lambda x: f'{x:.2f} руб'))

@callback(
    Output('r-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_item_param(value):  
    if value == '1': #'Динамика ТН по дням': 
        df_tn = daily_sales_date              
        bar_fig =  px.bar(df_tn, 
                        x = 'date', 
                        y ='tn', 
                        #title = 'Себестоимость по позиции, руб. в разрезе дней', 
                        labels={'tn':'Торговая надбавка, %.'},
                        text = df_tn['tn'].apply(lambda x: f'{x:.0f} %')
                        ) 
        return bar_fig
    else:  #Динамика изменения цены
        df_price = prices_avg
        bar_fig =  px.bar(df_price, 
                    x = 'date', 
                    y='price_delta', 
                    #title = 'Себестоимость по позиции, руб. в разрезе дней', 
                    labels={'price_delta':'Изменение цены, руб.'}
                    #text = df_price['price_delta'].apply(lambda x: f'{x:.2f} руб')
                    )
        return bar_fig

#def update_item_param(selected_value):
#    df_r = daily_sales[daily_sales.name == selected_value]
#
#    return px.line(df_r, 
#                  x = 'date', 
#                  y='cost', 
#                  title = 'Себестоимость по позиции, руб. в разрезе дней', 
#                  labels={'cost':'Себестоимость, руб.', 'name':'Наименование товара'}
#                  #text = df_r['cost'].apply(lambda x: f'{x:.2f} руб')
#                  )


if __name__ == '__main__':
    app.run(debug=True) 