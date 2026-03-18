

class PayloadsFood:

    analyze_food = {
      "text": "борщ 300г"
    }

    analyze_food_image = {
        "image": "<base64_string>"
    }

    save_food = {
        "tg_id": 123456789,
        "profile_name": "test",
        "dish": "борщ",
        "calories": 350,
        "protein": 12.5,
        "fat": 8,
        "carbs": 45
    }


    negative_analyze_food = [
        {**analyze_food, "text": "боооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооооорщ 100г"},
        {**analyze_food, "text": ""},
        {**analyze_food, "text": " "},
    ]

