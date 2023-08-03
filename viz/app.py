import os
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from player_class import Player

# TODO: DOCUMENTATION 

# Change to your local folder before editing
os.chdir("C:/Users/tobyt/Desktop/Coding/Personal/wins-above-replacement-soccer/WAR-based-soccer-valuation")

# Setup
search_df = pd.read_csv("./output/database/search-data.csv")

# Initialize the app
app = Dash(__name__)

# App layout
# TODO: adding stylesheet
app.layout = html.Div([
    html.H1(children="Implementing a WAR (Wins Above Replacement) Metric Into Major Soccer Leagues"),
    # Player 1
    html.Div([
        html.Div([
            dcc.Dropdown(options=list(search_df["Name"].unique()), placeholder="Player:", id="name-dropdown", clearable=False),
            dcc.Dropdown(options=[], placeholder="Year:", id="year-dropdown", clearable=False),
            dcc.Dropdown(options=[], placeholder="Club:", id="club-dropdown", clearable=False),
            html.Table([
                html.Tr([html.Td(id = "unique_ID"), html.Td(id = "position"), html.Td(id = "actual_value")]),
                html.Tr([html.Td(id = "war_overall"), html.Td(id = "war_league"), html.Td(id = "projected_value_overall")]),
                html.Tr([html.Td(id = "percentile_overall"), html.Td(id = "percentile_league"), html.Td(id = "projected_value_league")])
            ]),
            dcc.Graph(figure={}, id="overall-graph"),
            dcc.Graph(figure={}, id="league-graph")
        ], className = "grid-child"),
        # Player 2
        html.Div(
        # TODO: add Player2 
            html.Div(children="temp for css testing - player 2 functionality should be here")
        )
    ], className = "grid-container")


])

# Controls

# Chained Dropdown Callbacks - Player 1

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
    Output(component_id="club-dropdown", component_property="options"),
    Input(component_id="name-dropdown", component_property="value"),
    Input(component_id="year-dropdown", component_property="value")
)
def get_club(name, year):
    club_options = search_df.loc[(search_df["Name"] == name) & (search_df["Year"] == year)]
    return[{'label': i, 'value': i} for i in club_options["Club"].unique()]
    

@callback(
    Output(component_id="club-dropdown", component_property="value"),
    Input(component_id="club-dropdown", component_property="options")
)
def select_club(club_options):
    return [k["value"] for k in club_options][0]

# Table - Player 1
@callback(
    Output(component_id="unique_ID", component_property="children"),
    Output(component_id="position", component_property="children"),
    Output(component_id="war_overall", component_property="children"),
    Output(component_id="war_league", component_property="children"),
    Output(component_id="percentile_overall", component_property="children"),
    Output(component_id="percentile_league", component_property="children"),
    Output(component_id="actual_value", component_property="children"),
    Output(component_id="projected_value_overall", component_property="children"),
    Output(component_id="projected_value_league", component_property="children"),
    Input(component_id="name-dropdown", component_property="value"),
    Input(component_id="year-dropdown", component_property="value"),
    Input(component_id="club-dropdown", component_property="value")
)
def generate_table(name, year, club):
    Player1 = Player(name, year, club)

    overall_df = pd.read_csv("".join(["./output/PCA/overall_", search_df.query("unique_ID == @Player1.unique_ID")["Role"].iloc[0], "_war.csv"]))
    overall_fig = px.scatter(overall_df, x="calculated_war", y="player_market_value_euro", trendline="ols")
    overall_results = px.get_trendline_results(overall_fig)
    overall_params = overall_results.iloc[0]["px_fit_results"].params
    league_df = pd.read_csv("".join(["./output/PCA/overall_", search_df.query("unique_ID == @Player1.unique_ID")["Role"].iloc[0], "_war_", search_df.query("unique_ID == @Player1.unique_ID")["suffix"].iloc[0], ".csv"]))
    league_fig = px.scatter(league_df, x="calculated_war", y="player_market_value_euro", trendline="ols")
    league_results = px.get_trendline_results(league_fig)
    league_params = league_results.iloc[0]["px_fit_results"].params

    print(overall_params)
    print(league_params)

    unique_ID = "".join(["Unique ID: ", Player1.unique_ID])
    position = "".join(["Position: ", search_df.query("unique_ID == @Player1.unique_ID")["Role"].iloc[0]])
    war_overall = "".join(["Overall WAR: ", str(round(Player1.war_overall, 2))])
    war_league = "".join(["League-Only WAR: ", str(round(Player1.war_league, 2))])
    percentile_overall = "".join(["Overall Percentile %: ", str(round(Player1.percentile_overall, 2))])
    percentile_league = "".join(["League-Only Percentile %: ", str(round(Player1.percentile_league, 2))])
    actual_value = "".join(["Actual Market Value: ", "{:,}".format(round(Player1.actual_value, 0))])
    projected_value_overall = "".join(["Projected Overall Market Value: ", "{:,}".format(round(overall_params[0] + (overall_params[1] * Player1.war_overall), 0))])
    projected_value_league = "".join(["Projected League-Only Market Value: ", "{:,}".format(round(league_params[0] + (league_params[1] * Player1.war_league), 0))])
    
    print(unique_ID, position, war_overall, war_league, percentile_overall, percentile_league, actual_value, projected_value_overall, projected_value_league, sep="\n")
    return unique_ID, position, war_overall, war_league, percentile_overall, percentile_league, actual_value, projected_value_overall, projected_value_league

# Graphs - Player 1

@callback(
    Output(component_id="overall-graph", component_property="figure"),
    Input(component_id="name-dropdown", component_property="value"),
    Input(component_id="year-dropdown", component_property="value"),
    Input(component_id="club-dropdown", component_property="value")
)
def update_overall_graph(name, year, club):
    Player1 = Player(name, year, club)
    overall_df = pd.read_csv("".join(["./output/PCA/overall_", search_df.query("unique_ID == @Player1.unique_ID")["Role"].iloc[0], "_war.csv"]))
    fig = px.scatter(overall_df, x="calculated_war", y="player_market_value_euro", hover_data=["unique_ID"], trendline="ols", 
                     title="".join([Player1.name, " (", str(Player1.year), ") WAR compared to all players in ", search_df.query("unique_ID == @Player1.unique_ID")["Role"].iloc[0].replace("-", " ")]))
    fig.add_traces(px.scatter(overall_df[overall_df["unique_ID"] == Player1.unique_ID], x="calculated_war", y="player_market_value_euro", hover_data=["unique_ID"])
                   .update_traces(marker_size = 20, marker_color = "yellow").data)
    return fig

@callback(
    Output(component_id="league-graph", component_property="figure"),
    Input(component_id="name-dropdown", component_property="value"),
    Input(component_id="year-dropdown", component_property="value"),
    Input(component_id="club-dropdown", component_property="value")
)
def update_league_graph(name, year, club):
    Player1 = Player(name, year, club)
    league_df = pd.read_csv("".join(["./output/PCA/overall_", search_df.query("unique_ID == @Player1.unique_ID")["Role"].iloc[0], "_war_", search_df.query("unique_ID == @Player1.unique_ID")["suffix"].iloc[0], ".csv"]))
    fig = px.scatter(league_df, x="calculated_war", y="player_market_value_euro", hover_data=["unique_ID"], trendline="ols",
                     title="".join([Player1.name, " (", str(Player1.year), ") WAR compared to all ", search_df.query("unique_ID == @Player1.unique_ID")["suffix"].iloc[0]," players in ", search_df.query("unique_ID == @Player1.unique_ID")["Role"].iloc[0].replace("-", " ")]))
    fig.add_traces(px.scatter(league_df[league_df["unique_ID"] == Player1.unique_ID], x="calculated_war", y="player_market_value_euro", hover_data=["unique_ID"])
                   .update_traces(marker_size = 20, marker_color = "yellow").data)
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)