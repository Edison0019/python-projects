import cards

class hand(cards.desk):
    def __init__(self,name=''):
        self.name = name
        self.cards = []
    
    #this is for adding cards to the hand
    def add(self,card):
        return self.cards.append(card)
    