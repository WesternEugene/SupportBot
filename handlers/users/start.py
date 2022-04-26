from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Добрый день, {message.from_user.full_name}!\nЭто техподдержка магазина Terry Shop!\n\nЧто бы отправить одно сообщение техподдержке, используйте команду /support.\n\nЧто бы начать переписку с оператором техподдержки, используйте команду /support_call")
