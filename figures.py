import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
from data import daily_sales_date

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
title="Динамика продаж в рублях "
)



