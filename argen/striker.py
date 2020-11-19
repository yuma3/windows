import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

mp = [1663, 1397, 1467, 1267, 2101, 920, 1591]
pg = [0.60, 1.03, 0.31, 0.85, 0.47, 0.59, 0.51]
pa = [0.05, 0.19, 0.25, 0.14, 0.00, 0.10, 0.11]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
  # html.H2(children='アルヘンの9番比べてみました'),
  html.Div(children=[
    dcc.Graph(
      id='strk_graph',
      figure={
        'data':[
          go.Scatter(
            x=[pg[0]],
            y=[pa[0]],
            mode='markers',
            opacity=0.7,
            marker={
              'size':20
            },
            name='Lautaro'
          ),
          go.Scatter(
            x=[pg[1]],
            y=[pa[1]],
            mode='markers',
            opacity=0.7,
            marker={
              'size':20
            },
            name='Aguero'
          ),
          go.Scatter(
            x=[pg[2]],
            y=[pa[2]],
            mode='markers',
            opacity=0.7,
            marker={
              'size':20
            },
            name='Higuain'
          ),
          go.Scatter(
            x=[pg[3]],
            y=[pa[3]],
            mode='markers',
            opacity=0.7,
            marker={
              'size':20
            },
            name='Icardi'
          ),
          go.Scatter(
            x=[pg[4]],
            y=[pa[4]],
            mode='markers',
            opacity=0.7,
            marker={
              'size':20
            },
            name='Benedetto'
          ),
          go.Scatter(
            x=[pg[5]],
            y=[pa[5]],
            mode='markers',
            opacity=0.7,
            marker={
              'size':20
            },
            name='Alario'
          ),
          go.Scatter(
            x=[pg[6]],
            y=[pa[6]],
            mode='markers',
            opacity=0.7,
            marker={
              'size':20
            },
            name='Chimy'
          ),
        ],
        'layout':go.Layout(
          title='（アルヘンの9番を抜粋）',
          xaxis={
            'title':'90分あたりのゴール数',
            'linewidth':1,
            'mirror':False,
          },
          yaxis={
            'title':'90分あたりのアシスト数',
            'linewidth':1,
            'mirror':False,
          }
        )
      }
    )
  ])
],style={
   'width':'800px',
   'textAlign':'center',
   'margin': '0 auto'
})
if __name__ == '__main__':
    app.run_server(debug=True)

