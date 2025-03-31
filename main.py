from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Query, HTTPException
import logging

from get_items_of_user import get_items_of_user
from get_stat_of_user import get_stat_of_user

from fastapi import FastAPI, APIRouter, Query
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,  # Для разработки используем DEBUG
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),  # Вывод в консоль
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для теста разрешаем все домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.get("/test")
async def test():
    logger.debug("Тестовое сообщение")
    return {"status": "ok"}

@router.get("/")
async def get_user_info(
    steamId: str = Query(..., description="Steam ID пользователя")
):
    logger.info(f"Получен запрос для SteamID: {steamId}")
    try:
        logger.debug("Начало обработки запроса")
        get_items_of_user(steamId)
        response_data = get_stat_of_user(steamId)
        logger.debug(f"Успешный ответ")
        return response_data
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(router)
logger.info("Приложение запущено")