from dash import Dash, html, dcc, callback, Output, Input, ctx
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from app import app
from data_transform import daily_sales_date, daily_sales, prices_avg

@callback(
    Output("graph-content", "figure"),
    Input("dropdown-selection", "value"),
)
def update_graph(value):
    df = daily_sales.sort_values(by = 'revenue', ascending = False)
    
    if value: 
        df = df[df["date"] == value]
        title=f"Прибыль по позициям за дату: {value}"
    else:
        title=f"Прибыль по позициям"
        df = df.groupby("name").agg( revenue=("revenue", "sum")).reset_index()
        df.sort_values(by = 'revenue', ascending = False, inplace=True)
    item_bar = go.Figure()
    item_bar.add_trace (go.Bar(
            x=df["name"],
            y=df["revenue"],
            #marker=dict(color="blue"),
        )
    )
    for index, row in df.iterrows():
        item_bar.add_trace(go.Indicator(
            mode="number",
            value=row["revenue"],
            number={"prefix": "₽", "suffix": "k","font":{"size":25}},
            #domain={'x': 'name', 'y': [0, 1]},
            # domain={'x': [0, 1], 'y': [0.9-0.1*index, 0.9-0.1*(index+1)]}
            ))

    item_bar.update_layout(title=title, barmode = 'group')  
    return item_bar

#@callback(
#    Output('output-graph', 'figure'),
#    Input('tn-dynamic', 'n_clicks'),
#    Input('price-dynamic', 'n_clicks'),
#)
#def update_button_param(btn1_clicks, btn2_clicks):
#    button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
#    if button_id == 'tn-dynamic':   
#        print(button_id)    
#        df_tn = daily_sales_date              
#        bar_fig =  px.bar(df_tn, 
#                         x = 'date', 
#                         y ='tn', 
#                         #title = 'Себестоимость по позиции, руб. в разрезе дней', 
#                         labels={'tn':'Торговая надбавка, %.'},
#                         #text = df_tn['tn'].apply(lambda x: f'{x:.0f} %')
#                         ) 
#        return bar_fig
#        
#    elif button_id =='price-dynamic':
#        print(button_id)   
#        df_price = prices_avg
#        bar_fig =  px.bar(df_price, 
#                     x = 'date', 
#                     y='price_delta', 
#                     color = 'price_delta',
#                     #title = 'Себестоимость по позиции, руб. в разрезе дней', 
#                     labels={'price_delta':'Изменение цены, руб.'}
#                     #text = df_price['price_delta'].apply(lambda x: f'{x:.2f} руб')
#                     )
#        return bar_fig
 

   # button_id = ctx.triggered[0]['prop_id'].split('.')[0]
 #  if button_id == 'tn-dynamic':
 #      

 #  elif button_id == 'price-dynamic':
 #       df_price = prices_avg
 #       bar_fig =  px.bar(df_price, 
 #                      x = 'date', 
 #                      y='price_delta', 
 #                      color = 'price_delta',
 #                      #title = 'Себестоимость по позиции, руб. в разрезе дней', 
 #                      labels={'price_delta':'Изменение цены, руб.'}
 #                      #text = df_price['price_delta'].apply(lambda x: f'{x:.2f} руб')
 #                      )
 #       return bar_fig
        




#@callback(
#    Output('r-content', 'figure'),
#    Input('dropdown-selection_2', 'value'),
#    prevent_initial_call=True
#)
#def update_item_param(value):   
#    if value == '1': #'Динамика ТН по дням': 
#        df_tn = daily_sales_date              
#        bar_fig =  px.bar(df_tn, 
#                        x = 'date', 
#                        y ='tn', 
#                        #title = 'Себестоимость по позиции, руб. в разрезе дней', 
#                        labels={'tn':'Торговая надбавка, %.'},
#                        #text = df_tn['tn'].apply(lambda x: f'{x:.0f} %')
#                        ) 
#        return bar_fig
#    else:  #Динамика изменения цены
#        df_price = prices_avg
#        bar_fig =  px.bar(df_price, 
#                    x = 'date', 
#                    y='price_delta', 
#                    color = 'price_delta',
#                    #title = 'Себестоимость по позиции, руб. в разрезе дней', 
#                    labels={'price_delta':'Изменение цены, руб.'}
#                    #text = df_price['price_delta'].apply(lambda x: f'{x:.2f} руб')
#                    )
#        return bar_fig
    
#@callback(
#    Output('r-content', 'figure'),
#    Input('dropdown-selection_2', 'value'),
#    prevent_initial_call=True
#)
#def update_item_param(value):   
#    if value == '1': #'Динамика ТН по дням': 
#        df_tn = daily_sales_date              
#        bar_fig =  px.bar(df_tn, 
#                        x = 'date', 
#                        y ='tn', 
#                        #title = 'Себестоимость по позиции, руб. в разрезе дней', 
#                        labels={'tn':'Торговая надбавка, %.'},
#                        #text = df_tn['tn'].apply(lambda x: f'{x:.0f} %')
#                        ) 
#        return bar_fig
#    else:  #Динамика изменения цены
#        df_price = prices_avg
#        bar_fig =  px.bar(df_price, 
#                    x = 'date', 
#                    y='price_delta', 
#                    color = 'price_delta',
#                    #title = 'Себестоимость по позиции, руб. в разрезе дней', 
#                    labels={'price_delta':'Изменение цены, руб.'}
#                    #text = df_price['price_delta'].apply(lambda x: f'{x:.2f} руб')
#                    )
#        return bar_fig

if __name__ == '__main__':
    app.run(debug=True) 



    

#@callback(
#    Output('graph-content', 'figure'),
#    Input('dropdown-selection', 'value')
#)
#def update_graph(value):
#    df = daily_sales[daily_sales.date == value]
#
#    return px.bar(df.sort_values(by = 'revenue', ascending = False), 
#                  x = 'name', 
#                  y='revenue', 
#                  color = 'name',
#                  title = 'Прибыль по товарам, руб. в разрезе дней', 
#                  labels={'revenue':'Прибыль, руб.', 'name':'Наименование товара'},
#                  text = df['revenue'].apply(lambda x: f'{x:.2f} руб'))






        
#   dbc.DropdownMenu(
#       id='dropdown-selection',
#       label='Выберите дату',
#       children=[
#           dbc.DropdownMenuItem(date, id= 'dropdown-selection-item')
#           for  date in daily_sales['date']
#       ],
#   ),
#       dcc.Graph(id='graph-content'),
#
#callback(
#   Output('graph-content', 'figure'),
#   Input('dropdown-selection-item', 'value')
#
#ef update_graph(selected_date):
#   df = daily_sales_date[daily_sales_date['date'] == selected_date]
#   item_bar = go.Figure(go.Scatter(
#                           x = df['name'],
#                           y = df['revenue'],
#                           color = 'name',
#                           mode='markers+lines',
#                           marker=dict(color='blue')
#                            )
#   )
#   item_bar.update_layout(title=f'Daily Sales for {selected_date}')
#   return item_bar
#