import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime
import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('../assets/pivote/pivote.csv')
numsA = np.random.randint(1,500,5)
numsB = np.random.randint(1,200,5)

# arthur = [90.7, 1.1, 10, 101, 205, 57, 23] 総パス1060　1182min出場
# pjanic = [87.6, 3.1, 43, 192, 255, 190, 71] 総パス1867　2140min出場

arthur = [9.7, 0.94, 9.5, 19.3, 5.4, 2.2]
pjanic = [8.8, 2.3, 10.2, 13.7, 10.2, 3.8]





app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
  html.H2(children='ピポーテ検証'),
  html.Div(children=[
    dcc.Graph(
      id='pivote_graph',
      figure={
        'data':[
         go.Scatterpolar(
           r=pjanic,
           theta=['パス成功率','キーパス', 'Finalサードへのパス','被プレス時のパス', '前方へのパス', 'サイドチェンジ'],
           fill='toself',
           name='ミラレム・ピャニッチ',
           marker_color='rgb(158,154,200)'
         ),
         go.Scatterpolar(
           r=arthur,
           theta=['パス成功率', 'キーパス', 'Finalサードへのパス','被プレス時のパス', '前方へのパス', 'サイドチェンジ'],
           fill='toself',
           name='アルトゥール・メロ',
           marker_color='tomato'
         )
        ],
        'layout':go.Layout(
          polar={'radialaxis':{
            'visible':False,
            'range':[0,20]
          }},
          showlegend=False
        )
      }
    ),
  ])
])







if __name__ == '__main__':
  app.run_server(debug=True)
