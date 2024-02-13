import vk_api
from vk_api.longpoll import VkLongPoll
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой

from utils.VK_API import Bot
from handlers.longpoll_bot import LongPollBot
            
def vk_connetion():
    load_dotenv()
    user_id = os.getenv("USER_ID")

    bot = LongPollBot()
    bot.run_long_poll()
    #bot.send_message()

if __name__=="__main__":
    vk_connetion()