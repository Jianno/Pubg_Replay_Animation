import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Match
import PlayerPosition
from datetime import datetime as dt

match = Match.Match("Pubg Api Key Here","Match Id Here")
gamePositions = PlayerPosition.PlayerPositions(match).positions

img = "Maps/Miramar.jpg"
if(match.map == "Erangel_Main"):
    img = plt.imread("Maps/Erangel.jpg")
fig = plt.figure(figsize=(8, 8), dpi=100)
plt.axis([0, match.mapSize, 0, match.mapSize])
fig, ax = plt.subplots()
ax.imshow(img)

survivors = match.playerList
plots = {}

N = len(survivors)
points = ax.plot( *([[], []]*N), marker="o")

def init():    
    for index in range(N):
        player = survivors[index]
        x,y = gamePositions[player][0][1]
        line = points[index]
        line.set_data([x], [y])
    return points

def update(index):
    for player in survivors:
        print(player + '\n')
        survivorIndex = survivors.index(player)
        if(index >= len(gamePositions[player])):
            points[survivorIndex].set_data([0], [0])
        else:
            x, y = gamePositions[player][index][1]
            points[survivorIndex].set_data([x], [y])
    return points



game = animation.FuncAnimation(fig, update, int(match.duration/10), init_func=init, interval=25, repeat=False)
fig.show()
