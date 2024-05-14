from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from app import app
from data import daily_sales_dateqty

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    df = daily_sales_dateqty[daily_sales_dateqty.date == value]

    return px.line(df, x = 'date', y='sum_sales')


if __name__ == '__main__':
    app.run(debug=True)