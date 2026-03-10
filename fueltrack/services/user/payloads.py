from faker import Faker

fake = Faker()

class Payload:

    create_user = {
        "tg_id": 123456789,
        "name": "Адим",
        "profile_name": "main",
        "gender": "male",
        "age": 25,
        "height": 180,
        "weight": 80,
        "goal": "loss",
        "activity": "medium"
    }

