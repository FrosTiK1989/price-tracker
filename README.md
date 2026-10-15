# Price Tracker

Telegram-бот для отслеживания цен на комплектующие для ПК.

- Собирает цены из нескольких магазинов и хранит историю.
- Сравнивает цену нового товара (DNS) с рыночной ценой б/у (Avito).
- Присылает уведомление, когда цена опустилась ниже заданного порога или до исторического минимума.

## Стек

Python 3.13, FastAPI, Pydantic, uv, ruff, mypy, pytest.

Планируется: PostgreSQL, SQLAlchemy, Redis, aiogram, Docker.

## Запуск

Нужен установленный [uv](https://docs.astral.sh/uv/).

```bash
# установить зависимости
uv sync

# создать файл настроек из шаблона
cp .env.example .env               # Linux / macOS
Copy-Item .env.example .env        # Windows PowerShell

# запустить сервер
uv run price-tracker
```

Проверить, что всё работает:

- http://127.0.0.1:8000/health — должен вернуть `{"status": "ok"}`
- http://127.0.0.1:8000/docs — документация API

## Разработка

```bash
uv run ruff format .     # форматирование
uv run ruff check .      # линтер
uv run mypy .            # проверка типов
uv run pytest            # тесты
```

## Статус

В разработке, этап 1: каркас проекта и CI.
