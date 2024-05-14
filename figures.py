import plotly.express as px
import pandas as pd
from data import daily_sales_dateqty



line_graph = px.line(daily_sales_dateqty, x = 'date', y='sum_sales')