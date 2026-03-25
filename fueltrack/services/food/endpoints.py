import os
from dotenv import load_dotenv

load_dotenv()

class EndpointFood:

    analyze_food = f'{os.getenv("HOST")}/api/food/analyze'
    save_food = f'{os.getenv("HOST")}/api/food/save'

    get_today_meals_and_tg = lambda self, tgId : f'{os.getenv("HOST")}/api/food/today/{tgId}'
    get_history_for_7_day = lambda self, tgId : f'{os.getenv("HOST")}/api/food/history/{tgId}'
