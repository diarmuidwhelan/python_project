# python_project
Python Project for Scripting and Programming Module
Due April 29th

The project entails researching the Iris data set, and then writing documentation and code in the Python programming language based on that research. 
  1. Research background information about the data set and write a summary about it.
  2. Keep a list of references used in completing the project.
  3. Download the data set and write some Python code to investigate it. 
  4. Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set.
  5. Write a summary of your investigations. 
  6. Include supporting tables and graphics as you deem necessary.


#DATASET SUMMARY
The Iris data set is a well known data set collected by Ronald Fisher in 1936. It contains data on characteristics of 3 different species of iris flowers.




#Initial Exploration
There are 5 columns and 150 rows in the dataset.
Columns 1,2,3 and 4 are numerical variables whilst column 5 is a categorical variable.
Column 1 is sepal length in cm,column 2 is  sepal width in cm , column 3 is petal length in cm, column 4 is petal width in cm and column 5 is species type.
The graphs of each column outputted by running dataset_initial_exploration.py are below.
We can see column 1 is quite normally distributed between 4.3cm and 7.9 cm. There looks to be a small skew to the left. Median and mean are quite close together, median is 5.8cm and mean is 5.8433cm. There appear to be 3 mini peaks in the data around 4.75, 5.5 and 6.25. 

Similarly, column 2 is quite normally distributed between 2cm and 4.4 cm. Again median and mean are quite close together, median is 3.0cm and mean is 3.054cm. There appear to be 3 mini peaks in the data around 4.75, 5.5 and 6.25. 

Column 3 is somewhat different in it's distribution from columns 1 and 2. It's variance looks to be wider with data spanning the range between 1cm and 6.9cm. The graph illustrates this with 2 distinct peaks around 5cm and 1cm. There is a decent difference between mean and median of the column as a result.
In the same vein column 4 looks to be quite spread out between 0.1cm and 1.5cm. Mean is 1.198cm whilst median is 1.3cm.




References
https://en.wikipedia.org/wiki/Iris_flower_data_set
http://archive.ics.uci.edu/ml/datasets/Iris
