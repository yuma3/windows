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
import chart_studio
import chart_studio.plotly as py

df = pd.read_csv('../assets/league/liga.csv')

teams = ['barca', 'real', 'atletico','man city', 'man united', 'liverpool', 'tottenham', 'arsenal', 'chelsea', 'bayern', 'dortmund', 'juventus', 'inter', 'milan', 'psg',]


fig = tools.make_subplots(rows=5, cols=3, subplot_titles=('Barca', 'RealMadrid', 'Atletico', 'City', 'United', 'Liverpool',  'Tottenham', 'Arsenal', 'Chelsea', 'Bayern','Dortmund', 'Juve', 'Inter', 'Milan', 'PSG'))



row = 1
col = 1

for team in teams:

    mp_total = 0
    df_by_t = df[df['team'] == team]
    df_by_mp = df_by_t['mplay']
    for mp in df_by_mp:
          mp_total += mp


    df_by_30 = df[(df['age'] >= 30) & (df['team'] == team) & (df['mplay'] > 90)]

    df_by_25 = df[(df['age'] >= 24) & (df['age'] < 30) & (df['team'] == team) & (df['mplay'] > 90)]

    df_by_20 = df[(df['age'] >= 15) & (df['age'] < 24) & (df['team'] == team) & (df['mplay'] > 90)]



    df_by_mp30 = df_by_30['mplay']
    # print(df_by_mp30)
    print('#############################')

    df_by_mp25 = df_by_25['mplay']
    # print(df_by_mp25)
    print('#############################')

    df_by_mp20 = df_by_20['mplay']
    # print(df_by_mp20)
    print('#############################')



    total30 = 0
    total25 = 0
    total20 = 0

    for minute in df_by_mp30:
          total30 += minute
          per30 = math.floor(100 * (total30 / mp_total))
        #   print(per30)


    for minute in df_by_mp25:
          total25 += minute
          per25 = math.floor(100 * (total25 / mp_total))

    for minute in df_by_mp20:
          total20 += minute
          per20 = math.floor(100 * (total20 / mp_total))

    x_age = ['17~23', '24~29', '30~']
    y_data = [per20, per25, per30]

    team_dict = {}
    team_dict[team] = y_data
    print(team_dict)

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


fig['layout'].update(
                      height=1000,
                      width=1000,
                      title='パレデスがいる時代に生まれることができて良かった。',
                    #   xaxis={'title': '年齢層'},
                    #   yaxis={
                    #         'title': '総出場時間に対する割合',
                    #         'range': [0,100]
                    #          },
                  #     xaxis_type="linear", yaxis_type="log",
                      margin={
                            'l': 50, 'r': 50, 't': 50, 'b': 50,
                        #     'autoexpand': False
                             },
                      font={"family": "Cursive,Monospace", "size": 12},
                      paper_bgcolor="#fff",
                    #   plot_bgcolor="#fff"
                  #   template="plotly_dark"
)




app = dash.Dash()

app.layout = html.Div([
    html.H2(
        children='「訂正版」',
        style={
            # 'textAlign': 'center',
            'font-family': 'monospace',
            'color':'red'
        }
        ),
    html.H3(
        children='CityとUnited、ロンドン勢のラベルがミスってました！！\n代入ミスです。。。ごめんなさい。。',
        style={
            # 'textAlign': 'center',
            'font-family': 'monospace'
        }
        ),
    html.Div([
        dcc.Graph(
            id='age_balance',
            figure=fig
        )
    ])
]
)

# chart_studio.tools.set_config_file(world_readable=False,
#                                    sharing='private')
# chart_studio.tools.set_credentials_file(username='yuma3', api_key='••••••••••')

# py.plot(fig)

if __name__ == '__main__':
      app.run_server(debug=True)
