import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.offline as pyo
from plotly import subplots
import math
import chart_studio



df = pd.read_csv('../assets/liga/mf_pass.csv')

clubs = df['Club'].unique()

df_by_season = df[df['Season'] == '2019-2020']

fig = subplots.make_subplots(rows=7, cols=3, subplot_titles=(clubs))


# print(df_by_season[['Name','Cmpper']])
# print(df_by_cmpper)
# print(df_by_season['Name'].unique())
app = dash.Dash()
# s = len(df_by_season['Name'].unique())



row = 1
col = 1

for club in clubs:
    df_by_club = df_by_season[df_by_season['Club'] == club]
    # print(df_by_club)

    CMPPER = df_by_club['Cmpper']

    NAMES = []
    for name in df_by_club['Name'].unique():
        if ' ' in name:
            name = name.split()
            name = name[-1]
        NAMES.append(name)

    graph = go.Bar(
        x=CMPPER,
        y=NAMES,
        name=club.title(),
        text=CMPPER,
        textposition='auto',
        orientation='h'
    )

    fig.append_trace(graph, row, col)
    col += 1
    if col == 4:
          col = 1
          row += 1
          if row == 8:
                break


fig['layout'].update(
                      height=1500,
                      width=1000,
                    #   title='Pass'
                  #     xaxis_type="linear", yaxis_type="log",
                      margin={
                            # 'l': 50, 'r': 50, 't': 50, 'b': 50,
                            'autoexpand': True
                             },
                    #   padding={'l': 20, 'r':30},
                      font={"family": "Cursive,Monospace", "size": 12},
                      paper_bgcolor="#fff",
                    #   plot_bgcolor="#fff"
                    #   template="plotly_dark"
)
app.layout = html.Div([

    html.Div([
        dcc.Graph(
            id='pass',
            figure=fig,



        )
    ])
],style=dict(display='flex', justifyContent='center')
)
if __name__ == '__main__':
    app.run_server(debug=True)
