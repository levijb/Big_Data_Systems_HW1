import re
import findspark
import sys
from operator import add
from typing import Iterable, Tuple

from pyspark.resultiterable import ResultIterable
from pyspark.sql import SparkSession

findspark.init('/home/ubuntu/spark-3.3.1-bin-hadoop3')
findspark.find()

"""Helper function to calculates URL contributions to the rank of other URLs"""
def calculateRankContrib(urls: ResultIterable[str], rank: float) -> Iterable[Tuple[str, float]]:
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


"""Helper function to parses a urls string into urls pair"""
def parseNeighborURLs(urls: str) -> Tuple[str, str]:
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]


if __name__ == "__main__":
	# A baseline implementation should take three command-line arguments except the python code
	# You can extend this by including however many arguments you want
    if len(sys.argv) != 4:
        print("Usage: pagerank <path_to_input> <path_to_output> <iterations>", file=sys.stderr)
        sys.exit(-1)

    # Initialize the Spark context
	# IP below is the private IPv4 address of your Spark master
    spark = SparkSession\
        .builder\
        .appName("PySpark PageRank program with partitions and worker killed halfway")\
        .master("spark://172.31.33.143:7077")\
        .getOrCreate()


    # Loads in input file
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     ...
    
    partitions = int(50)
    lines = spark.sparkContext.textFile("hdfs://172.31.33.143:9000/"+sys.argv[1], partitions)

    # Perform a transformation to define a links RDD by using parseNeighborURLs helper function
    links = lines.map(lambda urls: parseNeighborURLs(urls)).distinct().groupByKey()

    # Initialize a ranks RDD
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))
    # Split into partitions
    ranks = ranks.partitionBy(partitions)
    
    # Calculates and updates URL ranks continuously using PageRank algorithm.
    for iteration in range(int(sys.argv[3])):
        contribs = links.join(ranks).flatMap(lambda url_urls_rank: calculateRankContrib(
            url_urls_rank[1][0], url_urls_rank[1][1]  # type: ignore[arg-type]
        ))

        # Re-calculates URL ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

    # Collects all URL ranks and dump them to console.
    for (link, rank) in ranks.collect():
        print("%s has rank: %s." % (link, rank))



	# Dump output to HDFS
    ranksDf = ranks.toDF()
	# IP below is the private IPv4 address of your HDFS master
    ranksDf.write.format("csv").save("hdfs://172.31.33.143:9000/"+sys.argv[2])

	# You should always stop the Spark session when it's done
    spark.stop()
