class Course:
    score = 0.00
    rating = 0.00
    slope = 0.00
    def __init__(self, sc, ra, sl):
        self.score = sc
        self.rating = ra
        self.slope = sl

class Profile:
    recents = [0.00, 0.00, 0.00]
    topTwenty = [0.00, 0.00, 0.00, 0.00, 0.00,
                0.00, 0.00, 0.00, 0.00, 0.00, 
                0.00, 0.00, 0.00, 0.00, 0.00, 
                0.00, 0.00, 0.00, 0.00, 0.00,]
    def __init__(self, ttt, r):
        self.topTwenty = ttt
        self.recents = r
    def Add(self, diff):
        #Add to recents (Queue)
        self.recents[0] = self.recents[1]
        self.recents[1] = self.recents[2]
        self.recents[2] = diff
        #Add to top twenty (if it fits)
        i = 0
        for x in self.topTwenty:
            if diff < x:
                self.Add(x) #Shift scores
                self.topTwenty[i] = diff
                break
            i += 1

    def GetHandicap(self):
        s = 0
        n = 23
        for x in self.recents:
            s += float(x)
            if float(x) == 0:
                n -= 1
        for x in self.topTwenty:
            s += float(x)
            if float(x) == 0:
                n -= 1
        if n > 0:
            return s/n
        return "<Not Enough Data>"

def GetDiff(score, rating, slope):
    return (score - rating) * 113 / slope

def SingleScore():
    print("Score: ")
    score = float(input())
    print("Rating: ")
    rating = float(input())
    print("Slope: ")
    slope = float(input())
    return GetDiff(score, rating, slope)

def MultipleScore():
    print("How many scores? ")
    n = float(input())
    s = 0
    i = 0
    while i < n:
        s += SingleScore()
        i += 1
    print("Overall Handicap: " + str(s/n))

def Save(name, Player):
    save = open(name + ".ohs", "w")
    i = 0
    while i < 20:
        save.write(str(Player.topTwenty[i]))
        if i < 20 - 1:
            save.write(",")
        i += 1
    save.write("|")
    i = 0
    while i < 3:
        save.write(str(Player.recents[i]))
        if i < 3 - 1:
            save.write(",")
        i += 1
    save.close()

#Initialize profile (tracked handicap)
name = str(input("Name: "))
temprecents = [0.00, 0.00, 0.00]
temptopTwenty = [0.00, 0.00, 0.00, 0.00, 0.00,
                0.00, 0.00, 0.00, 0.00, 0.00, 
                0.00, 0.00, 0.00, 0.00, 0.00, 
                0.00, 0.00, 0.00, 0.00, 0.00,]
try:
    save = open(name + ".ohs", "r")
    data = save.read()
    i = 0
    while i < 20:
        temptopTwenty[i] = data.split('q')[0].split(',')[i]
        i += 1
    i = 0
    while i < 3:
        temprecents[i] = data.split('q')[1].split(',')[i]
        i += 1
except:
    print("No save file found, starting new profile")
Player = Profile(temptopTwenty, temprecents)

#Main input loop
while True:
    print("===== Handicap Calculator=====\n"
    "[" + name + "] "
    "Your Handicap: " + str(Player.GetHandicap()) + "\n"
    "[1] - Single Match Handicap\n"
    "[2] - Multiple Match Handicap\n"
    "[3] - Add Score\n"
    "[4] - Save")
    command = int(input())
    if command == 1:
        print("Round Handicap: " + str(SingleScore()))
    elif command == 2:
        MultipleScore()
    elif command == 3:
        Player.Add(SingleScore())
    elif command == 4:
        Save(name, Player)
        print("Saved")
    print("Invalid Input")