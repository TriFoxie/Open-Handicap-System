class Course:
    score = 0.00
    rating = 0.00
    slope = 0.00
    def __init__(self, sc, ra, sl):
        self.score = sc
        self.rating = ra
        self.slope = sl

class Profile:
    lastTwenty = [-100, -100, -100, -100, -100,
                    -100, -100, -100, -100, -100, 
                    -100, -100, -100, -100, -100, 
                    -100, -100, -100, -100, -100,]
    def __init__(self, lt):
        self.lastTwenty = lt
    def Add(self, diff):
        i = 1
        j = 0
        while i < len(self.lastTwenty):
            self.lastTwenty[j] = self.lastTwenty[i]
            i += 1
            j += 1
        self.lastTwenty[19] = diff

    def GetHandicap(self):
        #find top 8
        s = 0
        n = 0
        topEight = [-100, -100, -100, -100, -100, -100, -100, -100]
        for x in self.lastTwenty:
            i = 0
            while i < len(topEight):
                if (topEight[i] == -100 or x < topEight[i]) and x != -100:
                    topEight[i] = x
                    i = 8
                    s += 1
                i += 1
        for x in topEight:
            if float(x) != -100:
                n += float(x)
        if s > 0:
            return n/s
        return "<Not enough data>"

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
        save.write(str(Player.lastTwenty[i]))
        if i < 20 - 1:
            save.write(",")
        i += 1
    save.close()

#Initialize profile (tracked handicap)
name = str(input("Name: "))
tempLastTwenty = [-100, -100, -100, -100, -100,
                -100, -100, -100, -100, -100, 
                -100, -100, -100, -100, -100, 
                -100, -100, -100, -100, -100,]
try:
    save = open(name + ".ohs", "r")
    data = save.read()
    i = 0
    while i < 20:
        tempLastTwenty[i] = float(data.split(',')[i])
        i += 1
except:
    print("No save file found, starting new profile")
Player = Profile(tempLastTwenty)

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
    else:
        print("Invalid Input")