import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
from scripts import data_processing as dp
from scripts import data_visualizations as dv

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

bill_df = pd.read_csv('data/Billionaires Statistics Dataset.csv')
world_df = pd.read_csv('word-data-2023.csv')

# perform data processing
df1 = dp.categoryWorths(bill_df)
df2, df2_pivoted, df2_top25 = dp.demoComparison(bill_df)
df2_top25.reset_index(inplace=True)

# create visualizations
fig1 = dv.catWorthGraph(df1)
fig2 = dv.demoGroupedBar(df2)

app.layout = html.Div([
    html.H1(children='Global Billionaire Dashboard'),

    html.Div(children=[
        html.H2(children='Total Net Worth Per Category'),
        dcc.Graph(id='cat-graph', figure=fig1, className='graph-container')
    ], className='div-container'),
    
    html.Div(children=[
        html.H2(children='Demographics'),
        dash_table.DataTable(
            data=df2_top25.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df2_top25.columns],
            id='demo-table',
            # className='data-table',
            style_table={'height': '300px', 'overflowY': 'auto'},  # Adjust height
            style_cell={'textAlign': 'center', 'minWidth': '100px', 'maxWidth': '150px', 'whiteSpace': 'normal'},
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#f9f9f9',
                    'className': 'dash-row-odd'
                },
                {
                    'if': {'column_id': 'total'},
                    'backgroundColor': '#f8d7da',
                    'color': '#721c24',
                    'className': 'dash-cell-total'
                }
            ],
            style_header={'className': 'dash-header'},
            style_cell_conditional=[
                {'if': {'column_id': 'country'}, 'className': 'dash-cell-left'}
            ]
        ),
        dcc.Graph(id='demo-graph', figure=fig2, className='graph-container')
    ], className='div-container'),
], className='div-container')

if __name__ == '__main__':
    app.run(debug=True)