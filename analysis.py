import numpy
import math





class PlayerVector:
    
    def __init__(self, name, games):
        self.username = name
        self.games = games 

    def normalize(self): #Takes the games vector and divides each value by the magnitude of the vector
        squared = 0
        for value in self.games:
            squared += value**2
        magnitude = math.sqrt(squared) #Essentially just sqrt(x1^2 + x2^2 +x3^2...)
        for value in self.games:
            value = value / magnitude 

    def compare(self, otherPlayer):
        self.normalize()
        otherPlayer.normalize()

        difference = numpy.subtract(self.games, otherPlayer.games)
        squared = 0
        for value in difference:
            squared += value**2
        return math.sqrt(squared)


vectors = []

with open("data.txt", "r") as readFile:
    text = readFile.read()
    userdata = text.split("User: ")
    del userdata[0]
    for user in userdata:
        games = numpy.zeros(500)
        splitdata = user.split()
        ecos = splitdata[1:]
        for eco in ecos:

            mapped_eco = 0
            match eco[0]:
                case "A":
                    mapped_eco = int(eco[1:])

                case "B":
                    mapped_eco = int(eco[1:]) + 100

                case "C":
                    mapped_eco = int(eco[1:]) + 200

                case "D":
                    mapped_eco = int(eco[1:]) + 300

                case "E":
                    mapped_eco = int(eco[1:]) + 400

            games[mapped_eco] += 1
        #print(games)
        vectors.append(PlayerVector(splitdata[0], games))



#distances = numpy.zeros((200,200))
for x in range(0,len(vectors)-1):
    for y in range(x+1, len(vectors) - 1):
        #distances[(x,y)]
        print(f"{vectors[x].username} distance compared to {vectors[y].username}: {vectors[x].compare(vectors[y])}")


   