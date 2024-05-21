from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data_transform import daily_sales_date, daily_sales, prices_avg

#from figures import line_graph
from figures import line_graph, tn_indicator, sumqty_indicator




general_layout = html.Div(
    [
        html.H1(
            children = "Daily sales",
            style={"textAlign": "center"},
        ),
        dcc.Graph(figure=line_graph),
        
       dbc.Select(
           id="dropdown-selection", 
           options=[{"label": date, "value": date} for date in daily_sales.date.unique()],
           placeholder="Выберите дату", 
),
        dcc.Graph(id='graph-content'),

   
        dbc.Row (
            [dbc.Col (
                [dcc.Graph(figure =tn_indicator)]
            ), dbc.Col(
                 [dcc.Graph(figure =sumqty_indicator)]
            )]

               ),

        #dcc.Dropdown(
        #    daily_sales.date.unique(), "2024-04-30", id="dropdown-selection"
        #),
        #dcc.Graph(id='graph-content'),
        
        dbc.Button('Вывести динамику ТН по дням', id = 'tn-dynamic' ,color='primary', n_clicks=0),
        dbc.Button('Вывести динамику изменения цены', id = 'price-dynamic', color='primary',n_clicks=0),
       
        dcc.Graph(id='output-graph')

        #dcc.Dropdown(
        #id='dropdown-selection_2',
        #options=[
        #    {'label': 'Динамика ТН по дням', 'value': '1'},
        #    {'label': 'Динамика изменения цены', 'value': '2'}
        #],
        #placeholder='Выберете тип графика' # Установить значение в пустом поле
        #),
  #
        #dcc.Graph(id='r-content'),
        
     
       
    ],
    style={"margin-left": "80px", "margin-right": "80px"},
)



