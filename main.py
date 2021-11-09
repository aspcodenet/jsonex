from hockey import Player
import json
from  collections import namedtuple

allPlayers = []
with open('players.json', 'r') as f:
    data = json.load(f)
    for  dic in data:
        p = Player.create(dic)
        allPlayers.append(p)                    



p = Player()
p.Jersey = 130
p.Namn = "Mats Sundin0"
p.Team = "Toronto0"
allPlayers.append(p)

p = Player()
p.Jersey = 211
p.Namn = "1Peter Forsberg"
p.Team = "1Colorado"
allPlayers.append(p)

with open('players.json', 'w') as json_file:
    json.dump([b.__dict__ for b in allPlayers], json_file)
