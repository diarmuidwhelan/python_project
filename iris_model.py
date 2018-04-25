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
from sklearn import neighbors, datasets,svm
#Load Data USING THE SAVED DATASET IN SKLEARN PACKAGE.
#THIS IS EASIER TO USE AND READY MADE FOR SOME OF THE MACHINE LEARNING FUNCTIONS
iris = datasets.load_iris()
X, y = iris.data, iris.target
#when predictive modelling it is important to understand how the features interact and imapct on each other
#Visualise the relationships between features
def sepal_data(): #define function to plot the relationship between sepal length and width
	iris = datasets.load_iris()
	X = iris.data[:, :2]  #Looks at the first two features -sepal length and width
	y = iris.target
	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
	plt.xlabel('Sepal length')#add labels
	plt.ylabel('Sepal width')#add labels
	plt.title('Sepal Width & Length')#add title
	plt.show()
 
sepal_data()


def petal_data():  #define function to plot the relationship between petal length and width
	iris = datasets.load_iris()
	X = iris.data[:, 2:]  #Looks at the first two features -petal length and width
	y = iris.target
	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
	plt.xlabel('Petal length') #add labels
	plt.ylabel('Petal width')  #add labels
	plt.title('Petal Width & Length') #add title
	plt.show()
 
petal_data()

# create the KNN model
knn = neighbors.KNeighborsClassifier(n_neighbors=5) #LOOKS FOR THE 5 CLOSEST DATA POINTS

# fit the KNN model
knn.fit(X, y)


# Use the predict method to predict the species type of certain characteristics
# If we wanted to know what kind of iris has 2cm x 4cm sepal and 3cm x 3cm petal?
knn_result = knn.predict([[2, 3, 3, 3],])
print(iris.target_names[knn_result])
#can also predict the probability of certain features being each species type
knn_prob = knn.predict_proba([[2, 3, 3, 3],])
print(knn_prob)

#measure an iris plant's sepal length and width and petal lengtha and width and input them when prompted
sepal_length=input("Please enter sepal length in cm:") #Enter a sepal length that you would like to predict
sepal_width=input("Please enter sepal width in cm:") #Enter a sepal width that you would like to predict
petal_legth=input("Please enter petal length in cm:") #Enter a petal length that you would like to predict
petal_width=input("Please enter petal width in cm:") #Enter a petal width that you would like to predict

knn_test = knn.predict([[sepal_length, sepal_width, petal_legth, petal_width],])
print(iris.target_names[knn_test])
#can also predict the probability of certain a flower with the above features being each species type
knn_test_prob = knn.predict_proba([[sepal_length, sepal_width, petal_legth, petal_width],])
print(knn_test_prob)


#FIT SVM (Support Vector Machine)
# create the SVC (SUPPORT VECTOR CLASSIFIER) model
svc = svm.SVC(kernel='linear') #LOOKS FOR THE 5 CLOSEST DATA POINTS

# fit the SVC model
svc.fit(X, y)


# Use the predict method to predict the species type of certain characteristics
# If we wanted to know what kind of iris has 2cm x 4cm sepal and 3cm x 3cm petal?
svc_result = svc.predict([[2, 3, 3, 3],])
print(iris.target_names[svc_result])

#FIT K-MEANS
