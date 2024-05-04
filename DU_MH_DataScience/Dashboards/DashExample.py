from dash import Dash, html, dcc, Input, Output, callback, dash_table
import plotly.express as px

df = px.data.tips()

app = Dash(__name__)

graph = dcc.Graph()
dropdown = dcc.Dropdown(["Sun", "Mon", "Sat"], "Mon", clearable=False)

app.layout = html.Div([
    html.H1("Restaurant tips"),
    dropdown,
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    graph
])

@callback(
    Output(graph, "figure"),
    Input(dropdown, "value")
)
def update_graph(col):
    mask = df["day"] == col
    fig = px.bar(df[mask], x="sex", y="total_bill", barmode="group", color='time')
    return fig

app.run_server(debug=True)
