import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/gapminderDataFiveYear.csv')
print(df)

year_options = []
for year in df['year'].unique():
  year_options.append({'label':str(year),'value':year})


app = dash.Dash()
app.layout = html.Div([
  html.H1(children='Life is easy'),
  html.Div([
    dcc.Dropdown(
      id='year-option',
      options=year_options,
      value=df['year'].min(),
      # style={'fontSize':18,'color':'#ccc'}
    ),
    dcc.Graph(id='graph')
  ])
])
@app.callback(Output(component_id='graph',component_property='figure'),
             [Input(component_id='year-option',component_property='value')])
def upback(selected_year):
  df_year = df[df['year']==selected_year]

  data = []
  for continent in df_year['continent'].unique():

    df_continent = df_year[df_year['continent']==continent]
    data.append(
                go.Scatter(
                  x=df_continent['gdpPercap'],
                  y=df_continent['lifeExp'],
                  mode='markers',
                  opacity=0.5,
                  marker={'size':32},
                  name=continent
                )
               )

  return {'data':data, 'layout':go.Layout(title='Myplot',
                                          xaxis={'title':'GDP Per Cap','type':'log'},
                                          yaxis={'title':'Life Expectancy'})
          }
app.config['suppress_callback_exceptions']=True

if __name__ == '__main__':
  app.run_server(debug=True)
