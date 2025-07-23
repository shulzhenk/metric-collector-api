# app/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Класс для загрузки и валидации настроек из переменных окружения.
    Pydantic автоматически находит переменные, переданные Docker Compose
    """

    # Описываем наши переменные.
    db_name: str
    db_user: str
    db_pass: str
    db_host: str
    db_port: str

# Создаем один экземпляр настроек, который будем импортировать в другие файлы
settings = Settings()