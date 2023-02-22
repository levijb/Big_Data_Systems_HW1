# Big_Data_Systems_HW1
# Part 3: PageRank, Task 2

For this task we use the same PySpark PageRank implementaion in task 1 (see README_Part3_Task1) but add partitions to parallelize the operations to achieve better runtime.
- In order to achieve high parallelism, Spark will split the data into smaller chunks called partitions, which are distributed across different nodes in the cluster. Partitions can be changed in several ways. For example, any shuffle operation on an RDD (e.g., join()) will result in a change in partitions (customizable via user’s configuration). In addition, one can also decide how to partition data when creating/configuring RDDs (hint: e.g., you can use the function partitionBy()).


