from infra import config_reader


class DeckOfCards:

    def __init__(self, api_object):
        self.my_api = api_object
        self.url = config_reader.get_config_data()['url']

    def shuffel_deck(self, count):
        result = self.my_api.api_get_request(f'{self.url}new/shuffle/?deck_count={count}')
        return result

    def reshuffel_deck(self, deck_id):
        result = self.my_api.api_get_request(f'{self.url}{deck_id}/shuffle/?remaining=true')
        return result

    def add_new_deck(self):
        self.deck = self.my_api.api_get_request(f"{self.url}new/")
        return self.deck

    def return_cards(self, deck_id):
        result = self.my_api.api_get_request(f"{self.url}{deck_id}/return/")
        return result

    def return_cards_from_pile(self, deck_id, pile_name):
        result = self.my_api.api_get_request(f"{self.url}{deck_id}/pile/{pile_name}/return/")
        return result

    def draw_card(self, deck_id, count):
        self.card = self.my_api.api_get_request(f"{self.url}{deck_id}/draw/?count={count}")
        return self.card

    def get_deck_id(self):
        return self.deck.json()['deck_id']

    def get_card_name(self):
        return self.card.json()["cards"][0]['code']
