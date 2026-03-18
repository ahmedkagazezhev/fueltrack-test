
HOST = "https://fueltrack-production-f193.up.railway.app"

class EndpointFood:

    analyze_food = f'{HOST}/api/food/analyze'
    save_food = f'{HOST}/api/food/save'

    get_today_meals_and_tg = lambda self, tgId : f'{HOST}/api/food/today/{tgId}'
    get_history_for_7_day = lambda self, tgId : f'{HOST}/api/food/history/{tgId}'
