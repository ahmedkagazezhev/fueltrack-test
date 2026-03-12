from faker import Faker

fake = Faker()

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

    negative_payloads = [
        {**create_user, "tg_id": 0},
        {**create_user, "tg_id": -10},
        {**create_user, "profile_name": "helicopter20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"},
        {**create_user, "profile_name": ""},
        {**create_user, "profile_name": " "},
    ]