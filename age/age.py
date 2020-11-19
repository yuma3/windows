import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.offline as pyo
from plotly import tools

df = pd.read_csv('../assets/league/liga.csv')
# print(df)

avarage_age = {
  'barca': 26.35,
  'madrid': 25.92,
  'atletico': 25.77
}

start_age = {
  'barca': 26.35,
  'madrid': 25.92,
  'atletico': 25.77
}

# print(df[df['team']=='barca'])

########### AGE #################################################


df_by_barca30 = df[(df['age'] >= 30) & (df['team'] == 'barca')]

# df_by_age25 = df[df.query('30 > age >= 24')]
df_by_barca25 = df[(df['age'] >= 24) & (df['age'] < 30) & (df['team'] == 'barca')]

df_by_barca20 = df[(df['age'] >= 17) & (df['age'] < 24) & (df['team']=='barca')]


# print(df_by_barca30)
# print('#########################################################')
# print('#########################################################')
# print(df_by_barca25)
# print('#########################################################')
# print('#########################################################')
# print(df_by_barca30)


play_minute30 = df_by_barca30['mplay']
play_minute25 = df_by_barca25['mplay']
play_minute20 = df_by_barca20['mplay']


barca_play_time30 = []
for i in play_minute30:
  barca_play_time30.append(i)

barca_play_time25 = []
for i in play_minute25:
  barca_play_time25.append(i)

barca_play_time20 = []
for i in play_minute20:
  barca_play_time20.append(i)

# print(barca_play_time30)
# print(barca_play_time25)
# print(barca_play_time20)


squad_age = {}

result30 = 0
for i in barca_play_time30:
  result30 += i
  squad_age['over30'] = result30

print('result30:', result30)


result25 = 0
for i in barca_play_time25:
  result25 += i
  squad_age['over25'] = result25


print('result25:', result25)


result20 = 0
for i in barca_play_time20:
  result20 += i
  squad_age['over20'] = result20


print('result20:', result20)

print(squad_age)

result = result30 + result25 + result20
print(result)


result30 = (result30 / result)*100
result25 = (result25 / result)*100
result20 = (result20 / result)*100
print(result20)
print(result25)
print(result30)

x_age = ['17~23', '24~29','30~']
y_data = [result20, result25,result30]

trace0 = go.Bar(
    x = x_age,
    y = y_data,
    name='age_balance',
)

trace0 = go.Bar(
    x = x_age,
    y = y_data,
    name='age_balance',
)

trace0 = go.Bar(
    x = x_age,
    y = y_data,
    name='age_balance',
)
trace0 = go.Bar(
    x = x_age,
    y = y_data,
    name='age_balance',
)
trace0 = go.Bar(
    x = x_age,
    y = y_data,
    name='age_balance',
)
trace0 = go.Bar(
    x = x_age,
    y = y_data,
    name='age_balance',
)



layout = go.Layout(
  title='Bucciaratiはデカダンス',
  # marker={'color':'tomato'}
)
fig = tools.make_subplots(rows=5, cols=3, subplot_titles=('Barca', 'RealMadrid', 'Atletico', 'Bayern', 'Inter', 'United', 'City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Dortmund', 'Juve', 'Psg'))


fig.append_trace(trace0, 1, 1)
fig.append_trace(trace0, 2, 1)
fig.append_trace(trace0, 3, 1)
fig.append_trace(trace0, 4, 1)
fig.append_trace(trace0, 5, 1)


fig['layout'].update(
                      height=1000,
                      width=1000,
                      title='バルサだけが老人ホームなのか調べてみた',
                      xaxis={'title': 'x軸'},
                      yaxis={'title': 'y軸'},
                      margin={'l':60, 'r':30, 't':100,'b':50, 'autoexpand':False}

)

pyo.plot(fig)
# df2 = df[['name', 'team']]
# print(df2)
