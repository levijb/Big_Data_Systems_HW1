# Big_Data_Systems_HW1

# Part 2: A simple Spark application
- For this step we create a a sample spark application that reads in a .csv file into a dataframe, sorts it by country code and timestamp, and then returns the new DF as a .csv. 
- Input file:
- - Put the input file into Ubuntu.
- - copy the file to the Hadoop/Spark instance. ex: hdfs dfs -copyFromLocal export.csv /
- Running the program:
- - Use spark-submit to run. bin/spark-submit -v /home/ubuntu/HW1_pt2.py 'export.csv' 'hw1_pt2.csv'  (run file, .py file location, input .csv, output .csv)
- View the output file (and input file) on the Hadoop dashboard.
