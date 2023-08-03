import os
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from unidecode import unidecode 

# LEGACY - CAN IGNORE (keeping code for reference, will remove in later iterations)

# Change to your local folder before editing
os.chdir("C:/Users/tobyt/Desktop/Coding/Personal/wins-above-replacement-soccer/WAR-based-soccer-valuation")

# Setup
positions = ['Centre-Forward', 'Left-Back', 'Right-Back', 'Right Winger', 'Central Midfield', 
            'Attacking Midfield', 'Centre-Back', 'Defensive Midfield', 'Second Striker', 
            'Left Winger', 'Right Midfield', 'Left Midfield']
positions_converter = {'Centre-Forward': 'centre-forward', 'Left-Back': 'left-back', 'Right-Back': 'right-back', 
                       'Right Winger': 'right-winger', 'Central Midfield': 'central-midfield', 
                       'Attacking Midfield': 'attacking-midfield', 'Centre-Back': 'centre-back', 
                       'Defensive Midfield': 'defensive-midfield', 'Second Striker': 'second-striker', 
                       'Left Winger': 'left-winger', 'Right Midfield': 'right-midfield', 'Left Midfield': 'left-midfield'}

leagues = ["🌎 Overall", "🇬🇧 Premier League", "🇪🇸 La Liga", "🇩🇪 Bundesliga", "🇮🇹 Italy", "🇫🇷 France"]
league_converter = {"🌎 Overall":"", "🇬🇧 Premier League":"_ENG", "🇪🇸 La Liga":"_ESP", 
                    "🇩🇪 Bundesliga":"_GER", "🇮🇹 Italy":"_ITA", "🇫🇷 France":"_FRA"}

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1(children="Implementing a WAR (Wins Above Replacement) Metric Into Major Soccer Leagues"),
    dcc.Dropdown(options=positions, value="Centre-Forward", id="positions-dropdown", clearable=False),
    dcc.Dropdown(options=leagues, value="🌎 Overall", id="league-dropdown", clearable=False),
    dcc.Graph(figure={}, id="graph")
])

# Controls
@callback(
    Output(component_id="graph", component_property='figure'),
    Input(component_id="positions-dropdown", component_property="value"),
    Input(component_id="league-dropdown", component_property="value")
)
def update_graph(position, league):
    file_string = "".join(["./output/PCA/overall_", positions_converter[position], "_war", league_converter[league], ".csv"])
    df = pd.read_csv(file_string)
    fig = px.scatter(df, x="calculated_war", y="player_market_value_euro", hover_data=["unique_ID"], trendline="ols")
    return fig



# Run the app
if __name__ == '__main__':
    app.run(debug=True)