# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 04:14:42 2017

@author: priya
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
columnNames=['End User Companies','End User Inquiries','Non End User Companies','Non End User Inquiries','Total Inquiries','Avg Sources','Avg Qty','Avg Qty NE','Avg Qty NS','Avg Qty OH','Avg Qty SV','Avg Qty AR','Min','Max','Median','Avg Quote',' Count','Last Quoted','Min','Max','Median','Avg Quote',' Count','Last Quoted','Min','Max','Median','Avg Quote','Count','Last Quoted','Min','Max','Median','Avg Quote','Count','Last Quoted','Min','Max','Median','Avg Quote','Count','Last Quoted','Min','Max','Median','Avg Quote','Count','Last updated','Min','Max','Median','Avg Quote','Count','Last Updated'];

df = pd.read_csv('C:\\Users\priya\Documents\Hackathon\dash.csv',sep=',',names=columnNames);

df1=df.iloc[:,0:5]

df2=df1.head(5)

from dash.dependencies import Input, Output
     

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Demand', 'value': 'Demand'},
            {'label': 'Supply', 'value': 'Supply'},
            {'label': 'NE', 'value': 'NE'}
        ],
        value='Demand'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value, data_source=df2,
        start=dt(1, 1), end=dt.now())
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }]
    }