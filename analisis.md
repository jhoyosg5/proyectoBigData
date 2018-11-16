# universidad EAFIT Topicos de telematica 2018-2

## proyecto 3 big data

### integrante
Jorge Andres Hoyos

## proyecto a realizar
cómo procesar flujos de datos en vivo usando las API de transmisión de Spark y Python, ademas realizar un análisis de sentimiento básico de tweets en tiempo real, usando un sistema de encolamiento de Kaftka

## Marco Teorico

### Datos streaming 
Los datos de transmisión(streaming) son datos que se generan continuamente por diferentes fuentes. Dichos datos deben procesarse de forma incremental utilizando técnicas de procesamiento de flujo sin tener acceso a todos los datos. Además, se debe considerar que la desviación del concepto puede ocurrir en los datos, lo que significa que las propiedades de la transmisión pueden cambiar con el tiempo.

Por lo general, se utiliza en el contexto de big data en el que es generado por muchas fuentes diferentes a alta velocidad. 

La transmisión de datos también se puede explicar como una tecnología utilizada para enviar contenido a dispositivos a través de Internet, y permite a los usuarios acceder al contenido de forma inmediata, en lugar de tener que esperar a que se descargue.  Big Data está obligando a muchas organizaciones a centrarse en los costos de almacenamiento, lo que atrae el interés de los lagos de datos y los flujos de datos.  Un lago de datos se refiere al almacenamiento de una gran cantidad de datos no estructurados y semi datos, y es útil debido al aumento de big data, ya que puede almacenarse de tal manera que las empresas pueden sumergirse en el lago de datos y extraer lo que necesitan. en el momento que lo necesiten.  Mientras que un flujo de datos puede realizar un análisis en tiempo real en la transmisión de datos, y difiere de los lagos de datos en la velocidad y la naturaleza continua del análisis, sin tener que almacenar los datos primero. 

### Apache Spark 
Apache Spark es un marco de computación en clúster de uso general distribuido de código abierto. Originalmente desarrollado en la Universidad de California, AMPLab de Berkeley, el código base de Spark fue luego donado a Apache Software Foundation, que lo ha mantenido desde entonces. Spark proporciona una interfaz para programar clústeres completos con paralelismo de datos implícito y tolerancia a fallas.

### Apache Kafka
 Es una plataforma de software de procesamiento de flujo de código abierto desarrollada por Apache Software Foundation, escrita en Scala y Java. El objetivo del proyecto es proporcionar una plataforma unificada, de alto rendimiento y baja latencia para el manejo de las fuentes de datos en tiempo real. Su capa de almacenamiento es esencialmente una "cola de mensajes de publicación / sub de gran escala escalable diseñada como un registro de transacciones distribuidas" , lo que la hace altamente valiosa para las infraestructuras empresariales para procesar datos de transmisión. Además, Kafka se conecta a sistemas externos (para importación / exportación de datos) a través de Kafka Connect y proporciona Kafka Streams, una biblioteca de procesamiento de secuencias de Java.