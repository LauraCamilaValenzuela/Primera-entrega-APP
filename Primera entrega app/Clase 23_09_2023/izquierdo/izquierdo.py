import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

izquierdo = dbc.Container ([   
    html.H1('DATOS DE LA ESTRUCTURA'),
    html.Hr(),
    html.Div([
        html.Label('Ingrese el número de pisos de la estrutura'),
        dcc.Input(id='entradaPisos', value = 5, type = 'number'),
        html.Label(id='salidaPisos')

    ])
  ])