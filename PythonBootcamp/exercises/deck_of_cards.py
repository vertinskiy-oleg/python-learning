from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(s,v) for s in suits for v in values]

    def __repr__(self):
        return "Deck of {} cards".format(len(self.cards))

    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
        dealt = []
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        elif num > len(self.cards):
            num = len(self.cards)
        for n in range(num):
            dealt.append(self.cards.pop())
        return dealt

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


if __name__ == "__main__":
    card = Card("Hearts", "Q")
    print(card)    
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck.deal_card())
    print(deck.deal_hand(5))
    print(deck)



