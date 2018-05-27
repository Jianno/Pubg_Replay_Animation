import requests

class Match:
    def __init__(self, key, matchid):
        endpointUrl = "https://api.playbattlegrounds.com/" \
                      "shards/pc-na/matches/" + matchid
        self.header = {
            "Authorization": key,
            "Accept": "application/vnd.api+json"
        }

        matchJson = (requests.get(endpointUrl, headers=self.header)).json()
        self.map = matchJson["data"]["attributes"]["mapName"]
        self.mode = matchJson["data"]["attributes"]["gameMode"]
        self.id = matchid
        self.playerList = [player['attributes']['stats']['name'] for player in matchJson["included"] if player["type"] == "participant"]
        self.duration = matchJson["data"]["attributes"]["duration"]
        self.start = (matchJson["data"]["attributes"]["createdAt"])[8:18]

        teleId = matchJson["data"]["relationships"]["assets"]["data"][0]["id"]

        dataArray = matchJson["included"]
        for index in range(len(dataArray)):
            if dataArray[index]["id"] == teleId:
                print("Telemetry data found")
                self.teleUrl = dataArray[index]["attributes"]["URL"]
                break
