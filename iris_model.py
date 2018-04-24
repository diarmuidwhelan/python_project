###################################################################################################################
#GMIT Higher Diploma in Data Analytics
#Scripting and Programming
#Python Project
#Diarmuid Whelan, 2018-04-22
#Iris Dataset predictive model
#Will attempt to build a predictive model using machine learning techniques for the Iris Dataset
######################################################################################################################
import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets
#Load Data USING THE SAVED DATASET IN SKLEARN PACKAGE.
#THIS IS EASIER TO USE AND READY MADE FOR SOME OF THE MACHINE LEARNING FUNCTIONS
iris = datasets.load_iris()
X, y = iris.data, iris.target

# create the KNN model
knn = neighbors.KNeighborsClassifier(n_neighbors=5) #LOOKS FOR THE 5 CLOSEST DATA POINTS

# fit the KNN model
knn.fit(X, y)


# Use the predict method to predict the species type of certain characteristics
# If we wanted to know what kind of iris has 2cm x 4cm sepal and 3cm x 3cm petal?
result = knn.predict([[2, 3, 3, 3],])
print(iris.target_names[result])
#can also predict the probability of certain features being each species type
prob = knn.predict_proba([[2, 3, 3, 3],])
print(prob)
