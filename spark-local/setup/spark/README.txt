In caso di errore "The system cannot find the path specified" nell'esecuzione degli scripts eg spark-submit, ci sono le possibili soluzioni:
1: set JAVA_HOME
2. set SPARK_HOME e suo bin nel PATH
3. Se pyhton è stato installato esternamente da WindowsApp (microsoft store) bisogna rimuovere l'app execution alias
4. Set dell'executable python in PYSPARK_PYTHON e PYSPARK_DRIVER_PYTHON
5. Add winutils.exe e hadoop.dll File -> https://phoenixnap.com/kb/install-spark-on-windows-10 ed in c://Windows/System32