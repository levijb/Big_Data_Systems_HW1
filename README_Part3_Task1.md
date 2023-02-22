# Big_Data_Systems_HW1

# Part 3: PageRank, Task 1

For this task we implement the PageRank algorithm with pyspark
Overview of the PageRank algorithm:
- Set initial rank of each page to be 1.
- On each iteration, each page p contributes to its outgoing neighbors a value of rank(p)/(# of outgoing neighbors of p).
- Update each page’s rank to be 0.15 + 0.85 * (sum of contributions).
- Go to next iteration.

We are using the Berkeley-Stanford web graph dataset. 
- Put the input file into Ubuntu and copy the file to the Hadoop/Spark server. ex: hdfs dfs -copyFromLocal export.csv /
- Use spark-submit to run. ex: bin/spark-submit /home/ubuntu/HW1_task.py 'web-BerkStan.csv' 'hw1_pt3_task3.csv' (run file, .py file location, input .csv, output .csv)
- View the output file (and input file) on the Hadoop dashboard.
