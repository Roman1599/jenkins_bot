# import requests
# from flask import Flask, request
#
# app = Flask(__name__)
#
# def start_jenkins_build():
#     jenkins_url = "http://localhost:8080/job/first/build"
#     api_token = "feb13cb3748549348c344d4917f5fc24"
#     bot_token = "6303983490:AAHWquQFd1UrO2YIbUFi3KglobHAAx0BVUI"
#     chat_id = "-1002019866912"
#
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Basic MTEyNzUzNDg5ZTcwZmQyZjY4NGRmZmY4NjUzODI3NmU0ZQ=="
#     }
#
#     payload = {}
#
#     response = requests.post(jenkins_url, headers=headers, json=payload)
#
#     if response.status_code == 201:
#         message = "Build started successfully"
#     else:
#         message = f"Failed to start build. Status code: {response.status_code}, Response: {response.text}"
#
#     telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
#     telegram_params = {
#         "chat_id": chat_id,
#         "text": message
#     }
#
#     requests.post(telegram_url, json=telegram_params)
#
# @app.route(f'/{6303983490:AAHWquQFd1UrO2YIbUFi3KglobHAAx0BVUI}', methods=['POST'])
# def process_update():
#     data = request.get_json()
#
#     if "message" in data and "text" in data["message"]:
#         command = data["message"]["text"].lower()
#
#         if command == "/start":
#             response_text = "Hello! I'm your Jenkins bot. Use /build to start a Jenkins build."
#         elif command == "/build":
#             start_jenkins_build()
#             response_text = "Jenkins build started!"
#         else:
#             response_text = "Unknown command. Use /build to start a Jenkins build."
#
#         chat_id = data["message"]["chat"]["id"]
#         telegram_url = f"https://api.telegram.org/bot{6303983490:AAHWquQFd1UrO2YIbUFi3KglobHAAx0BVUI}/sendMessage"
#         telegram_params = {
#             "chat_id": chat_id,
#             "text": response_text
#         }
#
#         requests.post(telegram_url, json=telegram_params)
#
#     return "OK"
#
# if __name__ == "__main__":
#     app.run(port=5000)  # Замените 5000 на порт, который будете использовать для вебхука
