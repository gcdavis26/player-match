import requests as req
import json
import time

url1 = f"https://lichess.org/api/player/top/200/blitz" #Lichess api top 200 blitz link

players = req.get(url1).json()

player_list = []
for username in players['users']: 
    player_list.append(username['id']) #Appends each username to the list of users

open("data.txt", "w").close() #clear the file

for username in player_list:
    url2 = f"https://lichess.org/api/games/user/{username}"
    params = {"max" : 100, "rated" : True, "perfType" : "blitz", "moves": False, "tags" : False, "opening" : True}
    headers = {"Accept" : "application/x-ndjson"}

    games = (req.get(url2, params = params, headers = headers)).iter_lines()
    
    with open("data.txt", "a") as writeFile:
        writeFile.write(f"User: {username}\n")
        for game in games:
            json_game = json.loads(game)
            print(json_game)
            try:
                writeFile.write(f"{json_game['opening']['eco']}\n")
            except:
                break #Basically, if the game is resigned or whatever before an opening can be found

    time.sleep(1)
