"""this is the cards class"""

class cards:
    suits = ['Clubs','Diamonds','Hearts','Spades']
    ranks = ['narf','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    def __init__(self,suit=0,rank=0):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return (self.ranks[self.rank] + ' of ' + self.suits[self.suit])

    #this method ir for comparing cards
    def comp(self,other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        #this is for comparing the rank
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        #otherwise are equall
        return 0
    #operator overloading
    def __eq__(self,other):
        return self.comp(other) == 0
    def __le__(self,other):
        return self.comp(other)  <= 0
    def __ge__(self,other):
        return self.comp(other) >= 0
    def __gt__(self,other):
        return self.comp(other) > 0
    def __lt__(self,other):
        return self.comp(other) < 0
    def __ne__(self,other):
        return self.comp(other) != 0

"""this is the desk class"""

class desk:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.cards.append(cards(suit,rank))
    
    #the string operator
    def __str__(self):
        s = ''
        for i in range(len(self.cards)):
            s = s + ' ' * i + str(self.cards[i]) + '\n'
        return s
    
    #to shuffle the cards
    def shuffle(self):
        import random
        rnd = random.Random()
        rnd.shuffle(self.cards)

    #this is to remove cards from the desk
    def remove(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False
    
    #this method is form removing the last card of the desk
    def pop(self):
        return self.cards.pop()
    
    #this is for knowing if the desk is empty
    def is_empty(self):
        return self.cards == []

    #this is to give cards away to different hands
    def deal(self,hands,num_cards = 999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break #break if out of cards
            card = self.pop() #take the outermost card
            hand = hands[i % num_hands] #who is next
            hand.add(card) #give the card to the hand