import random


class Tournament:
    def __init__(self):
        global finalResult
        self.playerscore = 0
        self.dealerscore = 0
        tournamentOn = True
        while tournamentOn:
            match = Game()
            playgame = match.start()
            if playgame == "Dealer":
                self.dealerscore += 1
            if playgame == "Player":
                self.playerscore += 1    
            playq = input("Play again?(Y/N)")
            if playq != "Y" or playq != "y":
                tournamentOn = False
                print(f"Dealer endscore is {self.dealerscore} and Player endscore is {self.playerscore}")
                print("Cya!")
        

class Game:
    def __init__(self):
        self.player = Player("Sami")
        self.dealer = Player("Dealer")

    def phase1(self):
        global gameOver
        global finalResult
        print("\n\nWelcome to Black Jack v0.1")
        print("Dealer shuffles and deals first cards....", end="\n\n")
        self.player.situation()
        self.dealer.situation()
        print(f"Player {self.player.name} can now ask for more cards...\n\n")
        if self.player.cards[0].ranknum == 11 or self.player.cards[0].ranknum == 10 and self.player.cards[1].ranknum == 11 or self.player.cards[1].ranknum == 10:
            print("Player has BlackJack!!")
            finalResult = "Player"
            gameOver = True

    def phase2(self):
        global gameOver
        global finalResult
        checkMore = True
        while checkMore:
            question = input("Do you want more cards? (Y/N)")
            if question == "Y" or question == "y":
                self.player.addCard()
                self.player.situation()
            else:
                checkMore = False
        if self.player.total() > 21:
            print(f"Player went over ({self.player.total()}). Unfortunately Dealer Won!")
            finalResult = "Dealer"
            gameOver = True
        if self.player.total() == 21:
            print(f"Player has 21!! Player Won!")
            finalResult = "Player"
            gameOver = True
            

    def phase3(self):
        global gameOver
        global finalResult
        while self.dealer.total() < 17:
            self.dealer.addCard()
            self.dealer.situation()
        if self.dealer.total() > 21:
            print(f"Dealer went over ({self.dealer.total()}). Player Won!")
            finalResult = "Player"
            gameOver = True
        if self.dealer.total() == 21:
            print(f"Dealer has 21!! Dealer Won!")
            finalResult = "Dealer"
            gameOver = True
    
    def phase4(self):
        global finalResult
        if self.dealer.total() < self.player.total():
            print("Player Won!")
            finalResult = "Player"
        elif self.dealer.total() > self.player.total():
            print("Dealer Won!")
            finalResult = "Dealer"
        elif self.dealer.total() == self.player.total():
            print("Dealer Won because both had equal!")
            finalResult = "Dealer"
        else:
            print("WTF")


    def start(self):
        global finalResult
        global gameOn
        global gameOver
        while gameOn:
            self.phase1()
            if gameOver == False:
                self.phase2()
            if gameOver == False:
                self.phase3()
            if gameOver == False:
                self.phase4()
            gameOn = False
            return finalResult

class Player:
    def __init__(self, name):
        self.cards = [Card(), Card()]
        self.name = name    
    
    def situation(self):
        if self.name == "Dealer":
            print(f'\n\n{self.name} cards are:')
        else:
            print(f'\n\nPlayer {self.name} cards are:')
        for i in self.cards:
            i.printCards()
        print("")
    def addCard(self):
        self.cards.append(Card())

    def total(self):
        total = 0
        aces = 0
        for i in self.cards:
            if i.ranknum > 10:
                i.ranknum = 10
            if i.ranknum == 1 and total <= 10:
                i.ranknum = 11
                aces += 1
            if i.ranknum == 1 and total > 21 and aces > 0:
                total -= 10
                if i.ranknum == 1 and total <= 10:
                    i.ranknum == 11
            total += i.ranknum
        return total

class Card:
    def __init__(self):
        self.suit, self.rank, self.ranknum = cardSuitRank(getCard())
    
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    
    def getRankNum(self):
        return self.ranknum

    def printCards(self):
        print(f"{self.rank} of {self.suit}")
    
def cardNames(cardId):
    if cardId == 1:
        rank = "Ace"
    elif cardId == 11:
        rank = "Jack"
    elif cardId == 12:
        rank = "Queen"
    elif cardId == 13:
        rank = "King"
    else:
        rank = str(cardId)
    return rank

def cardSuitRank(cardId):
    if cardId in range(1, 14):
        suit = "Heart"
    elif cardId in range(14, 27):
        suit = "Spade"
        cardId = cardId - 13
    elif cardId in range(27, 40):
        suit = "Club"
        cardId = cardId - 26
    elif cardId in range(40, 53):
        suit = "Diamond"
        cardId = cardId - 39
    else:
        suit = "Error"
    
    return suit,cardNames(cardId),cardId

def getCard():
    randomCard = random.randint(1,53)
    while randomCard not in deck:
        randomCard = random.randint(1,53)
    deck.remove(randomCard)
    return randomCard

finalresult = "Unknown"
gameOver = False
gameOn = True
deck = list(range(1,53))

def main():
    Tournament()

if __name__ in "__main__":
    main()