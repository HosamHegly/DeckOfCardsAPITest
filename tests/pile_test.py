import unittest
from infra.api_wrapper import APIWrapper
from logic.decks import DeckOfCards
from logic.pile import Pile


class PileTest(unittest.TestCase):
    pile_name = "my_pile"

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.deck = DeckOfCards(self.my_api)
        add_deck_resp = self.deck.add_new_deck().json()
        self.deck_id = add_deck_resp["deck_id"]
        self.pile = Pile(self.my_api)
        card_response = self.deck.draw_card(deck_id=self.deck_id, count=1).json()
        self.card_name = card_response["cards"][0]['code']

    def test_add_cards_to_pile(self):
        response = self.pile.add_to_pile(deck_id=self.deck_id, name=self.pile_name, cards=self.card_name)
        self.assertTrue(response.status_code, 'Didnt get status 200 OK')
        decks_piles = response.json()
        cards_in_pile = self.pile.list_cards_in_pile(deck_id=self.deck_id, name=self.pile_name).json()
        self.assertEqual(1, decks_piles["piles"][self.pile_name]["remaining"], "card wasnt added to pile")
        self.assertEqual(cards_in_pile["piles"][self.pile_name]["cards"][0]["code"], self.card_name)

    def test_draw_cards_to_pile(self):
        self.pile.add_to_pile(deck_id=self.deck_id, name=self.pile_name, cards=self.card_name)
        discared_card_response = self.pile.draw_from_pile(deck_id=self.deck_id, name=self.pile_name,                                             card=self.card_name)
        self.assertTrue(discared_card_response.status_code, 'Didnt get status 200 OK')
        resp_json = discared_card_response.json()
        self.assertEqual(self.card_name, resp_json["cards"][0]["code"])
        cards_in_pile = self.pile.list_cards_in_pile(deck_id=self.deck_id, name=self.pile_name).json()
        self.assertEqual(0, cards_in_pile["piles"][self.pile_name]["remaining"])

    def tearDown(self):
        self.deck.return_cards_from_pile(self.deck_id, self.pile_name)
        self.deck.return_cards(self.deck_id)
