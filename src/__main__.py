# Данный файл обозначает поведение модуля `src` при попытке
# его вызова посредством команды `python3 -m src`.

from src.app import bot

# Обратите внимание, здесь нет практически ничего, кроме
# метода запуска <bot.run_forever()>, который начинает поллинг. 
# Этот файл предназначен исключительно для запуска приложения.

bot.run_forever()