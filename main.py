import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', )

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp)
