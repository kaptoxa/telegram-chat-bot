import exceptions
from aiogram import types
from scenario import scenario

from misc import dp


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_scenario(message: types.Message):
    print('new scenario!')
    try:
        scenario_file = await message.document.get_file()
        await scenario_file.download('new_scenario.xlsx')
        phrases = scenario.load('new_scenario.xlsx')

    except exceptions.NotCorrectScenarioFile as e:
        await message.answer(f"Файл сценария не может быть распаршен: {e}!")
        return await message.answer('Для дальнейшей работы бует использован старый сценарий.')

    except exceptions.NotCorrectScenarioLinks as e:
        await message.answer(f"Сценарий содержит ошики: {e}!")
        return await message.answer('Для дальнейшей работы бует использован старый сценарий.')

#    except Exception as e:
#        await message.answer(f"Unkown exception!: {e}")
#        return await message.answer('Для дальнейшей работы бует использован старый сценарий.')

    return await message.answer('Новый сценарий диалогов успешно сохранён')
