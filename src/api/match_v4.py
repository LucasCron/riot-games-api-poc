from src.api.base_api import get_from_riot_api
from src.api.summoner_v4 import get_summoner_by_name

base_url = "https://na1.api.riotgames.com"
match_by_account = "{}/lol/match/v4/matchlists/by-account/{}"
match_by_id = "{}/lol/match/v4/matches/{}"


def get_match_by_summoner_name(summoner_name):
    account_id = get_summoner_by_name(summoner_name).get('accountId')
    url = match_by_account.format(base_url, account_id)
    return get_from_riot_api(url)


def get_match_by_id(match_id):
    url = match_by_id.format(base_url, match_id)
    return get_from_riot_api(url)
