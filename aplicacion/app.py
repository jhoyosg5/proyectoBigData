import json
from kafka import SimpleProducer, KafkaClient
import tweepy
import configparser

# Nota: Algunas de las importaciones son bibliotecas externas de Python. Son instaladas en la máquina actual.
# Si está ejecutando un clúster multinodo, debe asegurarse de que estas bibliotecas
#y la versión  actual de Python está instalada en todos los nodos de trabajo.

class TweeterStreamListener(tweepy.StreamListener):
    """ Esta clase lee los twitter en tiempo real y los manda a kaftka"""

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        client = KafkaClient("localhost:9092")
        self.producer = SimpleProducer(client, async = True,
                          batch_send_every_n = 1000,
                          batch_send_every_t = 10)

    def on_status(self, status):
        """ Este metodo es llamado cuando nueva data llega del stream en vivo
        Se manda asincronicamente la data a las colas de kaftka"""
        msg =  status.text.encode('utf-8')
        try:
            self.producer.send_messages(b'twitterstream', msg)
        except Exception as e:
            print(e)
            return False
        return True

    def on_error(self, status_code):
        print("Error received in kafka producer")
        return True # No matar el flujo de datos

    def on_timeout(self):
        return True # No matar el flujo de datos

if __name__ == '__main__':

    # Lee las credenciales del archivo 'twitter-app-credentials.txt' 
    config = configparser.ConfigParser()
    config.read('twitter-app-credentials.txt')
    consumer_key = config['DEFAULT']['consumerKey']
    consumer_secret = config['DEFAULT']['consumerSecret']
    access_key = config['DEFAULT']['accessToken']
    access_secret = config['DEFAULT']['accessTokenSecret']

    # Crea el objeto de autorizacion
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Crea el flujo de datos y lo enlaza al listener
    stream = tweepy.Stream(auth, listener = TweeterStreamListener(api))

    #Reglas de filtro, todos los tweets pasan por este filtro en tiempo real
    #stream.filter(track = ['love', 'hate'], languages = ['en'])
    stream.filter(locations=[-180,-90,180,90], languages = ['en'])
