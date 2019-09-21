import json
import os

import requests


class RiotUtils:

    def format_summoner_name(self, summoner_name):
        return summoner_name.replace(" ", "%20")

    def jprint(self, obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def get_api_response_json(self, url, parameters):
        return requests.get(url, parameters).json()


if __name__ == '__main__':

    riot_utils = RiotUtils()
    API_KEY = os.environ['API_KEY']
    SUMMONER_NAME = "Lu the Dirty"
    parameters = {"api_key": API_KEY}

    formatted_summoner_name = riot_utils.format_summoner_name(SUMMONER_NAME)
    # print("Formatted summoner name: {}".format(formatted_summoner_name))

    summoner_by_name_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(
        formatted_summoner_name)
    summoner_by_name_response = riot_utils.get_api_response_json(summoner_by_name_url, parameters)
    # riot_utils.jprint(summoner_by_name_response)

    id = summoner_by_name_response['id']
    champion_masteries_by_summoner_url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by" \
                                         "-summoner/{}".format(id)
    champion_masteries_by_summoner_response = riot_utils.get_api_response_json(champion_masteries_by_summoner_url,
                                                                               parameters)
    # riot_utils.jprint(champion_masteries_by_summoner_response)

    ddragon_response_url = "http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json"
    ddragon_response_json = riot_utils.get_api_response_json(ddragon_response_url, parameters)

    champ_key_to_name_dict = {}
    # Make map for key -> name
    for (name, key) in ddragon_response_json['data'].items():
        champ_key_to_name_dict[str(key['key'])] = str(name)

    total_level = 0
    total_score = 0
    for item in champion_masteries_by_summoner_response:
        champ_id = item['championId']
        champ_name = champ_key_to_name_dict[str(champ_id)]
        champ_level = item['championLevel']
        total_level += champ_level
        champ_score = item['championPoints']
        total_score += champ_score
        print("Champion: {}, Level: {}, Score: {}".format(champ_name, champ_level, champ_score))

    print("Total level: {}".format(total_level))
    print("Total score: {}".format(total_score))
