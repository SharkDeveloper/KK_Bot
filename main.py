import vk_api
from vk_api.longpoll import VkLongPoll
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой

def msg_handler(longpoll):
    while True:
        for event in longpoll.listen():
            
def vk_connetion():
    load_dotenv()
    token = os.getenv("ACCESS_TOKEN")
    vk_session = vk_api.VkApi(token=token)
    session_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    msg_handler(longpoll)



if __name__=="__main__":
    vk_connetion()