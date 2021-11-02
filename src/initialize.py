from typing import NoReturn
from tortoise import Tortoise


async def setup_db() -> NoReturn:
    await Tortoise.init(
        # Адрес вашей локальной базы данных
        db_url="sqlite://db.sqlite",
        # В поле `models` необходимо передавать пути
        # к модулям, содержащим модели Tortoise
        # в формате `src.database.*`
        modules={"models": []}
    )
    await Tortoise.generate_schemas()
