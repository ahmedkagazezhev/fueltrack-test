# FuelTrack Test Suite 🧪

Автоматизированное тестирование REST API для [FuelTrack](https://github.com/ahmedkagazezhev/fueltrack) — Telegram Mini App для учёта питания и тренировок.


## 🛠 Стек

- Python 3.11
- pytest + parametrize
- Pydantic v2 — валидация ответов
- Allure — отчётность
- GitHub Actions — CI/CD
- Railway — деплой тестируемого API

## 📁 Структура
```
fueltrack/
├── config/          # BaseTest, конфигурация
├── services/
│   ├── user/        # API клиент, модели, payload, endpoints
│   ├── food/        # API клиент, модели, payload, endpoints
│   └── workout/     # API клиент, модели, payload, endpoints
├── tests/
│   ├── test_users.py
│   ├── test_food.py
│   └── test_workout.py
└── utils/           # Helpers, Allure attachments
```

## 🚀 Запуск

**1. Клонировать репозиторий:**
```bash
git clone https://github.com/ahmedkagazezhev/fueltrack-test
cd fueltrack-test
```

**2. Установить зависимости:**
```bash
pip install -r requirements.txt
```

**3. Создать `.env` файл:**
```
HOST=https://fueltrack-production-f193.up.railway.app
```

**4. Запустить тесты:**
```bash
# Все тесты
pytest -sv

# По сервису
pytest fueltrack/tests/test_users.py -sv
pytest fueltrack/tests/test_food.py -sv
pytest fueltrack/tests/test_workout.py -sv
```

**5. Allure отчёт:**
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## ⚙️ CI/CD

Тесты автоматически запускаются через GitHub Actions при каждом push в `main`.

## 🐛 Найденные баги

В процессе тестирования задокументировано 14 багов:
- Отсутствие валидации входных данных (отрицательные значения, нулевые значения, неверные типы)
- `profile_name` и `exercise` возвращают `null` в GET /workout/today
- Отсутствие каскадного удаления данных при удалении пользователя