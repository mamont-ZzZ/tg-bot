import telebot
from telebot import types
import webbrowser
from telebot.util import content_type_media

bot = telebot.TeleBot('8131298081:AAGAv9Hxhyl8n5f_JZQTMxdkKcMMZaVKbBI')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('УЧАСТВУЮ', url='https://t.me/+agJ4ymR0vTA4NWZi'))
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!\nГоворит бот-помощник Даниэля.\nУ меня для тебя системное уведомление:\n\n'
                                      '🎉 <b>Событие:</b> День рождения Даниэля.\n'
                                      '📅 <b>Дата:</b> 10 января (сб)\n'
                                      '⏰ <b>Время:</b> 16:30\n'
                                      '📍 <b>Место:</b> <a href="https://yandex.ru/maps/11084/orenburg-oblast/house/molodyozhnaya_ulitsa_47/YUwYdwJnSU0PQFtrfXtzcX9lbQ==/?ll=55.157089%2C51.720370&z=16.63"><ins>п. Весенний, ул. Молодежная, 47</ins></a>\n\n'
                                      '<em>Я как цифровой ассистент обязан проинформировать, что ваше присутствие значительно увеличит шансы на успешное проведение праздника.</em>\n\n'
                                      'Для подтверждения участия нажми <b>"УЧАСТВУЮ"</b>\n\n'
                                      'Ваш,\n'
                                      'Виртуальный организатор Даниэля 🤖\n', parse_mode='html', disable_web_page_preview=True, reply_markup=markup)

@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, message.text)
bot.polling()
