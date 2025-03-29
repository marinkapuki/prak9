from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import re

app = FastAPI()

# Регулярное выражение для проверки формата Accept-Language (опционально)
LANGUAGE_REGEX = r"^[a-zA-Z-]+(,\s*[a-zA-Z-]+(;\s*q=[0-9.]+)?)*$"

@app.get("/headers")
async def get_headers(request: Request):
    # Извлекаем заголовки
    user_agent = request.headers.get("User-Agent")
    accept_language = request.headers.get("Accept-Language")

    # Проверка наличия обязательных заголовков
    if not user_agent or not accept_language:
        raise HTTPException(
            status_code=400,
            detail="Missing required headers: User-Agent or Accept-Language"
        )

    # Опциональная проверка формата Accept-Language
    if not re.match(LANGUAGE_REGEX, accept_language):
        raise HTTPException(
            status_code=400,
            detail="Invalid Accept-Language format"
        )

    return JSONResponse({
        "User-Agent": user_agent,
        "Accept-Language": accept_language
    })
