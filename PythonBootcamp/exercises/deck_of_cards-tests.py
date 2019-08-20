import unittest
from deck_of_cards import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.test_card = Card("Hearts", "Q")

    def test_init(self):
        """card should have suit and value"""
        self.assertEqual(self.test_card.suit, "Hearts")
        self.assertEqual(self.test_card.value, "Q")

    def test_repr(self):
        """card should be printed as 'Q of Hearts'"""
        self.assertEqual(repr(self.test_card), 'Q of Hearts')


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.test_deck = Deck()

    def test_init(self):
        """new deck should have 52 cards"""
        self.assertEqual(len(self.test_deck.cards), 52)

    def test_repr(self):
        """deck should be printed as 'Deck of 52 cards'"""
        self.assertEqual(repr(self.test_deck), "Deck of 52 cards")

    def test_count(self):
        """count method should return len of cards attribute"""
        self.assertEqual(self.test_deck.count(), len(self.test_deck.cards))

    def test_deal_card(self):
        """deal 1 card from the deck. Deck has 51 cards now"""
        self.test_deck.deal_card()
        self.assertTrue(len(self.test_deck.cards) == 51)

    def test_deal_hand(self):
        """deal 5 cards from the deck. Deck has 47 cards now"""
        self.test_deck.deal_hand(5)
        self.assertTrue(len(self.test_deck.cards) == 47)

if __name__ == "__main__":
    unittest.main()