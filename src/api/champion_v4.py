from src.api.base_api import get_from_riot_api
from src.util.riot_utils import RiotUtils

riot_utils = RiotUtils()

base_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners"
by_account_url = "{}/by-account/{}"
by_name_url = "{}/by-name/{}"
by_puuid_url = "{}/by-puuid/{}"
by_id_url = "{}/{}"


def get_summoner_by_name(summoner_name):
    formatted_summoner_name = riot_utils.format_summoner_name(summoner_name)
    url = by_name_url.format(base_url, formatted_summoner_name)
    return get_from_riot_api(url)
