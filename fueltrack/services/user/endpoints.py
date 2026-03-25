import os
from dotenv import load_dotenv

load_dotenv()

class EndpointUser:

    create_user = f'{os.getenv("HOST")}/api/user/setup'
    get_first_profile_user = lambda self, tgId : f'{os.getenv("HOST")}/api/user/{tgId}'
    get_tg_id_user = lambda self, tgId :f'{os.getenv("HOST")}/api/user/{tgId}/profiles'
    delete_tg_id_user = lambda self, tgId , profileName : f'{os.getenv("HOST")}/api/user/{tgId}/profiles/{profileName}'
    get_tg_id_profile_name_user = lambda self, tgId , profileName : f'{os.getenv("HOST")}/api/user/{tgId}/{profileName}'
