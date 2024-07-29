import plotly.express as px
import plotly.graph_objects as go

def catWorthGraph(df):
    fig = px.line(df, x='category', y='finalWorth')
    return fig

def demoGroupedBar(df):
    f1 = df[df['gender'] == 'M']
    f2 = df[df['gender'] == 'F']
    fx = df['country'].tolist()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=fx, y=f1['finalWorth'], name='M'))
    fig.add_trace(go.Bar(x=fx, y=f2['finalWorth'], name='F'))
    fig.update_layout(barmode='stack')
    return fig
