import pandas as pd


search_df = pd.read_csv("./output/database/search-data.csv")

'''
Player Class contains:
name - player name
year - season end-year
club - player club
unique_ID - player unique identifier (combined name, year, club)
war_overall - overall calculated WAR score
war_league - league-only calculated WAR score
percentile_overall - overall position-based percentile of WAR score
percentile_league - league-only position-based percentile of WAR score
self.actual_value - current transfermarkt valuation (or formulated valuation if not present)
self.projected_value_overall - projected value based on overall WAR score 
self.projected_value_league- projected value based on league-only WAR score 
'''

class Player:
    
    def __init__(self, name, year, club):
        self.name = name
        self.year = year
        self.club = club
        self.initialise_war()
    
    def initialise_war(self):
        self.unique_ID = "_".join([self.name, str(self.year), self.club])

        # Query formulas search for role/league suffix given a certain unique ID
        overall_player_df_location = "".join(["./output/PCA/overall_", search_df.query("unique_ID == @self.unique_ID")["Role"].iloc[0], "_war.csv"])
        league_player_df_location = "".join(["./output/PCA/overall_", search_df.query("unique_ID == @self.unique_ID")["Role"].iloc[0], "_war_", search_df.query("unique_ID == @self.unique_ID")["suffix"].iloc[0], ".csv"])
        overall_player_df = pd.read_csv(overall_player_df_location).query("unique_ID == @self.unique_ID")
        league_player_df = pd.read_csv(league_player_df_location).query("unique_ID == @self.unique_ID")
        self.war_overall = overall_player_df["calculated_war"].iloc[0]
        self.war_league = league_player_df["calculated_war"].iloc[0]
        self.percentile_overall = overall_player_df["percentile"].iloc[0]
        self.percentile_league = league_player_df["percentile"].iloc[0]
        self.actual_value = overall_player_df["player_market_value_euro"].iloc[0]
    