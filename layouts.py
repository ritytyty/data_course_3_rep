from dash import html, dcc

from data import daily_sales_dateqty
from figures import line_graph


general_layout = html.Div(
    [
        html.H1(
            children="Daily sales",
            style={"textAlign": "center"},
        ),
        dcc.Graph(figure=line_graph),
    ],
    style={"margin-left": "80px", "margin-right": "80px"},
)