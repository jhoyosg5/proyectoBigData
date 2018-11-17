# universidad EAFIT Topicos de telematica 2018-2

## proyecto 3 big data

### integrante
Jorge Andres Hoyos

## Problema a resolver
En este proyecto, busca cómo procesar flujos de datos en vivo usando las API de transmisión de Spark y Python. Se realizo un análisis de sentimiento básico de tweets en tiempo real. Además, también se obtuvo una introducción básica a Apache Kafka, que es un servicio de colas para flujos de datos.

Para facilidad de el proyecto se usaran tweets en ingles, debido a la mayor cantidad de flujo bajo este idioma, ademas se usaran filtros para la clasificacion de los tweets con palabras como lo son 'love' 'hate', para poder definir los tweets como positivos o negativos.

## Arquitectura preliminar de datos

![alt text](https://github.com/jhoyosg5/proyectoBigData/blob/master/Untitled%20Diagram.jpg)



## Fuente y naturaleza de los datos
Los datos provendran de la red social www.twitter.com del feed de una cuenta cuya credenciales deben ser dadas a la aplicacion, estos datos seran en tiempo real via Streaming los cuales sera extraidos usando  Tweepy, la cual accede y extrae los tweets a traves de la API, estos tweets tienen un formato no estructurado.


## Sistema de ingesta de datos
La ingesta de datos sera a traves de Apache Kaftka, la cual usa mensajeria de publicacion-suscripcion y ofrece un servicio distribuido y replicado.
Se usara Tweepy, para acceder a la API de twitter, y poder extraer los tweets.

## Almacenamiento de los datos
Para el almacenamiento de datos se tiene pensado usar HDFS para guardar la informacion generada a traves de spark streaming como Data Nodes (todavia no se ha implementado)

## Analisis de los datos 
Luego de que Spark Streaming recibe los datos por parte de kaftka, estos son procesados con el Spark Engine, para luego determinar los tweets en dos categorias
 * Positivos
 * negativos


## Marco Teorico

### Datos streaming 
Los datos de transmisión(streaming) son datos que se generan continuamente por diferentes fuentes. Dichos datos deben procesarse de forma incremental utilizando técnicas de procesamiento de flujo sin tener acceso a todos los datos. Además, se debe considerar que la desviación del concepto puede ocurrir en los datos, lo que significa que las propiedades de la transmisión pueden cambiar con el tiempo.

Por lo general, se utiliza en el contexto de big data en el que es generado por muchas fuentes diferentes a alta velocidad. 

La transmisión de datos también se puede explicar como una tecnología utilizada para enviar contenido a dispositivos a través de Internet, y permite a los usuarios acceder al contenido de forma inmediata, en lugar de tener que esperar a que se descargue.  Big Data está obligando a muchas organizaciones a centrarse en los costos de almacenamiento, lo que atrae el interés de los lagos de datos y los flujos de datos.  Un lago de datos se refiere al almacenamiento de una gran cantidad de datos no estructurados y semi datos, y es útil debido al aumento de big data, ya que puede almacenarse de tal manera que las empresas pueden sumergirse en el lago de datos y extraer lo que necesitan. en el momento que lo necesiten.  Mientras que un flujo de datos puede realizar un análisis en tiempo real en la transmisión de datos, y difiere de los lagos de datos en la velocidad y la naturaleza continua del análisis, sin tener que almacenar los datos primero. 

### Apache Spark 
Apache Spark es un marco de computación en clúster de uso general distribuido de código abierto. Originalmente desarrollado en la Universidad de California, AMPLab de Berkeley, el código base de Spark fue luego donado a Apache Software Foundation, que lo ha mantenido desde entonces. Spark proporciona una interfaz para programar clústeres completos con paralelismo de datos implícito y tolerancia a fallas.

### Spark Streaming 
Spark Streaming utiliza la capacidad de programación rápida de Spark Core para realizar análisis de transmisión. Ingiere datos en mini lotes y realiza transformaciones RDD en esos mini lotes de datos. Este diseño permite utilizar el mismo conjunto de código de aplicación escrito para el análisis por lotes en el análisis de transmisión, lo que facilita la implementación fácil de la arquitectura lambda.  Sin embargo, esta conveniencia viene con la penalización de latencia igual a la duración de mini lotes. Otros motores de transmisión de datos que procesan evento por evento en lugar de en mini lotes incluyen Storm y el componente de transmisión de Flink. Spark Streaming tiene soporte incorporado para consumir desde sockets de Kafka, Flume, Twitter, ZeroMQ, Kinesis y TCP / IP.

### HDFS 
El HDFS es un sistema de archivos distribuido, escalable y portátil escrito en Java para el marco de Hadoop. Algunos consideran que es un almacén de datos debido a su falta de compatibilidad con POSIX,  pero proporciona comandos de shell y métodos de interfaz de programación de aplicaciones Java (API) que son similares a otros sistemas de archivos.  Hadoop se divide en dos HDFS y MapReduce. HDFS se utiliza para almacenar los datos y MapReduce se utiliza para el procesamiento de los datos.

### Apache Kafka
 Es una plataforma de software de procesamiento de flujo de código abierto desarrollada por Apache Software Foundation, escrita en Scala y Java. El objetivo del proyecto es proporcionar una plataforma unificada, de alto rendimiento y baja latencia para el manejo de las fuentes de datos en tiempo real. Su capa de almacenamiento es esencialmente una "cola de mensajes de publicación / sub de gran escala escalable diseñada como un registro de transacciones distribuidas" , lo que la hace altamente valiosa para las infraestructuras empresariales para procesar datos de transmisión. Además, Kafka se conecta a sistemas externos (para importación / exportación de datos) a través de Kafka Connect y proporciona Kafka Streams, una biblioteca de procesamiento de secuencias de Java.