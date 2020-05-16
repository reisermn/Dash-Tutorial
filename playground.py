import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

test_dict = [dict(
    x=df[df['continent'] == i]['gdp per capita'],
    y=df[df['continent'] == i]['life expectancy'],
    text=df[df['continent'] == i]['country'],
    mode='markers',
    opacity=0.7,
    marker={
        'size': 15,
        'line': {'width': 0.5, 'color': 'white'}
    },
    name=i
) for i in df.continent.unique()]