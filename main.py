from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from get_items_of_user import get_items_of_user
from get_stat_of_user import get_stat_of_user

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Или "*" для всех доменов (небезопасно в продакшене)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все HTTP-методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешает все заголовки
)
router = APIRouter()


@router.get("/", summary="Получить данные пользователя")
async def get_user_info(
        steamId: str = Query(..., description="Steam ID пользователя", min_length=10, max_length=20)
):
    get_items_of_user(steamId)
    return get_stat_of_user(steamId)

app.include_router(router)