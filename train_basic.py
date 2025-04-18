from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''


chatbot = ChatBot('Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    'chatterbot.corpus.english'
)

# Now let's get a response to a greeting
response = chatbot.get_response('Are you sapient?')
print(response)