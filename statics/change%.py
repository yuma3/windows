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

import os
import pathlib



FILE_PATH = '../assets/liga/mf_pass.csv'
DEFAULT_ROW = 1
DEFAULT_COL = 1

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



def get_data(file_path=None, season='2019-2020', value='Final'):


    if file_path is None:
        file_path = FILE_PATH
    df = pd.read_csv(file_path)

    clubs = df['Club'].unique()
    fig = subplots.make_subplots(rows=7, cols=3, subplot_titles=(clubs))

    df_by_season = df[df['Season'] == season]

    df = pd.read_csv(FILE_PATH)


    for club in clubs:

        df_by_club = df_by_season[df_by_season['Club'] == club]

        NAMES = df_by_club['Name'].unique()


        RESULTS = []
        for name in NAMES:
            df_by_name = df_by_club[df_by_club['Name'] == name]

            VALUE = df_by_name[value].values

            MINUTE = df_by_name['90s'].values

            result = VALUE[0] / MINUTE[0]
            result = round(result, 2)

            RESULTS.append(result)


        RENAMES = []
        for name in df_by_club['Name'].unique():
            if ' ' in name:
                name = name.split()
                name = name[-1]
            RENAMES.append(name)


        graph = go.Bar(
            x=RESULTS,
            y=RENAMES,
            name=club.upper(),
            text=RESULTS,
            textposition='auto',
            orientation='h'
        )

        global DEFAULT_COL
        global DEFAULT_ROW

        fig.append_trace(graph, DEFAULT_ROW, DEFAULT_COL)
        DEFAULT_COL += 1
        if DEFAULT_COL == 4:
            DEFAULT_COL = 1
            DEFAULT_ROW += 1
            if DEFAULT_ROW == 8:
                break


    fig['layout'].update(
            height=1500,
            width=1000,
            margin={'autoexpand': True},
            font={"family": "Monospace", "size": 12}
        )

    return fig




app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H2(children='Penalty Area Pass'),
    dcc.Graph(
        id='bucciara_graph_',
        figure=get_data(value='PPA')
    )
], style={'display': 'flex', 'justifyContent': 'center'})





if __name__ == '__main__':
    # get_data()
    app.run_server(debug=True)
