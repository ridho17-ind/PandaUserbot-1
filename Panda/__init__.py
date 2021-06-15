# ILHAM MANSIEZ
# PANDA USERBOT
# PANDA
import time

import heroku3

from .Config import Config
from .core import logger
from .core.session import pandaub

__version__ = "3.0.0"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "PandaUserBot <https://github.com/ilhammansiz/PandaUserbot>"
__copyright__ = "PandaUserBot Copyright (C) 2020 - 2021  " + __author__

pandaub.version = __version__
pandaub.tgbot.version = __version__
bot = pandaub

StartTime = time.time()
pandaversion = "5.0.0"

if Config.UPSTREAM_REPO == "panda":
    UPSTREAM_REPO_URL = "https://github.com/ilhammansiz/PandaUserbot"
elif Config.UPSTREAM_REPO == "panda":
    UPSTREAM_REPO_URL = "https://github.com/ilhammansiz/PandaUserbot"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


async def check_alive():
    await bot.send_message(BOTLOG_CHATID, "```🐼PANDA-USERBOT🐼\nMENYALA```")
    return


with bot:
    try:
        bot.loop.run_until_complete(check_alive())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file."
        )
        quit(1)

# Global
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}
