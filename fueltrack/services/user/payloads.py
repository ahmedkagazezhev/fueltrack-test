class Payload:

    create_user = {
        "tg_id": 123456789,
        "name": "Адим",
        "profile_name": "test",
        "gender": "male",
        "age": 25,
        "height": 180,
        "weight": 80,
        "goal": "loss",
        "activity": "medium"
    }

    NEGATIVE_TG_ID = 987654321

    negative_payloads = [
        {**create_user, "tg_id": 0},
        {**create_user, "tg_id": -10},
        {**create_user, "tg_id": NEGATIVE_TG_ID, "profile_name": "helicopter000..."},
        {**create_user, "tg_id": NEGATIVE_TG_ID, "profile_name": ""},
        {**create_user, "tg_id": NEGATIVE_TG_ID, "profile_name": " "},
    ]