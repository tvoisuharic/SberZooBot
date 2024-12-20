import os
import telebot
from gigachat_function import get_animal_description
from yolodetection import get_animal_from_image
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import configs
import strings
from animals import animals

bot = telebot.TeleBot(configs.TG_API)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(strings.HELP_BUTTON_TEXT)
    markup.add(btn1)
    bot.send_message(message.chat.id, text=strings.START_TEXT, reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, text=strings.PROCESS_PHOTO_TEXT)
    photo_info = message.photo[-1]
    photo_id = photo_info.file_id
    photo_part = bot.get_file(photo_id).file_path
    downloaded_file = bot.download_file(photo_part)
    save_path = 'photo'
    os.makedirs(save_path, exist_ok=True)
    file_name = f'{photo_id}.jpg'
    photo_path = os.path.join(save_path, file_name)
    with open(photo_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    animal_name = get_animal_from_image(photo_path)
    animal_discription = get_animal_description(animal_name)
    bot.reply_to(message, animal_discription)

@bot.message_handler(content_types=['text'])
def get_animal_text(message):
    if message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, text=strings.HELP_TEXT)
        return

    bot.send_message(message.chat.id, text=strings.PROCESS_NAME_TEXT)
    if message.text.lower() in animals:
        animal_description = get_animal_description(message.text)
        bot.reply_to(message, animal_description)
    else:
        bot.reply_to(message, strings.WRONG_ANIMAL_TEXT)

bot.polling(none_stop=True)