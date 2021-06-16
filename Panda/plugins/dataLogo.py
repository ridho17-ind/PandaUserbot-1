import re
import time
from platform import python_version

from telethon import version
from telethon.events import CallbackQuery

from Panda import StartTime, pandaub, pandaversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time, pandaalive
from ..helpers.utils import reply_id
from . import mention

CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "✮ BOT PANDA SUCCESSFULLY ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  🐼 "

plugin_category = "utils"


@pandaub.ilhammansiz_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if Config.ALIVE_PIC:
        panda_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        panda_caption += f"**{EMOJI} Database :** `{check_sgnirts}`\n"
        panda_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
        panda_caption += f"**{EMOJI} Bot Version :** `{pandaversion}`\n"
        panda_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
        panda_caption += f"**{EMOJI} Uptime :** `{uptime}\n`"
        panda_caption += f"**{EMOJI} Sudo  :** {Config.SUDO_ENABLED}\n"
        panda_caption += f"**{EMOJI} Master:** {mention}\n\n"
        panda_caption += (
            f"**{EMOJI} Repo :** [Klik](https://github.com/ilhammansiz/PandaUserbot)\n"
        )
        panda_caption += (
            f"**{EMOJI} Support :** [Klik](https://t.me/TEAMSquadUserbotSupport)\n"
        )
        panda_caption += f"**{EMOJI} Creator :** [Klik](http://t.me/diemmmmmmmmmm)\n"
        await event.client.send_file(
            event.chat_id, Config.ALIVE_PIC, caption=panda_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            event,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} Bot Version :** `{pandaversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Sudo  :** {Config.SUDO_ENABLED}\n"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {mention}\n\n",
            f"**{EMOJI} Repo :** [Klik](https://github.com/ilhammansiz/PandaUserbot)\n"
            f"**{EMOJI} Support :** [Klik](https://t.me/TEAMSquadUserbotSupport)\n"
            f"**{EMOJI} Creator :** [Klik](http://t.me/diemmmmmmmmmm)\n",
        )


@pandaub.ilhammansiz_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    panda_caption = f"**Pandauserbot is Up and Running**\n"
    panda_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    panda_caption += f"**{EMOJI} PetercordBot Version :** `{pandaversion}`\n"
    panda_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    panda_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, panda_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@pandaub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await pandaalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
