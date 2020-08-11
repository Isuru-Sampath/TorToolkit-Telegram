from telethon import TelegramClient,events 
from telethon.tl.types import KeyboardButtonCallback
from ..consts.ExecVarsSample import ExecVars
from ..core.getCommand import get_command
from ..core.getVars import get_val
from ..functions.Leech_Module import check_link,cancel_torrent

def add_handlers(bot: TelegramClient):
    bot.add_event_handler(handle_leech_command,events.NewMessage(pattern=get_command("LEECH"),chats=ExecVars.ALD_USR))
    bot.add_event_handler(handle_test_command,events.NewMessage(pattern="/test",chats=ExecVars.ALD_USR))
    bot.add_event_handler(callback_handler,events.CallbackQuery(pattern="torcancel"))

#*********** Handlers Below ***********

async def handle_leech_command(e):
    if not e.is_reply:
        await e.reply("Reply to a link or magnet")
    else:
        path = await check_link(e)
        if path is not None:
            print(path)

async def handle_test_command(e):
    msg = await e.reply("tset")
    await msg.edit(
        file="/mnt/d/GitMajors/TorToolkit/test.html",
        text="modified"
    )
async def callback_handler(e):
    
    mes = await e.get_message()
    mes = await mes.get_reply_message()
    
    if mes.from_id == e.sender_id:
        hashid = str(e.data).split(" ")[1]
        hashid = hashid.strip("'")
        print("hashid - ",hashid)
        await cancel_torrent(hashid)
        await e.answer("The torrent has been cancled ;)",alert=True)
    elif mes.from_id in get_val("ALD_USR"):
        hashid = str(e.data).split(" ")[1]
        hashid = hashid.strip("'")
        print("hashid - ",hashid)
        await cancel_torrent(hashid)
        await e.answer("The torrent has been cancled in ADMIN MODE XD ;)",alert=True)
    else:
        await e.answer("You can cancel only your torrents ;)")