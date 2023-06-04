from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('ChatBoot')

# Criação do treinador
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.portuguese")

def get_response(message):
    return chatbot.get_response(message).text

while True:
    user_input = input('Você: ')
    response = get_response(user_input)
    print('ChatBot:', response)
