# app/main.py

import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .config import settings

# Модель данных 
class Visit(BaseModel):
    page_url: str

# Создание приложения FastAPI 
app = FastAPI(
    title="Metric Collector API",
    description="Простой сервис для сбора метрик посещений",
    version="1.0.0",
)

def get_db_connection():
    """
    Устанавливает и возвращает соединение с базой данных.
    В случае ошибки подключения вызывает HTTPException 500.
    """
    try:
        conn = psycopg2.connect(
            dbname=settings.db_name,
            user=settings.db_user,
            password=settings.db_pass,
            host=settings.db_host,
            port=settings.db_port
        )
        return conn
    except psycopg2.OperationalError as e:
        raise HTTPException(status_code=500, detail=f"Ошибка подключения к базе данных: {e}")

# API Эндпоинты

@app.post("/visit", status_code=201)
def add_visit(visit: Visit) -> dict:
    """
    Регистрирует новый визит.

    Принимает URL страницы и сохраняет информацию о визите в БД.
    Возвращает статус операции.
    """
    # `with` автоматически управляет открытием/закрытием соединения и курсора
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO visits (page_url) VALUES (%s)",
                (visit.page_url,)
            )
            # conn.commit() неявно вызывается при выходе из блока `with`
    return {"status": "ok", "message": f"Визит на {visit.page_url} записан."}

@app.get("/stats")
def get_stats() -> list[dict]:
    """
    Возвращает статистику по всем визитам.

    Данные отсортированы по времени в порядке убывания (сначала новые).
    """
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id, page_url, timestamp FROM visits ORDER BY timestamp DESC")
            visits = cur.fetchall()
    return visits

@app.get("/")
def root() -> dict:
    """Корневой эндпоинт для проверки работы сервиса."""
    return {"message": "Добро пожаловать в Metric Collector! Документация API доступна по адресу /docs"}