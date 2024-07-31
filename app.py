import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
from scripts import data_processing as dp
from scripts import data_visualizations as dv

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

bill_df = pd.read_csv('data/Billionaires Statistics Dataset.csv')
world_df = pd.read_csv('data/world-data-2023.csv')


# data cleaning
world_df = dp.world_data_cleaning(world_df)

# perform data processing
df1 = dp.industry_worths(bill_df)
df2, df2_pivoted, df2_top25 = dp.demo_comparison(bill_df)
df2_top25.reset_index(inplace=True)
matrix3 = dp.economic_correlations(world_df)
df4 = dp.continent_gdp_life(world_df)

# create visualizations
fig1 = dv.industry_graph(df1)
fig2 = dv.demo_grouped_bar(df2)
fig3 = dv.economic_corr_map(matrix3)
fig4 = dv.cont_gdp_life_scatter(df4)

app.layout = html.Div([
    html.H1(children='Global Economy Dashboard'),
    html.H2(children='Total Net Worth Per Industry'),
    dcc.Graph(
        id='industry-graph', 
        figure=fig1, 
        className='graph-container'
    ),

    html.H2(children='Top 25 Net Worths in Millions by Gender'),
    html.Div(children=[
        dash_table.DataTable(
            data=df2_top25.to_dict('records'),
            columns=[{'name': i, 'id': i, 'selectable': True} for i in df2_top25.columns],
            id='demo-table',
            fixed_rows={'headers': True},
            style_table={'background-color': '#343a40', 'color': '#ffffff', 'height': '400px', 'overflowY': 'autoworld', 'width': '550px', 'border': '1px solid #ced4da'}, 
            style_header={'background-color': '#343a40', 'color': '#ffffff', 'font-weight': 'bold', 'border': '1px solid #ced4da'},
            style_cell={'background-color': '#343a40', 'color': '#ffffff', 'textAlign': 'center', 'minWidth': '100px', 'maxWidth': '150px', 'whiteSpace': 'normal'},
            style_cell_conditional=[{ 'if': {'column_id': 'country'}, 'text-align': 'left '}],
            style_data_conditional=[{ 'if': {'column_id': 'total'}, 'background-color': '#509990', 'padding': '10px' }],
        ),
        dcc.Graph(id='demo-graph', figure=fig2, className='graph-container', style={'width': '900px', 'margin-left': '15px'} )
    ], style={'display': 'flex', 'margin-bottom': '30px'}),  

    html.H2(children='Correlation Between Economic Indicators and Socio-Economic Factors'),
    dcc.Graph(
        id='corr-map',
        figure=fig3,
        className='graph-container',
        style={'height': '600px'}
    ),

    html.H2(children='GDP vs Life Expectancy per Country'),
    dcc.Graph(
        id='bubble-scatter-plot',
        figure=fig4,
        className='graph-contaner'
    )
], className='div-container')

if __name__ == '__main__':
    app.run(debug=True)