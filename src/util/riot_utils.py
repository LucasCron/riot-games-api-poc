import json

from src.api.data_dragon import get_champions


def format_summoner_name(summoner_name):
    return summoner_name.replace(" ", "%20")


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_champion_key_to_name_dict():
    champion_keys_to_names = {}
    for (champion_name, champion_key) in get_champions()['data'].items():
        champion_keys_to_names[str(champion_key['key'])] = str(champion_name)
    return champion_keys_to_names
