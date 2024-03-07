import unittest
from infra.api_wrapper import APIWrapper
from logic.decks import DeckOfCards
from logic.pile import Pile


class PileTest(unittest.TestCase):
    pile_name = "player1"

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.deck = DeckOfCards(self.my_api)
        add_deck_resp = self.deck.add_new_deck()
        self.deck_id = self.deck.get_deck_id()
        self.pile = Pile(self.my_api)
        card_response = self.deck.draw_card(deck_id=self.deck_id, count=1).json()
        self.card_name = self.deck.get_card_name()
        self.response = self.pile.add_to_pile(deck_id=self.deck_id, name=self.pile_name, cards=self.card_name)


    def test_add_cards_to_pile(self):
        decks_piles = self.response.json()
        cards_in_pile = self.pile.list_cards_in_pile(deck_id=self.deck_id, name=self.pile_name).json()
        self.assertTrue(self.response.status_code, 'Didnt get status 200 OK')
        self.assertEqual(1, decks_piles["piles"][self.pile_name]["remaining"], "card wasnt added to pile")
        self.assertEqual(cards_in_pile["piles"][self.pile_name]["cards"][0]["code"], self.card_name)

    def test_draw_cards_to_pile(self):
        self.pile.add_to_pile(deck_id=self.deck_id, name=self.pile_name, cards=self.card_name)
        discared_card_response = self.pile.draw_from_pile(deck_id=self.deck_id, name=self.pile_name,card=self.card_name)
        cards_in_pile = self.pile.list_cards_in_pile(deck_id=self.deck_id, name=self.pile_name).json()
        resp_json = discared_card_response.json()
        self.assertTrue(discared_card_response.status_code, 'Didnt get status 200 OK')
        self.assertEqual(self.card_name, resp_json["cards"][0]["code"])
        self.assertEqual(0, cards_in_pile["piles"][self.pile_name]["remaining"])

    def tearDown(self):
        self.deck.return_cards_from_pile(self.deck_id, self.pile_name)
        self.deck.return_cards(self.deck_id)
