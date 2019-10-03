from src.api.match_v4 import get_match_by_summoner_name, get_match_by_id
from src.util.riot_utils import get_champion_key_to_name_dict


def get_participant_id_from_identities(summ_name, identities):
    for identity in identities:
        if identity['player']['summonerName'] == summ_name:
            return identity['participantId']
    return None


def get_participant_from_participant_id(part, part_id):
    for part in participants:
        if part['participantId'] == part_id:
            return part
    return None


def get_stat_from_participant(stat, part):
    return part['stats'][stat]


if __name__ == '__main__':
    summoner_name = "Lu the Dirty"
    matches_by_summoner_response = get_match_by_summoner_name(summoner_name)

    last_five_matches = matches_by_summoner_response['matches'][0:5]

    champion_keys_to_names = get_champion_key_to_name_dict()

    for match in last_five_matches:
        champion_key = match['champion']
        champion_name = champion_keys_to_names[str(champion_key)]

        match_id = match['gameId']

        match_details = get_match_by_id(match_id)
        game_mode = match_details['gameMode']

        participant_identities = match_details['participantIdentities']
        participant_id = get_participant_id_from_identities(summoner_name, participant_identities)
        participants = match_details['participants']
        participant = get_participant_from_participant_id(participants, participant_id)

        win = get_stat_from_participant("win", participant)
        kills = get_stat_from_participant("kills", participant)
        deaths = get_stat_from_participant("deaths", participant)
        assists = get_stat_from_participant("assists", participant)
        outcome_str = "WIN" if win else "LOSS"

        print("Lu's Outcome: {}, Champion: {}, Game Mode: {}".format(outcome_str, champion_name, game_mode))
        print("Kills: {}, Deaths {}, Assists: {}".format(kills, deaths, assists))
