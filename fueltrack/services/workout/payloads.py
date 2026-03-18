class PayloadWorkOut:

    save_workout_set_payload = {
        "tg_id": 123456789,
        "profile_name": "test",
        "exercise": "Жим лёжа",
        "weight_kg": "80",
        "sets": 3,
        "reps": 10
    }

    negative_save_workout_payloads = [
        # отрицательные значения
        {"tg_id": 123456789, "profile_name": "test", "exercise": "Жим лёжа", "weight_kg": -80, "sets": -3, "reps": -10},
        # нулевые значения
        {"tg_id": 123456789, "profile_name": "test", "exercise": "Жим лёжа", "weight_kg": 0, "sets": 0, "reps": 0},
        # пустой profile_name
        {"tg_id": 123456789, "profile_name": "", "exercise": "Жим лёжа", "weight_kg": 80, "sets": 3, "reps": 10},
        # отрицательный tg_id
        {"tg_id": -123456789, "profile_name": "test", "exercise": "Жим лёжа", "weight_kg": 80, "sets": 3, "reps": 10},
        # int вместо str в profile_name
        {"tg_id": 123456789, "profile_name": 1, "exercise": "Жим лёжа", "weight_kg": 80, "sets": 3, "reps": 10},
        # float вместо int в tg_id
        {"tg_id": 124.4, "profile_name": "test", "exercise": "Жим лёжа", "weight_kg": 80, "sets": 3, "reps": 10},
        # str вместо int в weight_kg
        {"tg_id": 123456789, "profile_name": "test", "exercise": "Жим лёжа", "weight_kg": "80", "sets": 3, "reps": 10},
    ]

    negative_get_today_workouts = [
        {'tg_id': 0},
        {'tg_id': -60},
        {'tg_id': 100},
        {'tg_id': ""},
        {'tg_id': " "},
        {'tg_id': True},
    ]

    negative_get_workout_history = [
        {'tg_id': 123456789,"exercise": ""},
        {'tg_id': 0,"exercise": ""},
        {'tg_id': 123456789,"exercise": " "},
        {'tg_id': 123456789,"exercise": 123},
        {'tg_id': 123456789,"exercise": bool},
    ]