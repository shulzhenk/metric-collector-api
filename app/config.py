# app/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Класс для загрузки и валидации настроек из переменных окружения.
    """
    # Указываем pydantic, что нужно искать файл .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

    # Описываем наши переменные. Pydantic автоматически их найдет и проверит типы.
    db_name: str
    db_user: str
    db_pass: str
    db_host: str
    db_port: str

# Создаем один экземпляр настроек, который будем импортировать в другие файлы
settings = Settings()