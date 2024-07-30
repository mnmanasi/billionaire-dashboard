import plotly.express as px
import plotly.graph_objects as go

def industryGraph(df):
    fig = px.line(df, x='category', y='finalWorth')
    fig.update_layout(plot_bgcolor='#343a40', paper_bgcolor='#343a40')
    fig.update_traces(line_color='#3dc2ec')
    fig.update_xaxes(color='#dddddd')
    fig.update_yaxes(color='#3dc2ec')
    return fig

def demoGroupedBar(df):
    combined_worth = df.groupby('country')['finalWorth'].sum().reset_index()
    top_countries = combined_worth.nlargest(25, 'finalWorth')['country']
    filtered_df = df[df['country'].isin(top_countries)]
    filtered_df = filtered_df.sort_values('finalWorth', ascending=False)
    f1 = filtered_df[filtered_df['gender'] == 'M']
    f2 = filtered_df[filtered_df['gender'] == 'F']
    fx = filtered_df['country'].tolist()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=fx, y=f1['finalWorth'], name='M', marker_color='#8CABFF'))
    fig.add_trace(go.Bar(x=fx, y=f2['finalWorth'], name='F', marker_color='#EAB2A0'))
    fig.update_layout(barmode='stack', plot_bgcolor='#343a40', paper_bgcolor='#343a40', font={'color': '#dddddd'}, xaxis_tickangle=-45)
    return fig
