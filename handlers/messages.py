from vk_api.keyboard import VkKeyboard,VkKeyboardColor

def create_keyboard(buttons: list):
    keyboard = VkKeyboard(one_time=False, inline=True)
    for i in range(len(buttons)):
        keyboard.add_button(
            label=buttons[i],
            color=VkKeyboardColor.SECONDARY,
        )

    return keyboard

def payments(self,event):
    promlems = ["со стипендией","мат. помощью","иные"]
    keyboard = create_keyboard(promlems)

    # ответ отправляется в личные сообщения пользователя (если сообщение из личного чата)
    if event.from_user:
        self.send_message(receiver_user_id=event.user_id,message_text="Проблемы с выплатами связаные с чем?",keyboard=keyboard)

#TODO
#реализовать колбеки