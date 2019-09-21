from src.api.base_api import get_from_riot_api
from src.api.champion_v4 import get_summoner_by_name

base_url = "https://na1.api.riotgames.com"
by_summoner_url = "{}/lol/champion-mastery/v4/champion-masteries/by-summoner/{}"
scores_by_summoner_url = "{}/lol/champion-mastery/v4/scores/by-summoner/{}"


def get_mastery_by_summoner(summoner_name):
    summoner_id = get_summoner_by_name(summoner_name).get('id')
    url = by_summoner_url.format(base_url, summoner_id)
    return get_from_riot_api(url)


def get_scores_by_summoner(summoner_name):
    summoner_id = get_summoner_by_name(summoner_name).get('id')
    url = scores_by_summoner_url.format(base_url, summoner_id)
    return get_from_riot_api(url)
