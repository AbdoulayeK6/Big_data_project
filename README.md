# Big_data_project

#  Description
This project contains two mini-projects based on Apache Spark and Hadoop. The objective is to explore big data processing using these technologies and compare their performance on a word count task using a large text file, shakespeare.txt

# Prerequisites
Before running these projects, makwe have to install :
Apache Spark
Hadoop
Python 3

# Project Structure
/
|-- Apache_Spark/
|   |-- spark_project.ipynb  
|
|-- Hadoop/
|   |-- map.py   
|   |-- reduce.py  
|   |-- hadoop_project.ipynb  
|
|-- README.md  

you can see all these steps in the differents notebook submitted

# Apache Spark
The Spark project includes the following steps:
Loading and preprocessing data
Transforming and analyzing data with Spark
Running the Word Count on shakespeare.txt
Visualizing results

# Hadoop
The Hadoop project follows these steps:
Installing and configuring Hadoop
Defining the mapper script (map.py)
Defining the reducer script (reduce.py)
Running the Hadoop Streaming job on shakespeare.txt
Visualizing results with Spark

# Performance Analysis
The main goal of this project is to evaluate the performance differences between Apache Spark and Hadoop on a classic big data task: word count. We use the shakespeare.txt file, a large text containing the complete works of Shakespeare, to measure the speed and efficiency of both technologies.

With Hadoop, we used a Hadoop Streaming job with a map.py script to map words and a reduce.py script to aggregate and count them. Running on a cluster allows parallel processing but involves costly I/O operations.

With Apache Spark, we leveraged its in-memory processing engine to accelerate the Word Count. Spark uses the RDD API to distribute and parallelize computations while minimizing intermediate disk writes, thereby reducing execution time.

This comparison highlights Spark's advantages in terms of speed and efficiency over Hadoop, especially for interactive and iterative processing of massive data volumes.

#Author
Ismael Koulibaly
