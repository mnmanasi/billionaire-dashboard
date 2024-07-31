import pandas as pd
import re
# from decimal import Decimal
import pycountry
import pycountry_convert as pc

# sum all net worths, grouped by category (industry)
def industry_worths(df):
    cat_sum_worth = df.groupby('category')['finalWorth'].sum().reset_index()
    return cat_sum_worth

# compare sums of each country's net worth between male and female
def demo_comparison(df):
    demo = df.groupby(['country', 'gender']).agg('sum')['finalWorth'].reset_index()
    demo_pivot = pd.pivot(demo, index='country', columns='gender', values='finalWorth')
    demo_pivot['total'] = demo_pivot['M'] + demo_pivot['F']
    top_demo_pivot = demo_pivot.nlargest(25, 'total')
    return demo, demo_pivot, top_demo_pivot

# clean non numeric values
def clean_numeric(value):
    if isinstance(value, str) and re.search(r'\d', value):
        value = re.sub(r'[^\d.]', '', value)
        value = float(value)
    return value

# apply clean_numeric to world dataset
def world_data_cleaning(df):
    for col in df.columns:
        if col not in ['Country', 'Abbreviation', 'Currency-Code', 'Capital/Major City', 'Largest city']:
            df[col] = df[col].apply(clean_numeric)
    # for col in df.columns:
    #     df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# make correlation matrix to compare economic indicators
def economic_correlations(df):
    selected_columns = [
        'GDP', 'Density(P/Km2)', 'Agricultural Land( %)', 'Land Area(Km2)', 
        'Armed Forces size', 'Birth Rate', 'Co2-Emissions', 'CPI', 'CPI Change (%)', 
        'Fertility Rate', 'Forested Area (%)', 'Gasoline Price', 
        'Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)', 
        'Infant mortality', 'Life expectancy', 'Maternal mortality ratio', 
        'Minimum wage', 'Out of pocket health expenditure', 
        'Physicians per thousand', 'Population', 'Population: Labor force participation (%)', 
        'Tax revenue (%)', 'Total tax rate', 'Unemployment rate', 'Urban_population'
    ]
    df_selected = df[selected_columns]
    df_selected = df_selected.dropna()
    correlation_matrix = df_selected.corr()
    return correlation_matrix

# map country to continent
def get_continent(country_name):
    try:
        country_alpha2 = pycountry.countries.lookup(country_name).alpha_2   # get alpha-2 code
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)   # get continent code
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)   # map continent code to continent name
        return continent_name
    except (LookupError, KeyError):
        return 'Unknown'
    
# get subset of df for scatter plot
def continent_gdp_life(df):
    df['Continent'] = df['Country'].apply(get_continent)
    df = df.dropna(subset=['GDP', 'Life expectancy'])
    return df