
HOST = "https://fueltrack-production-f193.up.railway.app"

class Endpoint:

    create_user = f'{HOST}/api/user/setup'
    get_tg_id_user = lambda self, tgId :f'{HOST}/api/user/{tgId}/profiles'
    delete_tg_id_user = lambda self, tgId , profileName : f'{HOST}/api/user/{tgId}/profiles/{profileName}'
    get_tg_id_profile_name_user = lambda self, tgId , profileName : f'{HOST}/api/user/{tgId}/{profileName}'
