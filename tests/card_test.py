import unittest

import requests
import json
from types import SimpleNamespace

from infra.api_wrapper import APIWrapper
from logic.decks import DeckOfCards

class CardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_api = APIWrapper()


    def test_draw_card(self):
        self.deck = DeckOfCards(self.my_api)
        add_deck_resp = self.deck.add_new_deck().json()
        self.deck_id = add_deck_resp["deck_id"]
        for count in range(1,6):
            response = self.deck.draw_card(deck_id=self.deck_id ,count=count)
            self.assertTrue(response.status_code, 'Didnt get status 200 OK')
            response_json = response.json()
            self.assertEqual(len(response_json["cards"]), count)
            self.assertTrue(response_json["success"])


    def tearDown(self):
        self.deck.return_cards(self.deck_id)



