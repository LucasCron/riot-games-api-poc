from src.api.champion_mastery_v4 import get_mastery_by_summoner
from src.api.data_dragon import get_champions

if __name__ == '__main__':

    summoner_name = "Lu the Dirty"
    champion_masteries_by_summoner_response = get_mastery_by_summoner(summoner_name)
    champion_data = get_champions()

    champion_keys_to_names = {}
    # Make map for key -> name
    for (champion_name, champion_key) in champion_data['data'].items():
        champion_keys_to_names[str(champion_key['key'])] = str(champion_name)

    total_level = 0
    total_score = 0
    for champion in champion_masteries_by_summoner_response:
        champ_id = champion['championId']
        champ_name = champion_keys_to_names[str(champ_id)]
        champ_level = champion['championLevel']
        total_level += champ_level
        champ_score = champion['championPoints']
        total_score += champ_score
        print("Champion: {}, Level: {}, Score: {}".format(champ_name, champ_level, champ_score))

    print("Total level: {}".format(total_level))
    print("Total score: {}".format(total_score))
