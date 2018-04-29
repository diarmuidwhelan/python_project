


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


# DATASET SUMMARY
The Iris data set is a well known data set collected by Ronald Fisher in 1936. It contains data on characteristics of 3 different species of iris flowers. The dataset contains the petal length and width and sepal length and width for 50 of each iris species type, Iris-setosa, iris-versicolor and Iris-virginica. The dataset is often referred to as Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula. Fisher developed a linear discriminant model to distinguish the species from each other, using a combination of the four characteristics. 


# Initial Exploration
There are 5 columns and 150 rows in the dataset.
Columns 1,2,3 and 4 are numerical variables whilst column 5 is a categorical variable.
Column 1 is sepal length in cm,column 2 is  sepal width in cm, column 3 is petal length in cm, column 4 is petal width in cm and column 5 is species type.

The graphs of each column outputted by running dataset_initial_exploration.py are below.
We can see column 1 is quite normally distributed between 4.3cm and 7.9 cm. There looks to be a small skew to the left. Median and mean are quite close together, median is 5.8cm and mean is 5.8433cm. There appears to be 3 mini peaks in the data around 4.75, 5.5 and 6.25cm. 

![alt text](https://github.com/diarmuidwhelan/python_project/blob/master/Column_1.png "Column 1 Distribution")

Similarly, column 2 is quite normally distributed between 2cm and 4.4 cm. Again median and mean are quite close together, median is 3.0cm and mean is 3.054cm. 

![alt text](https://github.com/diarmuidwhelan/python_project/blob/master/Column_2.png "Column 2 Distribution")

Column 3 is somewhat different in it's distribution from columns 1 and 2. It's variance looks to be wider with data spanning the range between 1cm and 6.9cm. The graph illustrates this with 2 distinct peaks around 5cm and 1cm. There is a decent difference between mean and median of the column as a result.

![alt text](https://github.com/diarmuidwhelan/python_project/blob/master/Column_3.png "Column 3 Distribution")


In the same vein column 4 looks to be quite spread out between 0.1cm and 1.5cm. Mean is 1.198cm whilst median is 1.3cm.

![alt text](https://github.com/diarmuidwhelan/python_project/blob/master/Column_4.png "Column 4 Distribution")


The describe function produces a table with key characteristics of each column. These reinforce the above observations about the column distributions. The 3rd columns standard deviation is significantly greater than the other 3 columns, with the 2nd column exhibiting quite a narrow standard deviation.


|Measure    | Sepal Length| Sepal Width| Petal Length| Petal Width|
| ----------|:-----------:| ----------:|------------:|-----------:|
| count     |   150.0000  |  150.0000  | 150.0000    |  150.0000  |
| mean      |   5.843333  |  3.054000  | 3.758667    |  1.198667  |
 std       |   0.828066  |  0.433594  | 1.764420    |  0.763161  |
| min       |   4.300000  |  2.000000  | 1.000000    |  0.100000  |
| 25%       |   5.100000  |  2.800000  | 1.600000    |  0.300000  |
| 50%       |   5.800000  |  3.000000  | 4.350000    |  1.300000  |
| 75%       |   6.400000  |  3.300000  | 5.100000    |  1.800000  |
| max       |   7.900000  |  4.400000  | 6.900000    |  2.500000  |



![alt text](https://github.com/diarmuidwhelan/python_project/blob/master/boxplot_iris.png "Box and Whisker Plot for Columns 1-4")

# Predictive Modelling
Fisher used the 4 characteristics, sepal length and width and petal length and width, to build a model that could predict the iris species type from these. The model built was a linear model. In iris_model.py, I am going to attempt to use some of python's machine learning packages to develop a model to predict species type. 

First I plot the relationshsip between some of the features.K Means clustering can be used on the features to attempt to group the species together. Here I attempt to  build 3 groups - 1 for each species type. 

![alt text](https://github.com/diarmuidwhelan/python_project/blob/master/Sepal_features_relationship.png "Sepal Length & Width")


![alt text](https://github.com/diarmuidwhelan/python_project/blob/master/petal_feature_relationship.png "Petal Length & Width")


From the above plots, we can see how the features are related and how this differs by species type. In the petal length and width there looks to be a linear positive correlation between length and width and each species type looks to have distinct petal length and width ranges.


In iris_model.py, I fit a Support Vector Classification and K nearest neighbours models to the iris data.  K nearest neighbours is a method which uses the K datapoints closest to the target to predict it's class. Support Vector Machines are a suppervised learning method that attempt to construct a plane between the different classes. These models can be used to predict the species type of a flower with certain features. Probabilities for each outcome are also calculated. However, there is an issue of overfitting the data with these initially where I use the entire dataset to predict the outcome of the same datapoints. In a sense correcting my own homework. To overcome this issue I use some validation techniques to test the robustness of the models.

I attempt to validate and test the accuracy of these models by splitting the dataset into a training and test sample.The results appear to be quite positive. In the case of the K Nearest Neighbours model the number of neighbours chosen is arbitrary. We can optimise the number chosen by looping a few different options and picking the best result. It turns out 1,5 and 10 have the best accuracy with 20 and 30 progressively worse the higher the number of neighbours. 

Further improvements may be made by exploring the different kernel types in SVC and looking at other techniques such as decision trees and random forests.


# References
https://en.wikipedia.org/wiki/Iris_flower_data_set

http://archive.ics.uci.edu/ml/datasets/Iris

www.scipy-lectures.org/advanced/scikit-learn/

https://docs.python.org/3/tutorial/index.html

https://github.com/jakevdp/sklearn_pycon2015

http://nbviewer.jupyter.org/github/donnemartin/data-science-ipython-notebooks/blob/master/scikit-learn/scikit-learn-intro.ipynb

