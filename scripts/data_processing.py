import pandas as pd

def categoryWorths(df):
    cat_sum_worth = df.groupby('category')['finalWorth'].sum().reset_index()
    return cat_sum_worth

def demoComparison(df):
    demo = df.groupby(['country', 'gender']).agg('sum')['finalWorth'].reset_index()
    demo_pivot = pd.pivot(demo, index='country', columns='gender', values='finalWorth')
    demo_pivot['total'] = demo_pivot['M'] + demo_pivot['F']
    top_demo_pivot = demo_pivot.nlargest(25, 'total')
    return demo, demo_pivot, top_demo_pivot

 