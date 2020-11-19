import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import math

import plotly.offline as pyo
from plotly import subplots
import chart_studio
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

DF = pd.read_csv('../assets/liga/goal.csv')
LEAGUES = DF['League'].unique()
NAMES = DF['Name'].unique()


def get_std():
    # return standard deviation of goal by league

    result = {}
    for league in LEAGUES:
        df_by_league = DF[DF['League'] == league]
        goals = df_by_league['Gls'].values
        std = np.std(goals)
        result[league] = std
    return result


def get_standardization():
    # return standardization of goal

    standardization_num_list = []
    standardization_num_list_dict = []

    for league in LEAGUES:

        df_by_league = DF[DF['League'] == league]
        goals = df_by_league['Gls'].values
        names = df_by_league['Name'].unique()
        ave = np.mean(goals)

        for name in names:

            df_by_name = df_by_league[df_by_league['Name'] == name]
            goal = df_by_name['Gls']

            std = get_std()
            result = (goal - ave) / std[league]
            r = pd.Series(result)
            s = r.values

            standardization_num_list.append(s)
            standardization_num_list_dict.append({name: s})

    return standardization_num_list


VALUES = get_standardization()
VALUES = [i for item in VALUES for i in item]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H2(children=''),
    dcc.Graph(
        id='bucciara_graph',
        figure={
            'data': [
                go.Bar(
                    x=NAMES,
                    y=VALUES,
                    text=VALUES,
                    textposition='auto',
                    marker_color='lightcyan',
                )
            ],
            'layout': go.Layout(
                title='This is Graph for Goal Relativization. by Bucciarati@LoveFF38',
                height=500,
                width=1000,
                margin={'autoexpand': True},
                font={"family": "Monospace", "size": 12},
                template='plotly_dark',
                yaxis=dict(
                    autorange=True,
                    range=[-2, 3],
                    scaleanchor='x1', scaleratio=1,  # 他の軸とのスケールを固定したいときに使う
                )
            )
        }
    )
],
)


if __name__ == '__main__':

    app.run_server(debug=True)
