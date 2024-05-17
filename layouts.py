from dash import html, dcc

from data import daily_sales_date, daily_sales, prices_avg
from figures import line_graph


general_layout = html.Div(
    [
        html.H1(
            children="Daily sales",
            style={"textAlign": "center"},
        ),
        dcc.Graph(figure=line_graph),
        dcc.Dropdown(
            daily_sales.date.unique(), "2024-04-30", id="dropdown-selection"
        ),
        dcc.Graph(id='graph-content'),

    
        dcc.Dropdown(['1','2'],'2'),
  
        dcc.Graph(id='r-content'),
       

    ],
    style={"margin-left": "80px", "margin-right": "80px"},
)
