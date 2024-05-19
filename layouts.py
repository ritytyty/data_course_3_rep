from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import daily_sales_date, daily_sales, prices_avg

from figures import line_graph


general_layout = html.Div(
    [
        html.H1(
            children="Daily sales",
            style={"textAlign": "center"},
        ),
        dcc.Graph(figure=line_graph),
        
        dbc.DropdownMenu(
        id='dropdown-selection',
        label='Выберите дату',
        children=[
            dbc.DropdownMenuItem(date, id= 'dropdown-selection-item')
            for  date in daily_sales.date.unique()
        ],
    ),    
        dcc.Graph(id='graph-content'),
        #dcc.Dropdown(
        #    daily_sales.date.unique(), "2024-04-30", id="dropdown-selection"
        #),
        #dcc.Graph(id='graph-content'),

   
        dcc.Dropdown(
        id='dropdown-selection_2',
        options=[
            {'label': 'Динамика ТН по дням', 'value': '1'},
            {'label': 'Динамика изменения цены', 'value': '2'}
        ],
        placeholder='Выберете тип графика' # Установить значение в пустом поле
        ),
  
        dcc.Graph(id='r-content'),
       

    ],
    style={"margin-left": "80px", "margin-right": "80px"},
)



