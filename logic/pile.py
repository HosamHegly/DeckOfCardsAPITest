from infra import config_reader


class Pile:

    def __init__(self, api_object):
        self.my_api = api_object
        self.url = config_reader.get_config_data()['url']

    def add_to_pile(self, name, deck_id, cards):
        result = self.my_api.api_get_request(f"{self.url}{deck_id}/pile/{name}/add/?cards={cards}")
        return result

    def list_cards_in_pile(self, name, deck_id):
        result = self.my_api.api_get_request(f"{self.url}{deck_id}/pile/{name}/list/")
        return result

    def draw_from_pile(self, name, deck_id, card):
        result = self.my_api.api_get_request(f"{self.url}{deck_id}/pile/{name}/draw/?cards={card}")
        return result
