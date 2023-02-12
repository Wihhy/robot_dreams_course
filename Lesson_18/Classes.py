class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, message):
        print(message)


some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def set_url(self, url):
        self.url = url

    def send_message(self, message):
        print(f'Message is:{message}, was sent to chat ID:{self.chat_id}, with URL:{self.url}')


telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
telegram_bot.set_url('www.url.com')
telegram_bot.send_message('Hello')
