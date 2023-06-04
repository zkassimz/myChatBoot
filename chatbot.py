from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criação do chatbot
chatbot = ChatBot('Meu ChatBot')

# Criação do treinador
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinamento do chatbot com o corpus de dados em português
trainer.train("chatterbot.corpus.portuguese")

# Função para receber e responder às mensagens
def get_response(message):
    return chatbot.get_response(message).text

# Loop para interação com o chatbot
while True:
    user_input = input('Você: ')
    response = get_response(user_input)
    print('ChatBot:', response)
