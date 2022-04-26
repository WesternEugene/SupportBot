from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/support - напистаь одно сообщение в техподдержку",
            "/support_call - начать переписку с оператором техподдержки",
            "/help - показать этот список")
    
    await message.answer("\n".join(text))
