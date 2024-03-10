from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# токен бота
TOKEN = '6303983490:AAHWquQFd1UrO2YIbUFi3KglobHAAx0BVUI'
# URL Jenkins
JENKINS_URL = 'http://localhost:8080/'
# Имя задачи в Jenkins
JENKINS_JOB_NAME = 'first'
JENKINS_USERNAME = 'admin'
JENKINS_TOKEN = '112753489e70fd2f684dfff86538276e4e'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для управления Jenkins. Используйте /build для запуска сборки.')


def build(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    # Проверка, что команда была вызвана в группе
    if update.message.chat.type == "group":
        update.message.reply_text('Запуск автотестов на Jenkins...')

    response = requests.post(JENKINS_URL)
    auth = (JENKINS_USERNAME, JENKINS_TOKEN)
    url = f'{JENKINS_URL}/job/{JENKINS_JOB_NAME}/build'
    response = requests.post(url, auth=auth)
    if response.status_code == 201:
        update.message.reply_text('Сборка запущена успешно!')
    else:
        update.message.reply_text('Ошибка при запуске сборки.')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    # Обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("build", build))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
