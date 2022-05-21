def return_responses():
    return responses

def return_config():
    return config

def return_API_TOKEN():
    return API_TOKEN

API_TOKEN = "5322759567:AAGO1hGoC9s5lzWK_kPYcV2VNCWJ1Xd9Q_A"

config = {
    'intents' : {
        'greetings' : {
            'examples' : ['привет', 'здравствуй', 'ку', 'здарова', 'добрый день','hi', 'hello', 'good day','салют', 'обращение', 'речь', 'поздравление', 'адрес', 'пожелание', 'благословение', 'напутствие', 'поклон', 'возглас', 'шалом', 'благопожелание', 'целование', 'зига', 'хайль', 'ахой', 'гамарджоба', 'здравица', 'взаимоприветствия', 'здорование', 'лобзание', 'теменна', 'туш', 'шоламалехем'],
            'response' : 'somefunk'
        },
        'farewll' : {
            'examples' : ['с наилучшими пожеланиями', 'всего хорошего', 'всего наилучшего', 'не поминай лихом', 'спасибо вашему дому, пойдем к другому', 'позвольте откланяться', 'всего доброго', 'спишемся', 'простите', 'до новых встреч', 'будь здоров', 'прости', 'увидимся', 'счастливо', 'до завтра', 'будьте здоровы', 'разрешите откланяться', 'будь', 'целую', 'до скорого', 'до скорой встречи', 'всего', 'успехов', 'встретимся', 'прощайте', 'созвонимся', 'в добрый час', 'удачи', 'всего лучшего', 'счастливо оставаться', 'честь имею кланяться', 'до вечера', 'звони', 'честь имею', 'до скорого свидания', 'разрешите попрощаться', 'до свиданья', 'целую ручки', 'до свидания', 
'пока', 'до связи', 'пересечемся', 'прощай', 'словимся', 'всех благ', 'не поминайте лихом', 'не болей', 'до созвона', 'адью', 'ауфидерзейн', 'бывай', 'маме привет', 'ата', 'свидимся', 'позвольте попрощаться', 'до встречи', 'чао', 'бай', 'бай-бай', 'покеда', 'ариведерче', 'сайонара', 'прощевайте', 'гуд-бай', 'прощевай', 'прости-прощай', 'покедова', 'гудбайте'],
            'response' : 'somefunk'
        },
        'positive' : {
            'examples' : ['хорошо', 'отлично', 'замечательно','умница', 'красавчик', 'молодчина', 'молодец', 'умник', 'красавелла', 'гений', 'браво', 'красавец', 'орел', 'красава', 'иес', 'люблю молодца за обычай', 'ухарь', 'боец', 'бодро', 'хвалю', 'ай да', 'добрый молодец', 'чертяка', 'казачина', 'молодчик', 'штык', 'иес!', 'честь и хвала', 'мощага', 'парень, что надо', 'чудо-молодец', 'чертом', 'масёл', 'молодчага', 'размолодец', 'молодец молодцом', 'молодчинища', 'молодцом', 'молодчинище', 'можно чести приписать', 'хороший', 'юноша', 'смельчак', 'храбрец', 'молоток', 'гвоздь', 'козырь', 'лихо', 'хват', 'удалец'],
            'response' : 'somefunc'
        },
        'hoareyou' : {
            'examples' : ['как дела','как ты', 'как поживаешь', 'как поживаете', 'как сам', 'как настроение', 'как делишки'],
            'response' : 'somefunc'
        }
    }
}

responses = {
    'intents' : {
        'greetings' : ['Привет!', 'Добрый день!', 'Здравствуй!'],
        'farewll' : ['Пока!', 'До скорой встречи!', 'До свидания!'],
        'positive' : ['Списибо за комплимент!', 'Очень приятное сообщение!)', 'Это положительное сообщение'],
        'hoareyou' : ['У меня все отлично! Спасибо!', 'Мои дела хорошо! Как ваши?', 'Все замечательно! Благодарю!']
    }
}
