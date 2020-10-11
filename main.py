import random

class Card:
    def __init__(self, deck):
        self.suit, self.rank, self.ranknum = cardSuitRank(getCard(deck))
    
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    
    def getRankNum(self):
        return self.ranknum
    
    def printCards(self):
        print(self.getRank() + " of " + self.getSuit())

class Player:
    def __init__(self, name, deck):
        self.cards = [Card(deck), Card(deck)]
        self.name = name    
    
    def situation(self):
        print(f'Player {self.name} has:')
        for i in self.cards:
            i.printCards()

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

def getCard(deck):
    randomCard = random.randint(1,53)
    while randomCard not in deck:
        randomCard = random.randint(1,53)
    deck.remove(randomCard)
    return randomCard


def main():
    deck = list(range(1,53))
    you = Player("Sami",deck)
    dealer = Player("Dealer",deck) 
    you.situation()
    dealer.situation()

if __name__ in "__main__":
    main()