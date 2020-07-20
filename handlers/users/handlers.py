from loader import bot, dp, types
from aiogram.types.chat import ChatType


@dp.message_handler(ChatType.is_private, commands='start')
async def send_welcome(message: types.Message):
    await message.answer('Привет')
