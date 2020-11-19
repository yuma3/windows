import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('../assets/balon/balon.csv')
print(df['Season'])

season_options = []
for season in df['Season'].unique():
  season_options.append({'label':season,'value':season})

app = dash.Dash()
app.layout = html.Div(children=[
  html.H1(children='GOAT'),
  html.Div(children=[
    dcc.Graph(
      id='graph'
    ),
    dcc.Dropdown(
      id='picker',
      options=season_options,
      value=df['Season'][0]
    )
  ])
])

@app.callback(Output(component_id='graph',component_property='figure'),
             [Input(component_id='picker',component_property='value')])
def update_figure(selected_season):

  filtered_df = df[df['Season']==selected_season]

  data = []
  for name in df['Name'].unique():
    df_by_name = filtered_df[filtered_df['Name']==name]
    print(df_by_name)
    data.append(go.Scatter(
      x=df_by_name['Ast'],
      y=df_by_name['Gls'],
      mode='markers',
      opacity=0.7,
      marker={'size':15},
      name=name
    ))

  return {'data':data,
          'layout':go.Layout(title='王と召使い',
                             xaxis={'title':'Assist'},
                             yaxis={'title':'Goals'})
          }

if __name__ == '__main__':
  app.run_server(debug=True)
