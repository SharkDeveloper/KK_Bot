from vk_api.keyboard import VkKeyboard,VkKeyboardColor

def create_keyboard(buttons: list):
    keyboard = VkKeyboard(one_time=False, inline=True)
    for i in range(len(buttons)):
        keyboard.add_button(
            label=buttons[i],
            color=VkKeyboardColor.SECONDARY,
        )

    return keyboard

class Buttons():
    Step1 = ["Выплаты","Университет","Прочее"]
    Viplati = ["Проблемы с выплатами стипендии"]