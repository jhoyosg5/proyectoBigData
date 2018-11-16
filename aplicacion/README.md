# Analitica de sentimientos de Twitter  usando Apache Spark Streaming APIs y Python

En este proyecto, se busca cómo procesar flujos de datos en vivo usando las API de transmisión de Spark y Python. Se realizo un análisis de sentimiento básico de tweets en tiempo real. Además, también se obtuvo una introducción básica a Apache Kafka, que es un servicio de colas para flujos de datos.

## Requisitos
Uno de los primeros requisitos es tener acceso a los datos de transmisión; En este caso, tweets en tiempo real. Twitter proporciona una muy
API conveniente para obtener tweets de una manera streaming
 
Además, también usé Kafka para amortiguar los tweets antes de procesarlos. Kafka proporciona un servicio de colas distribuido que puede usarse para almacenar los datos cuando la tasa de creación de datos es más que la tasa de procesamiento. 

### Configuración del proyecto
 
#### Instalación de las librerias Python requeridas
el proyectp posee  un archivo de texto que contiene los paquetes de Python necesarios: `Requirements.txt`

Para instalar todos estos a la vez, simplemente ejecute (solo se instalarán los paquetes faltantes):
`$ sudo pip install -r Requirements.txt`
 
#### Instalación e inicialización de Kafka
Descargue y extraiga el último binario de https://kafka.apache.org/downloads.html

##### Iniciar el servicio zookeeper:
`$ bin / zookeeper-server-start.sh config / zookeeper.properties`
 
##### Iniciar el servicio kafka:
`$ bin / kafka-server-start.sh config / server.properties`
 
##### Cree un tema llamado twitterstream en kafka:
`$ bin / kafka-topics.sh --create --zookeeper --partitions 1 --topic twitterstream localhost: 2181 --replication-factor 1`

 
#### Usando la API de streaming de Twitter
Para descargar los tweets de la API de transmisión de twitter y enviarlos a la cola kafka, se ha creado un script de python
app.py. El script necesitará sus tokens (claves) de autenticación de Twitter.

Una vez que tenga sus tokens de autenticación, cree o actualice el `twitter-app-credentials.txt` con estas credenciales.

Después de actualizar el archivo de texto con sus claves de twitter, puede comenzar a descargar tweets de la API de Twitter y enviarlos a la aplicacion twitterstream en Kafka. Haga esto ejecutando el script de la siguiente manera:
`$ python app.py`
Nota: este programa debe mantenerse funcionando para recopilar tweets.
 
##### Para verificar si los datos están aterrizando en Kafka:
`$ bin / kafka-console-consumer.sh --zookeeper localhost: 2181 --time twitterstream --from-beginning`

##### Ejecutando el programa Stream Analysis:
`$ $ SPARK_HOME / bin / spark-submit --paquetes org.apache.spark: spark-streaming-kafka_2.10: 1.5.1 twitterStream.py`