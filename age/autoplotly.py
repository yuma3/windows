import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.offline as pyo
from plotly import tools
import math

df = pd.read_csv('../assets/league/liga.csv')


avarage_age = {
  'barca': 26.35,
  'madrid': 25.92,
  'atletico': 25.77
}



########### AGE #################################################
teams = ['barca', 'real', 'atletico', 'Bayern', 'Inter', 'United', 'City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Dortmund', 'Juve', 'Psg']

team_dict = {}
fig = tools.make_subplots(rows=5, cols=3, subplot_titles=('Barca', 'RealMadrid', 'Atletico', 'Bayern', 'Inter', 'United', 'City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Dortmund', 'Juve', 'Psg'))



row = 1
col = 1

for team in teams:

    mp_total = 0
    df_by_t = df[df['team'] == team]
    df_by_mp = df_by_t['mplay']
    for mp in df_by_mp:
          mp_total += mp


    df_by_30 = df[(df['age'] >= 30) & (df['team'] == team)]

    df_by_25 = df[(df['age'] >= 24) & (df['age'] < 30) & (df['team'] == team)]

    df_by_20 = df[(df['age'] >= 15) & (df['age'] < 24) & (df['team'] == team)]

    df_by_mp30 = df_by_30['mplay']
    print(df_by_mp30)
    print('#############################')

    df_by_mp25 = df_by_25['mplay']
    print(df_by_mp25)
    print('#############################')

    df_by_mp20 = df_by_20['mplay']
    print(df_by_mp20)
    print('#############################')



    total30 = 0
    total25 = 0
    total20 = 0

    for minute in df_by_mp30:
          total30 += minute
          per30 = math.floor(100 * (total30 / mp_total))
          print(per30)


    for minute in df_by_mp25:
          total25 += minute
          per25 = math.floor(100 * (total25 / mp_total))

    for minute in df_by_mp20:
          total20 += minute
          per20 = math.floor(100 * (total20 / mp_total))

    x_age = ['17~23', '24~29', '30~']
    y_data = [per20, per25, per30]

    team_dict[team] = y_data

    team = go.Bar(
          x=x_age,
          y=y_data,
          name=team.title(),
          text=y_data,
          textposition='auto'
    )

    fig.append_trace(team, row, col)
    col += 1

    if col == 4:
          col = 1
          row += 1
          if row == 6:
                break

#     def counter(num):
#           for i in range(1, num):
#                 yield i
#     c = counter(4)
#     col = next(c)







#     layout = go.Layout(
#           title='年齢バランス',
#     )


#     for i in range(1,4):
      #   fig.append_trace(team, 1, i)
#         if i == 3:
#             i = 0
#             for i in range(1, 4):
#                 fig.append_trace(team, 2, i)
#                 if i == 3:
#                     i = 0
#                     for i in range(1,4):
#                         fig.append_trace(team, 3, i)
#                         if i == 3:
#                               i = 0
#                               for i in range(1,4):
#                                   fig.append_trace(team, 4, i)
#                                   if i == 3:
#                                       i = 0
#                                       for i in range(1,4):
#                                          fig.append_trace(team, 5, i)


fig['layout'].update(
                      height=1000,
                      width=1000,
                      title='バルサだけが老人ホームなのか調べてみた',
                      xaxis={'title': '年齢層'},
                      yaxis={
                            'title': '総出場時間に対する割合',
                            'range': [0,100]
                             },
                  #     xaxis_type="linear", yaxis_type="log",
                      margin={
                            'l': 60, 'r': 30, 't': 100, 'b': 50,
                        #     'autoexpand': False
                             },
                      font={"family": "Cursive", "size": 12},
                      paper_bgcolor = "#fff"
                  #     template="plotly_dark"
)


pyo.plot(fig)



# def generate(num):
#       for i in range(num):
#           yield(i)

# g = generate(3)

# print(next(g))
# print(next(g))
# print(next(g))

# g = generate(3)

# print(next(g))
# print(next(g))
# print(next(g))







# print(team_dict)
# for i in range(1,5):
#     print(i)
