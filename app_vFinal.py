import os
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Change to your local folder before editing
os.chdir("C:/Users/tobyt/Desktop/Coding/Personal/wins-above-replacement-soccer/WAR-based-soccer-valuation")

# Setup
search_df = pd.read_csv("./output/database/search-data.csv")

# Initialize the app
app = Dash(__name__)

# App layout
# TODO: add third dropdown logic
# TODO: add graph
app.layout = html.Div([
    html.H1(children="Implementing a WAR (Wins Above Replacement) Metric Into Major Soccer Leagues"),
    dcc.Dropdown(options=list(search_df["Name"].unique()), placeholder="Player:", id="name-dropdown", clearable=False),
    dcc.Dropdown(options=[], placeholder="Year:", id="year-dropdown", clearable=False),
    html.Div(id="display-test")
])

# Controls

# Chained Dropdown Callbacks

@callback(
    Output(component_id="year-dropdown", component_property="options"),
    Input(component_id="name-dropdown", component_property="value")
)
def get_year(name):
    year_options = search_df[search_df["Name"] == name]
    return[{'label': i, 'value': i} for i in year_options["Year"].unique()]

@callback(
    Output(component_id="year-dropdown", component_property="value"),
    Input(component_id="year-dropdown", component_property="options")
)
def select_year(year_options):
    return [k["value"] for k in year_options][0]

@callback(
    Output(component_id="display-test", component_property="children"),
    Input(component_id="name-dropdown", component_property="value"),
    Input(component_id="year-dropdown", component_property="value")
)
def display_test(name, year):
    return "".join([name, ", ", str(year)])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)