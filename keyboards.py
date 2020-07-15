from aiogram import types
from misc import posts_cb


def get_keyboard(answers) -> types.InlineKeyboardMarkup:
    """
    Генерирует клавиатуру из списка кортежей answers и ссылки back
    """
    markup = types.InlineKeyboardMarkup()
    for answer, link in answers:
        if answer.startswith('link'):
            answer = answer.replace('link="', '')
            url = answer[:answer.index('"')]
            print(url)
            answer = answer[answer.index('"'):]
            markup.add(
                types.InlineKeyboardButton(
                    answer,
                    url=url),
            )
        else:
            markup.add(
                types.InlineKeyboardButton(
                    answer,
                    callback_data=posts_cb.new(id=link, action='view')),
            )
    return markup
