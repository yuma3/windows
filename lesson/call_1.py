import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()
app.layout = html.Div(children=[
  html.H1(children='コールバックの練習'),
  html.Div(children=[
    dcc.Input(
      id='input',
      value=1,
      style={
        'fontSize':18,
        'color':'tomato'
      }
    ),
    html.H2(id='output',style={'color':'blue'}),


    dcc.Input(
      id="input2",value=0, style={'fontSize':24}
    ),
    html.Button(
      id='submit',
      n_clicks=0,
      children='submit here',
      style={'fontSize':22}
    ),
    html.H2(id='output2',style={'color':'yellowgreen'}),
  ])
])

@app.callback(
  Output(component_id='output', component_property='children'),
  [Input(component_id='input', component_property='value')]
)
def input(input_value):
  return 'you entered : {}'.format(input_value)


@app.callback(
  Output(
    component_id='output2', component_property='children'
  ),
  [Input(
    component_id='submit', component_property='n_clicks'
  )],
  [State(
    component_id='input2', component_property='value'
  )]
)
def button(n_clicks, num):
  return '{c} was typed in, and Button was clicked {n} times'.format(c=num, n=n_clicks)



if __name__ == '__main__':
  app.run_server(debug=True)
