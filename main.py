from telebot import TeleBot
import uuid
import speech_recognition as sr
import os
import subprocess
import random
from data_preprocess import data_preprocessing
from config import return_config,return_API_TOKEN, return_responses
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

API_TOKEN = return_API_TOKEN()

bot = TeleBot(API_TOKEN)

config = return_config()

responses = return_responses()

def recognize(message,file_path):
    try:
        with sr.AudioFile(file_path) as source:
            # Уровень окружающего шума #
            audio_text = recog.listen(source) 
            recog.adjust_for_ambient_noise(source)
            audio_text = recog.recognize_google(audio_text, language = "ru-RU")
            return audio_text
    except sr.WaitTimeoutError:
        bot.send_message(message.chat.id, 'Я тебя не услышал! Проверь микро')
        return 1
    except sr.UnknownValueError:
        bot.send_message(message.chat.id, 'Я тебя не понял! \nВыражайся яснее что ли')
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEEtNVie__4NjE4PJGCYW_a3vmk9JyFxwAClioAAulVBRgLdLMUEsstzCQE")
        return 1
    except sr.RequestError:
        bot.send_message(message.chat.id, 'Проверь свой интернет!')
        return 1

def prepare_corpus():
    corpus = []
    target_vector = []

    for intent_name, intent_data in config['intents'].items():
        for example in intent_data['examples']:
            corpus.append(example)
            target_vector.append(intent_name)
    
    training_data = vectorizer.fit_transform(corpus)
    pac.fit(training_data, target_vector)

def prediction_and_response(audio_text):
    
    prep_data = vectorizer.transform(audio_text)

    list_intents = list(pac.predict(prep_data))

    best_intent = max(list_intents, key=list_intents.count)
    
    response = ''

    for intent_name, intent_data in responses['intents'].items():
        if (best_intent == intent_name):
            response = intent_data

    return response

def respond_to_recognize(response, message):
    bot.send_message(message.chat.id,response[random.randint(0 , len(response) - 1)])

@bot.message_handler(commands=['bye','пока'])
def bye(message):
    bot.send_message(chat_id=message.chat.id, text='Goodbye!')

@bot.message_handler()
def echo(message):
    bot.send_message(chat_id=message.chat.id, text='You said : ' + message.text)

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    filename = str(uuid.uuid4())
    file_name_full = 'telegram_bot/voice/' + filename + ".ogg"
    file_name_full_converted = 'telegram_bot/ready/' + filename + ".wav"
    
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    subprocess.run('ffmpeg -i '+file_name_full+'  '+file_name_full_converted)

    audio_text = recognize(message, file_name_full_converted)

    if (audio_text == 1):
        os.remove(file_name_full)
        os.remove(file_name_full_converted)
    else:

        audio_text = data_preprocessing(audio_text)

        response = prediction_and_response(audio_text)

        respond_to_recognize(response, message)

        os.remove(file_name_full)
        os.remove(file_name_full_converted)

if (__name__ == '__main__'):

    corpus = []
    target_vector = []

    recog = sr.Recognizer()

    vectorizer = TfidfVectorizer()
    pac = PassiveAggressiveClassifier()

    prepare_corpus()

    bot.polling(non_stop=True)
