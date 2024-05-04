from dash import Dash, html, dash_table, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("../datasets/ipldata_19/matches.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children="My IPL Dashboard"),
    html.Hr(),
    dcc.RadioItems(options=['winner', 'venue', 'toss_decision', 'season'], value='winner', id='controls-and-radio'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='control-graph')
])

@callback(
    Output(component_id='control-graph', component_property='figure'),
    Input(component_id='controls-and-radio', component_property='value')
)
def update_graph(col):
    fig = px.bar(df[col])
    return fig

app.run(debug=True)
