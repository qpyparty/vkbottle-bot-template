from vkbottle.user import User
from vkbottle.tools import load_blueprints_from_package

from src.config import USERBOT_TOKEN
from src.initialize import setup_db


def init_user() -> "User":
    user = User(token=USERBOT_TOKEN)
    setup_blueprints(user)
    setup_middlewares(user)
    return user


def setup_blueprints(user: User):
    for bp in load_blueprints_from_package("src/blueprints"):
        bp.load(user)


def setup_middlewares(user: User):
    for bp in load_blueprints_from_package("src/middlewares"):
        bp.load(user)


user = init_user()
user.loop_wrapper.on_startup.append(setup_db())
