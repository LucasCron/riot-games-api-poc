from src.api.match_v4 import get_match_by_summoner_name, get_match_by_id
from src.util.riot_utils import jprint, get_champion_key_to_name_dict

if __name__ == '__main__':
    summoner_name = "Lu the Dirty"
    matches_by_summoner_response = get_match_by_summoner_name(summoner_name)

    last_five_matches = matches_by_summoner_response['matches'][0:5]
    jprint(last_five_matches)

    champion_keys_to_names = get_champion_key_to_name_dict()

    for match in last_five_matches:
        champion_key = match['champion']
        champion_name = champion_keys_to_names[str(champion_key)]

        match_id = match['gameId']
        match_details = get_match_by_id(match_id)
        game_mode = match_details['gameMode']

        # TODO scan participant identities for matching summoner name
        # TODO check participant for win status

        print("Champion: {} - Game Moder: {}".format(champion_name, game_mode))
