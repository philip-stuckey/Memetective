import simplematrixbotlib as botlib
import nio
import os
import fire

@bot.listener.on_custom_event(nio.events.room_events.RoomMessageImage)
async def on_image_message(room, event):
    response = await asyn_bot.login("password")
    print(response)
    match = botlib.MessageMatch(room, event, bot)
    if match.is_not_from_this_bot() and room.is_group and room.member_count == 2:
        url = event.url
        urllist = url.split("/")
        response = await asyn_bot.download(urllist[2], urllist[3])
        fname="./"+event.source['content']['body']
        with open(fname, 'wb') as binary_file:
            binary_file.write(response.body)
            binary_file.close()
        if isinstance(response, nio.responses.DownloadError):
            await bot.api.send_text_message(room.room_id, "Bot image retrieval failed. Try again.")
            pass
        else:
            await bot.api.send_image_message(dumproom, fname)
            os.remove(fname)

def main(serveraddress="http://localhost:8008", botname, password, publicroom):
    creds = botlib.Creds(serveraddress, botname, password)
    bot = botlib.Bot(creds)
    asyn_bot = nio.AsyncClient(serveraddress, botname)
    dumproom = publicroom
    bot.run()