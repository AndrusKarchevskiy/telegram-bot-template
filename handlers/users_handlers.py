from loader import dp, types
from aiogram.types.chat import ChatType
from utils.keyboards.users import inline_markups as inl_markups, reply_markups as repl_markups
from utils.fsm import users_fsm as fsm
from utils.template_messages import users_template_messages as templ_msgs
from data.database import users_db as db


@dp.message_handler(ChatType.is_group_or_super_group, commands='start')
async def send_welcome(message: types.Message):
    await message.answer('Привет')
