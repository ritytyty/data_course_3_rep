import plotly.express as px
import pandas as pd
from data import daily_sales_date


line_graph = px.area( daily_sales_date, 
                     x = 'date',
                     y='sum_sales', 
                     title = 
                     'Динамика продаж в руб.', 
                     labels={'sum_sales':'Сумма продаж, руб.', 'date':'Дата'}
                     )

        