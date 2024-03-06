from infra.api_wrapper import APIWrapper
from infra import config_reader

class DeckOfCards:

    def __init__(self, api_object):
        self.my_api = api_object
        self.url = config_reader.get_config_data()['url']
    def shuffel_deck(self,count):
        result = self.my_api.api_get_request(f'{self.url}new/shuffle/?deck_count={count}')
        return result


    def reshuffel_deck(self,id):
        result = self.my_api.api_get_request(f'{self.url}{id}/shuffle/?remaining=true')
        return result

    def add_new_deck(self):
        result = self.my_api.api_get_request(f"{self.url}new/")
        return result

    def return_cards(self,id):
        result = self.my_api.api_get_request(f"{self.url}{id}/return/")
        return result

    def return_cards_from_pile(self,id,pile_name):
        result = self.my_api.api_get_request(f"{self.url}{id}/pile/{pile_name}/return/")
        return result

    def draw_card(self, deck_id, count):
        result = self.my_api.api_get_request(f"{self.url}{deck_id}/draw/?count={count}")
        return result

