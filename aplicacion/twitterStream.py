from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import operator
import numpy as np
import matplotlib.pyplot as plt


def main():
    conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
    sc = SparkContext(conf=conf)

    # Crea un contenido de stream con lotes de intervalos de 10 segundos
    ssc = StreamingContext(sc, 10)
    ssc.checkpoint("checkpoint")
    pwords = load_wordlist("./Dataset/positive.txt")
    nwords = load_wordlist("./Dataset/negative.txt")
    counts = stream(ssc, pwords, nwords, 100)
    make_plot(counts)


def make_plot(counts):
    """
    Esta funcion cuenta la cantidad de palabras positivas y negativas por cada paso de tiempo
    """
    positiveCounts = []
    negativeCounts = []
    time = []

    for val in counts:
	positiveTuple = val[0]
	positiveCounts.append(positiveTuple[1])
	negativeTuple = val[1]
	negativeCounts.append(negativeTuple[1])

    for i in range(len(counts)):
	time.append(i)

    posLine = plt.plot(time, positiveCounts,'bo-', label='Positive')
    negLine = plt.plot(time, negativeCounts,'go-', label='Negative')
    plt.axis([0, len(counts), 0, max(max(positiveCounts), max(negativeCounts))+50])
    plt.xlabel('Time step')
    plt.ylabel('Word count')
    plt.legend(loc = 'upper left')
    plt.show()

	
def load_wordlist(filename):
    """ 
    Esta funcion devuelve la lista o set de palabras dadoun nombre de archivo.
    """	
    words = {}
    f = open(filename, 'rU')
    text = f.read()
    text = text.split('\n')
    for line in text:
        words[line] = 1
    f.close()
    return words


def wordSentiment(word,pwords,nwords):
    if word in pwords:
	return ('positive', 1)
    elif word in nwords:
	return ('negative', 1)


def updateFunction(newValues, runningCount):
    if runningCount is None:
       runningCount = 0
    return sum(newValues, runningCount) 


def sendRecord(record):
    connection = createNewConnection()
    connection.send(record)
    connection.close()


def stream(ssc, pwords, nwords, duration):
    kstream = KafkaUtils.createDirectStream(
    ssc, topics = ['twitterstream'], kafkaParams = {"metadata.broker.list": 'localhost:9092'})
    tweets = kstream.map(lambda x: x[1].encode("ascii", "ignore"))

    # Cada elemento  del tweet hara parate del texto de un tweet
    # Se hace ratreo de la cuenta total y se imprime cada paso de tiempo.
    words = tweets.flatMap(lambda line:line.split(" "))
    positive = words.map(lambda word: ('Positive', 1) if word in pwords else ('Positive', 0))
    negative = words.map(lambda word: ('Negative', 1) if word in nwords else ('Negative', 0))
    allSentiments = positive.union(negative)
    sentimentCounts = allSentiments.reduceByKey(lambda x,y: x+y)
    runningSentimentCounts = sentimentCounts.updateStateByKey(updateFunction)
    runningSentimentCounts.pprint()
    
    # La variable count guarda el numero de palabras para todos los pasos de tiempo
    counts = []
    sentimentCounts.foreachRDD(lambda t, rdd: counts.append(rdd.collect()))
    
    # Inicia la computacion
    ssc.start() 
    ssc.awaitTerminationOrTimeout(duration)
    ssc.stop(stopGraceFully = True)

    return counts


if __name__=="__main__":
    main()
