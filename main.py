# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
#
# # Обработка команды /start
# def start(update: Update, context: CallbackContext) -> None:
#     user = update.effective_user
#     context.user_data['choice'] = None  # Инициализация переменной для хранения выбора пользователя
#     update.message.reply_html(
#         fr"Привет, {user.mention_html()}! Выберите вариант ответа:",
#         reply_markup=get_keyboard_markup(),
#     )
#
# # Обработка текстовых сообщений
# def handle_text(update: Update, context: CallbackContext) -> None:
#     text = update.message.text
#     context.user_data['choice'] = text  # Сохранение выбора пользователя
#     handle_choice(update, context)  # Обработка выбора пользователя
#
# # Обработка выбора пользователя
# def handle_choice(update: Update, context: CallbackContext) -> None:
#     choice = context.user_data['choice']
#     if choice == "Вариант 1":
#         update.message.reply_text("Вы выбрали первый вариант ответа.")
#     elif choice == "Вариант 2":
#         update.message.reply_text("Вы выбрали второй вариант ответа.")
#     elif choice == "Вариант 3":
#         update.message.reply_text("Вы выбрали третий вариант ответа.")
#     elif choice == "Вариант 4":
#         update.message.reply_text("Вы выбрали четвертый вариант ответа.")
#     else:
#         update.message.reply_text("Пожалуйста, выберите вариант ответа из предложенных.")
#
#     # Очистка выбора пользователя
#     context.user_data['choice'] = None
#
# # Отправка клавиатуры с вариантами ответов
# def get_keyboard_markup():
#     keyboard = [
#         ["Вариант 1", "Вариант 2"],
#         ["Вариант 3", "Вариант 4"],
#     ]
#     return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
#
# def main() -> None:
#     # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
#     updater = Updater("6303983490:AAHWquQFd1UrO2YIbUFi3KglobHAAx0BVUI")
#
#     dp = updater.dispatcher
#
#     # Обработка команды /start
#     dp.add_handler(CommandHandler("start", start))
#
#     # Обработка текстовых сообщений
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
#
#     updater.start_polling()
#
#     updater.idle()
#
# if __name__ == '__main__':
#     main()
#
