from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class Bot:
    def __init__(self, name):
        self.bot = ChatBot(name)
        
    def get_response(self, input):
        return self.bot.get_response(input)
    
    def train_list(self, data: list):
        trainer = ListTrainer(self.bot)
        trainer.train(data)
        
    def validate_response(self, response):
        response.save()