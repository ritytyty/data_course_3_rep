import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from data_transform import daily_sales_date, tn_df, sumqty_df

line_graph = go.Figure(go.Scatter(
                            x = daily_sales_date['date'],
                            y = daily_sales_date['sum_sales'],
                            fill= 'tonexty' )
    )
line_graph.add_trace(go.Indicator(
   mode = "number+delta",
   value =  0.001 * daily_sales_date['sum_sales'].loc[daily_sales_date['date']=='2024-04-30'].values[0],
   number = {"prefix": "₽", "suffix": "k"},
   delta = {"reference":  0.001 * daily_sales_date['sum_sales'].loc[daily_sales_date['date']=='2024-04-29'].values[0], 
            "valueformat": ".0f", 
            "prefix": "₽", 
            "suffix": "k"},
   title = {"text": "Выручка"}
       ))

line_graph.update_xaxes(title_text="Дата")
line_graph.update_yaxes(title_text="Продажи, руб.")
line_graph.update_layout(
title="Динамика продаж в рублях"
)

tn_indicator = go.Figure()
tn_indicator.add_trace(go.Indicator(
   mode = "number+delta",
   value = tn_df.values[0],
   number={"prefix": "%","suffix": ""},
   delta={"reference": 50, "valueformat" : "0.f" ,"prefix": "%","suffix": "" },
   title = {"text":"Норма ТН по компании 50%"}
))  
tn_indicator.update_layout(
    title="ТН по компании на текущий день"
)

sumqty_indicator = go.Figure()
sumqty_indicator.add_trace(go.Indicator(
   mode = "number+gauge+delta",
   gauge = {'shape': "bullet", 'bar': {'color': 'rgba(99, 110, 250, 0.8)'} },
   value = sumqty_df['sum_qty_day'].tail(1).values[0],
   number={"prefix": "Ед.","suffix": ""},
   delta={"reference": sumqty_df['old_sumqty'].tail(1).values[0], "valueformat" : "0.f" ,"prefix": "Ед.","suffix": "" },
   title = {"text":"Σ:"}
))  
sumqty_indicator.update_layout(
    title="Остатки на складе на текущий день"
)

                          
                    

