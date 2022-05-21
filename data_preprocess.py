import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = stopwords.words('russian')

def data_preprocessing(news):
  news = re.sub(re.compile(r'"@:;,<.*?>'), '', news)
  news  = re.sub('[^А-Яа-я0-9ё]+', ' ', news)
  news  = news.lower()
  tokens = word_tokenize(news)
  news = [WordNetLemmatizer().lemmatize(word) for word in tokens]
  
  return news
