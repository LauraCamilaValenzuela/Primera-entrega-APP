import dash
import dash_bootstrap_components as dbc
from dash import html

#derecho = dbc.Container ([   
 #   html.H1('Datos del proyecto'),
   # html.Hr(),
    #html.H2('Ensayos de pentracion'),
    #dbc.Row([ 
     #   dbc.Col ('visualizacion',md=3 , style={'background-color':'black'}),
      #  dbc.Col ('texto',md=6 , style={'background-color':'gray'}),
       # dbc.Col ('Usuario',md=3 , style={'background-color':'blue'})
    
   # ])
 # ])

derecho = dbc.Container(
    [
        html.H2('Datos del proyecto'),
        html.Hr(),
        html.Label('Nombre:'),
        dbc.Input(value="Nombre"),
        html.Label('Localización:'),
        dbc.Input(value="Localización"),
        html.Label('Fecha Inicio:'),
        dbc.Input(value="Fecha", type="date"),
        html.Label('Fecha Fin:'),
        dbc.Input(value="Fecha", type="date"),
    ])