import json


class RiotUtils:

    def format_summoner_name(self, summoner_name):
        return summoner_name.replace(" ", "%20")

    def jprint(self, obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
