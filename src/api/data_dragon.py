from src.api.base_api import get_from_riot_api

champion_url = "http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json"


def get_champions():
    return get_from_riot_api(champion_url)
