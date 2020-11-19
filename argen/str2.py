import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

pg = [0.78, 0.48, 0.66, 0.41, 0.56, 0.30, 0.67, 0.90, 0.57, 0.97, 1.11, 0.72, 0.22, 0.44, 0.48, 0.28, 0.13, 0.20, 0.26, 0.60, 0.53, 1.30, 1.10, 0.97, 0.60, 1.03, 0.31, 0.85, 0.47, 0.67, 1.07]
pa = [0.49, 0.21, 0.04, 0.00, 0.10, 0.26, 0.27, 0.19, 0.24, 0.14, 0.29, 0.08, 0.22, 0.06, 0.00, 0.06, 0.46, 0.13, 0.32, 0.15, 0.14, 0.26, 0.12, 0.28, 0.05, 0.19, 0.25, 0.14, 0.00, 0.19, 0.30]

app.layout = html.Div(children=[
  html.Div(children=[
    dcc.Graph(
      id='strk_graph2',
      figure={
        'data':[
          go.Scatter(
            x=[pg[25]],
            y=[pa[25]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Aguero',
            text='Aguero',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[6]],
            y=[pa[6]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Jesus',
            text='Jesus',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[1]],
            y=[pa[1]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Lacazette',
            text='Lacazette',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[2]],
            y=[pa[2]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Aubameyang',
            text='Aubameyang',
            textposition='bottom center'
          ),
          go.Scatter(
            x=[pg[3]],
            y=[pa[3]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Giroud',
            text='Giroud',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[4]],
            y=[pa[4]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Kane',
            text='Kane',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[5]],
            y=[pa[5]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Firmino',
            text='Firmino',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[20]],
            y=[pa[20]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Martial',
            text='Martial',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[29]],
            y=[pa[29]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'blueviolet'
            },
            name='Rashford',
            text='Rashford',
            textposition='top center'
          ),
            go.Scatter(
            x=[pg[0]],
            y=[pa[0]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='Suarez',
            text='Suarez',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[8]],
            y=[pa[8]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='Benzema',
            text='Benzema',
            textposition='top center'
          ),
          # go.Scatter(
          #   x=[pg[12]],
          #   y=[pa[12]],
          #   mode='markers+text',
          #   opacity=0.7,
          #   marker={
          #     'size':20,
          #     'color':'gold'
          #   },
          #   name='D.Costa',
          #   text='D.Costa',
          #   textposition='top center'
          # ),
          go.Scatter(
            x=[pg[13]],
            y=[pa[13]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='Morata',
            text='Morata',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[14]],
            y=[pa[14]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='KPB',
            text='KPB',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[15]],
            y=[pa[15]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='L.DeJong',
            text='L.DeJong',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[16]],
            y=[pa[16]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='Rodrigo Moreno',
            text='Rodrigo Moreno',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[17]],
            y=[pa[17]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='Borja Iglesias',
            text='Borja Iglesias',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[18]],
            y=[pa[18]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'gold'
            },
            name='Braithwaite(18/19)',
            text='Braithwaite(18/19)',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[7]],
            y=[pa[7]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'limegreen'
            },
            name='Zlatan(Milan11/12)',
            text='Zlatan(11/12)',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[9]],
            y=[pa[9]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'limegreen'
            },
            name='C.Ronaldo',
            text='C.Ronaldo',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[26]],
            y=[pa[26]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'limegreen'
            },
            name='Higuain',
            text='Higuain',
            textposition='bottom center'
          ),
          go.Scatter(
            x=[pg[10]],
            y=[pa[10]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'limegreen'
            },
            name='Immobile',
            text='Immobile',
            textposition='bottom center'
          ),
          go.Scatter(
            x=[pg[11]],
            y=[pa[11]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'limegreen'
            },
            name='Lukaku',
            text='Lukaku',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[24]],
            y=[pa[24]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'limegreen'
            },
            name='Lautaro',
            text='Lautaro',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[19]],
            y=[pa[19]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'royalblue'
            },
            name='Cavani',
            text='Cavani',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[27]],
            y=[pa[27]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'royalblue'
            },
            name='Icardi',
            text='Icardi',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[30]],
            y=[pa[30]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'royalblue'
            },
            name='Mbappe',
            text='Mbappe',
            textposition='top center'
          ),
          # go.Scatter(
          #   x=[pg[28]],
          #   y=[pa[28]],
          #   mode='markers+text',
          #   opacity=0.7,
          #   marker={
          #     'size':20,
          #     'color':'royalblue'
          #   },
          #   name='Benedetto',
          #   text='Benedetto',
          #   textposition='bottom center'
          # ),
          go.Scatter(
            x=[pg[21]],
            y=[pa[21]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'orangered'
            },
            name='Haland',
            text='Haland',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[22]],
            y=[pa[22]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'orangered'
            },
            name='Lewandowski',
            text='Lewandowski',
            textposition='top center'
          ),
          go.Scatter(
            x=[pg[23]],
            y=[pa[23]],
            mode='markers+text',
            opacity=0.7,
            marker={
              'size':20,
              'color':'orangered'
            },
            name='Werner',
            text='Werner',
            textposition='top center'
          ),
        ],
        'layout':go.Layout(
          title='5大リーグのストライカー比べてみました',
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
   'width':'1100px',
   'height':'1200px',
   'textAlign':'center',
   'margin': '0 auto'
})

if __name__ == '__main__':
    app.run_server(debug=True)

