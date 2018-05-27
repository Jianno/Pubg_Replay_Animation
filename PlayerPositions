import Match
import requests
from datetime import datetime as dt
from datetime import timedelta as td

class PlayerPositions:
    def __init__(self, Match):
        teleUrl = Match.teleUrl
        teleJson = (requests.get(teleUrl, headers=Match.header)).json()

        self.positions = {}
        for player in Match.playerList:
            self.positions[player] = []

        for log in teleJson:
            if (log["_T"] == 'LogPlayerPosition') & (self.minutePassed((log["_D"])[8:18], Match.start)):
                x = self.posConversion(log["character"]["location"]["x"])
                y = self.posConversion(log["character"]["location"]["y"])
                if (log["character"]["name"] in self.positions):
                    (self.positions[str(log["character"]["name"])]).append([log["_D"][8:19], (x, y)])

    def posConversion(self, pos):
        return int((((pos) * 1078) / 800000))

    def minutePassed(self, time1, time2):
        time1 = dt.strptime(time1, "%dT%H:%M:%S")
        time2 = dt.strptime(time2, "%dT%H:%M:%S") + td(0,60)
        return time1 > time2

