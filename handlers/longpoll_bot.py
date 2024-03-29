from utils.VK_API import Bot  # базовый класс бота из файла simple_bot

from vk_api.longpoll import VkLongPoll, VkEventType  # использование VkLongPoll и VkEventType
from handlers import messages

class LongPollBot(Bot):
    """
    Бот, прослушивающий в бесконечном цикле входящие сообщения и способный отвечать на некоторые из них
    Бот отвечает на строго заданные сообщения
    """

    # длительное подключение
    long_poll = None

    def __init__(self):
        """
        Иинициализация бота
        """
        super().__init__()
        self.long_poll = VkLongPoll(self.vk_session)

    def run_long_poll(self):
        """
        Запуск бота
        """

        message = str()

        for event in self.long_poll.listen():

            # если пришло новое сообщение - происходит проверка текста сообщения
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

                if event.text == "Выплаты":
                    messages.payments(self, event)
                elif event.text == "Университет":
                    messages.university(self,event)


                # ответ отпрвляется в беседу (если сообщение было получено в общем чате)
                elif event.from_chat:
                    self.send_message(receiver_user_id=event.chat_id, message_text="Всем привет")
