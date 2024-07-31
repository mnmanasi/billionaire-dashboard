import plotly.express as px
import plotly.graph_objects as go


def industry_graph(df):
    fig = px.line(df, x='category', y='finalWorth')
    fig.update_layout(plot_bgcolor='#161a1d', paper_bgcolor='#161a1d')  # 242a44
    fig.update_traces(line_color='#61b6ee')
    fig.update_xaxes(color='#dddddd', gridcolor='Grey')
    fig.update_yaxes(color='#61b6ee', gridcolor='Grey')
    return fig

def demo_grouped_bar(df):
    combined_worth = df.groupby('country')['finalWorth'].sum().reset_index()
    top_countries = combined_worth.nlargest(25, 'finalWorth')['country']
    filtered_df = df[df['country'].isin(top_countries)]
    filtered_df = filtered_df.sort_values('finalWorth', ascending=False)
    f1 = filtered_df[filtered_df['gender'] == 'M']
    f2 = filtered_df[filtered_df['gender'] == 'F']
    fx = filtered_df['country'].tolist()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=fx, y=f1['finalWorth'], name='M', marker_color='#1f77b4')) #52e0f0
    fig.add_trace(go.Bar(x=fx, y=f2['finalWorth'], name='F', marker_color='#f05752')) #f05752
    fig.update_traces(marker_line_width = 0)
    fig.update_layout(
        barmode='stack',
        plot_bgcolor='#161a1d',
        paper_bgcolor='#161a1d',
        font={'color': '#dddddd'},
        xaxis_tickangle=-45
    )
    fig.update_yaxes(gridcolor='Grey')
    return fig

def economic_corr_map(corr_matrix):
    fig = px.imshow(
        corr_matrix,
        labels=dict(color="Correlation"),
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1
    )
    fig.update_layout(
        xaxis_title='Indicators', yaxis_title='Indicators',
        plot_bgcolor='#161a1d', paper_bgcolor='#161a1d',
        font={'color': '#dddddd'}
    )
    fig.update_xaxes(color='#dddddd')
    fig.update_yaxes(color='#dddddd')
    return fig

def cont_gdp_life_scatter(df):
    fig = px.scatter(
        df,
        x='GDP',
        y='Life expectancy',
        color='Continent',
        hover_name='Country',
        size='Population',
        size_max=45,
        log_x=True 
    )
    fig.update_layout(
        legend=dict(
            orientation='h',
            entrywidth=80,
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        font={'color': '#dddddd'},
        plot_bgcolor='#161a1d', paper_bgcolor='#161a1d'
    )
    fig.update_xaxes(color='#dddddd', gridcolor='Grey')
    fig.update_yaxes(color='#dddddd', gridcolor='Grey')
    return fig