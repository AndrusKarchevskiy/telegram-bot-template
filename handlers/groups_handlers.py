from loader import dp, types
from aiogram.types.chat import ChatType
from utils.keyboards.groups import inline_markups as inl_markups, reply_markups as repl_markups
from utils.fsm import groups_fsm as fsm
from utils.template_messages import groups_template_messages as templ_msgs
from data.database import groups_db as db


@dp.message_handler(ChatType.is_private, commands='start')
async def send_welcome(message: types.Message):
    await message.answer('Привет')
