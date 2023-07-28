from aiogram import Bot, Dispatcher, executor, types

from pars import main
import io

TOKEN = '6170915635:AAEg1R58NXxnnA2rRt4PlkKgIz_Zk6bv5FM'


bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
def send_welcome(message: types.Message):
    return message.answer('To get file use /get_file command')


def send_csv(chat_id, file_path, caption=None):
    with open(file_path, 'r') as file:
        # Read the CSV data and convert it into a BytesIO object
        csv_data = file.read().encode()

    # Send the CSV file with the appropriate content_type
    return bot.send_document(chat_id, types.InputFile(io.BytesIO(csv_data), filename=file_path), caption=caption)


@dp.message_handler(commands=['get_file'])
def send_file(message: types.Message):
    main()
    chat_id = message.chat.id
    file_path = 'enter_kg.csv'
    caption = 'check out this csv file!'
    return send_csv(chat_id, file_path, caption=caption)


executor.start_polling(dp, skip_updates=True)





executor.start_polling(dp, skip_updates=True)