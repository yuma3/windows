import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()
df = pd.read_csv('data/mpg.csv')
df2 = pd.read_csv('data/wheels.csv')
features = df.columns

app.layout = html.Div([
  html.Div([
    dcc.Dropdown(
      id='xaxis',
      options=[{'label':i,'value':i} for i in features],
      value='displacement',
      style={'color': 'yellowgreen'}
      )
  ], style={'width': '48%', 'display': 'inline-block'}),

  html.Div([
    dcc.Dropdown(
      id='yaxis',
      options=[{'label':i,'value':i} for i in features],
      value='mpg',
      style={'color': 'yellowgreen'}
      )
  ], style={'width': '48%', 'display': 'inline-block'}),

  dcc.Graph(
    id='graph'
  ),


  dcc.RadioItems(
    id='wheels',
    options=[{'label':i,'value':i}for i in df2['wheels'].unique()],
    value=1
  ),

  html.Div(id='wheels-output'),
  html.Hr(),

  dcc.RadioItems(
    id='colors',
    options=[{'label':i, 'value':i}for i in df2['color'].unique()],
    value='blue'
  ),
  html.Div(id='colors-output'),
  html.Img(id='display', src='children', height=300)

],style={'padding':10, 'fontFamily':'helvetica', 'fontSize':18})

@app.callback(
  Output(component_id='graph',component_property='figure'),
  [Input(component_id='xaxis',component_property='value'),
   Input(component_id='yaxis',component_property='value')]
)
def update(x,y):
  return {
    'data':[go.Scatter(
                x=df[x],
                y=df[y],
                text=df['name'],
                mode='markers',
                marker={
                  'size':12,
                  'opacity':0.7,
                  'line':{'width':0.5,'color':'white'}
                }
          )],
     'layout':go.Layout(title='My Dashboard for MPG',
                xaxis={'title':x},
                yaxis={'title':y},
                hovermode='closest')
  }


@app.callback(
  Output(component_id='wheels-output', component_property='children'),
  [
    Input(component_id='wheels', component_property='value')
  ]
)
def wheelback(wheels_value):
  return 'You\'ve selected "{}"'.format(wheels_value)

@app.callback(
  Output(component_id='colors-output', component_property='children'),
  [
    Input(component_id='colors', component_property='value')
  ]
)
def colorback(colors_value):
  return 'You\'ve selected "{}"'.format(colors_value)

@app.callback(
  Output(component_id='display', component_property='src'),
  [
    Input(component_id='wheels', component_property='value'),
    Input(component_id='colors', component_property='value')
  ]
)
def imgback(wheel, color):
  path = 'data/images/'
  return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
  app.run_server(debug=True)

