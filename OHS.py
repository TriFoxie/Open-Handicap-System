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
            s += x
            if x == 0:
                n -= 1
        for x in self.topTwenty:
            s += x
            if x == 0:
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

#Initialize profile (tracked handicap)
Player = Profile() #Creates blank, add filesaves

#Main input loop
while True:
    print("===== Handicap Calculator=====\n"
    "Your Handicap: " + str(Player.GetHandicap()) + "\n"
    "[1] - Single Match Handicap\n"
    "[2] - Multiple Match Handicap\n"
    "[3] - Add Score")
    try:
        command = int(input())
        if command == 1:
            print("Round Handicap: " + str(SingleScore()))
        elif command == 2:
            MultipleScore()
        elif command == 3:
            Player.Add(SingleScore())
    except:
        print("Invalid Input")