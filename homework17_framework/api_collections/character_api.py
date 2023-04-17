from homework17_framework.data_objects.character_data import CharacterData
from homework17_framework.utilities.api.base_api import BaseAPI


class CharacterAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__character_api = '/character'

    def get_character(self, character_id, headers=None):
        response = self.get(url=f'{self.__character_api}/{character_id}', headers=headers)
        return response

    def create_character(self, body=CharacterData(), headers=None, **kwargs):
        body.update_data(**kwargs)
        response = self.post(f'{self.__character_api}/', body=body.get_json(), headers=headers)
        return response
