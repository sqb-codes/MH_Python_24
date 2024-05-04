from dash import Dash, html, dcc, Input, Output, callback, dash_table
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

graph = dcc.Graph(id="graph")

app.layout = html.Div([
    html.H1("Restaurant tips"),
    html.H3("X-axis"),
    dcc.RadioItems(
        id="x-axis",
        options=["time", "sex", "day", "smoker"],
        value="time",
        inline=True
    ),
    html.H3("Y-axis"),
    dcc.RadioItems(
        id="y-axis",
        options=["total_bill", "tip", "size"],
        value="total_bill",
        inline=True
    ),
    # dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    graph
])

@callback(
    Output("graph", "figure"),
    Input("x-axis", "value"),
    Input("y-axis", "value")
)
def update_graph(x, y):
    fig = px.box(df, x=x, y=y)
    return fig

app.run_server(debug=True)
