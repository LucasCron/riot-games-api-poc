from src.api.champion_mastery_v4 import get_mastery_by_summoner
from src.api.champion_v4 import get_summoner_by_name
from src.api.data_dragon import get_champions

if __name__ == '__main__':

    summoner_name = "Lu the Dirty"
    summoner_by_name_response = get_summoner_by_name(summoner_name)
    champion_masteries_by_summoner_response = get_mastery_by_summoner(summoner_name)
    ddragon_response_json = get_champions()

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
