from envparse import env


env.read_envfile(".env")

USERBOT_TOKEN = env.str("USERBOT_TOKEN")