import requests as req
import json

url = f"https://lichess.org/api/player/top/200/blitz" #Lichess api top 200 blitz link

players = req.get(url).json()

player_list = []
for username in players['users']: 
    player_list.append(username['id']) #Appends each username to the list of users

