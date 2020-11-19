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


def get_league_average():

    df = pd.read_csv('../assets/liga/goal.csv')

    leagues = df['League']
    average = {}
    for league in leagues:

        df_by_league = df[df['League'] == league]
        goals = df['Gls'].values
        sorted_goals = sorted(goals, reverse=True)
        sorted_goals = sorted_goals[:10]
        print(sorted_goals)

        score = 0
        for goal in sorted_goals:
            score += goal

        ave = score / len(goals)

        average[league] = ave
        print(average)

    return average

def get_hensa(name, season, league):

    df = pd.read_csv('../assets/liga/goal.csv')
    target = df[(df['Season'] == season) & (df['League'] == league)]
    names = target['Name'].values

    hensa_list = []
    for name in names:
        df_by_name = target[target['Name'] == name]
        goal = df_by_name['Gls'].values

        averate = get_league_average()

        hensa = average[league] - goal[0]
        hensa_list.append(hensa)

    return hensa_list


def get_normal_hensa():
    result = 0
    for hensa in get_hensa():
        result += hensa ** 2

    bunsan = result / len(hensa_list)
    result = math.sqrt(bunsan)

    return result

def last():
    results = []
    for hensa in hensa_list:
        result = hensa / get_normal_hensa()
        results.append(result)
    return results
