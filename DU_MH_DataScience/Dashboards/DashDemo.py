from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("../datasets/ipldata_19/matches.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children="My IPL Dashboard"),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.bar(df['winner']))
])

app.run(debug=True)
