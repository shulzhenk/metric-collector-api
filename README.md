# Metric Collector API

Простой веб-сервис для сбора метрик посещений. Этот проект является учебным и демонстрирует работу с FastAPI и PostgreSQL.



## 🚀 Технологии

- **Бэкенд:** Python 3.11
- **Фреймворк:** FastAPI
- **База данных:** PostgreSQL
- **Драйвер БД:** psycopg2-binary
- **Управление конфигурацией:** Pydantic-Settings, python-dotenv
- **Веб-сервер:** Uvicorn



## ✨ Возможности

- Запись информации о посещении страницы через POST-запрос.
- Получение списка всех посещений через GET-запрос.
- Автоматически генерируемая интерактивная документация API (Swagger UI).

## ⚙️ Установка и запуск

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/shulzhenk/metric-collector-api.git
    cd metric-collector-api
    ```

2.  **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    ```
    *   **На macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    *   **На Windows (PowerShell/CMD):**
        ```bash
        venv\Scripts\activate
        ```

3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройте переменные окружения:**
    Скопируйте файл-шаблон `.env.example` в новый файл `.env` и укажите в нем свои данные для подключения к PostgreSQL.

    *   **На macOS/Linux:**
        ```bash
        cp .env.example .env
        ```
    *   **На Windows (CMD):**
        ```bash
        copy .env.example .env
        ```
    *   **На Windows (PowerShell):**
        ```bash
        Copy-Item .env.example .env
        ```


5.  **Запустите приложение:**
    ```bash
    python -m uvicorn app.main:app --reload
    ```


6.  **Откройте документацию в браузере:**
    Перейдите по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📝 API Эндпоинты

- **`POST /visit`** — регистрирует новый визит.
  - **Тело запроса:** `{"page_url": "string"}`
- **`GET /stats`** — возвращает список всех визитов.
- **`GET /`** — корневой эндпоинт для проверки доступности.