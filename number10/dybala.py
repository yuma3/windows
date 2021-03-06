import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../assets/dybala.csv')

n_season = df['season'].values
n_g = df['goal'].values
n_g9 = df['g9'].values

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(children=[
  html.H2(children='Paulo Dybala',style={'marginBottom':0}),
  html.Div(children=[
    dcc.Graph(
      id='ney1',
      figure={
        'data':[
          go.Scatter(
            x=n_season,
            y=n_g,
            opacity=0.7,
            mode='lines+markers',
            name='ゴール数',
            yaxis='y1'
          ),
          go.Bar(
            x=n_season,
            y=n_g9,
            opacity=0.7,
            name='ゴール/per90min',
            yaxis='y2'
          ),
        ],
        'layout':go.Layout(
          title='Juventus',
          xaxis={
            'title':'',
            # 'linewidth':1,
            # 'mirror':False,
          },
          yaxis={
            'title':'ゴール数',
            'side':'left',
            'range':[0,max(n_g)+10],
            'overlaying':'y2'
          },
          yaxis2={
            'title':'90分あたりのゴール数',
            'side':'right',
            'range':[0,max(n_g9)+1],
          }
        )
      }
    ),
  ])
],style={
   'width':'1100px',
   'height':'1200px',
   'textAlign':'center',
   'margin': '0 auto'
})

if __name__ == '__main__':
    app.run_server(debug=True)
