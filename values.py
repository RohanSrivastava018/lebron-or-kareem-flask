from nba_api.stats.static import players
import pandas as pd
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo

def getValues(name):

    player_dict = players.get_players()
    player_id = None
    #player ids
    for player in player_dict:
        if player['full_name'].lower() == name.lower():
            full_name = player['full_name']
            first_name = player['first_name']
            player_id = player['id']
            break

    if player_id == None:
        return None
    kareem_id = 76003 #kareem's id is 76003, DO NOT CHANGE

    #get points and difference
    player_pts = int(playercareerstats.PlayerCareerStats(player_id = player_id).career_totals_regular_season.get_data_frame().get('PTS'))
    kareem_pts = int(playercareerstats.PlayerCareerStats(player_id = kareem_id).career_totals_regular_season.get_data_frame().get('PTS'))
    diff = kareem_pts - player_pts
    player_ppg = float(commonplayerinfo.CommonPlayerInfo(player_id = player_id).player_headline_stats.get_data_frame().get('PTS'))
    games_left = int(diff / player_ppg) + 1

    return {'kareem_pts': kareem_pts,'player_pts': player_pts,'diff': diff, 'player_ppg': player_ppg,
             'games_left': games_left, 'full_name' : full_name, 'first_name' : first_name}