import findspark
import sys

findspark.init('/home/ubuntu/spark-3.3.1-bin-hadoop3')
findspark.find()

import pyspark

from pyspark.sql import SparkSession


# The entry point into all functionality in Spark is the SparkSession class.
spark = (SparkSession
    .builder
    .appName("Part 2: A simple Spark application")
    .master('spark://172.31.33.143:7077')
    .config('spark-defaults.conf')
    .getOrCreate())


# You can read the data from a file into DataFrames
partitions = int(50)
df = spark.read.load("hdfs://172.31.33.143:9000/export.csv", format='csv', header='true', sep=',', inferSchema='true')

df = df.orderBy("cca2","timestamp")
df.show()
df.write.format("csv").mode("overwrite").save("hdfs://172.31.33.143:9000/"+sys.argv[2])
spark.stop()