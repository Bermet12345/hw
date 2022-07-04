from handlers import fsadmin_register, callback_quiz, admin, client, extra
from config import dp
from aiogram.utils import executor

client.register_handlers_client(dp)
admin.register_handler_admin(dp)
callback_quiz.register_handlers_callback_quiz(dp)
extra.register_handlers_extra(dp)
fsadmin_register.register_handler_registration(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
