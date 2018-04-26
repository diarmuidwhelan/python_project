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
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
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
	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)#Colour code based on species type
	plt.xlabel('Sepal length')#add labels
	plt.ylabel('Sepal width')#add labels
	plt.title('Sepal Width & Length')#add title
	plt.show()
 
sepal_data()


def petal_data():  #define function to plot the relationship between petal length and width
	iris = datasets.load_iris()
	X = iris.data[:, 2:]  #Looks at the first two features -petal length and width
	y = iris.target
	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm) #Colour code based on species type
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
svc = svm.SVC(kernel='linear') #

# fit the SVC model
svc.fit(X, y)


# Use the predict method to predict the species type of certain characteristics
# If we wanted to know what kind of iris has 2cm x 4cm sepal and 3cm x 3cm petal?
svc_result = svc.predict([[2, 3, 3, 3],])
print(iris.target_names[svc_result])
#can also predict the probability of certain features being each species type
#svc_prob = svc.predict_proba([[2, 3, 3, 3],])
#print(svc_prob)
#FIT K-MEANS
km_sepal = KMeans(3)  #TRY TO CREATE 3 CLUSTERS
km_sepal.fit(X)
y_km_sepal = km_sepal.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_km_sepal, s=50, cmap='rainbow');
plt.show()
#print(km.labels_)

km_petal = KMeans(3)  #TRY TO CREATE 3 CLUSTERS
km_petal.fit(X)
y_kmeans_petal = km_petal.predict(X)
plt.scatter(X[:, 2], X[:, 3], c=y_kmeans_petal, s=50, cmap='rainbow');
plt.show()
#print(km_petal.labels_)


#To test the predictive power and accuracy of our knn model we can do the following
y_pred_knn =knn.predict(X)
print("{0} / {1} correct".format(np.sum(y == y_pred_knn), len(y)))
y_pred_svc =svc.predict(X)
print("{0} / {1} correct".format(np.sum(y == y_pred_svc), len(y)))
#Clearly these are very accurate but this is an example of overfitting where we use an entire sanple to predict itself
#Need to split the sample into test and training sets to get a better gauge on teh predictive power of the model out of sample

dataset = pandas.read_csv('C:/Users/DELL PC/Documents/GMIT DATA ANALYTICS/Programming and Scripting/iris_data.csv')
#Will split it 80% training and 20% test
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

#lets train with 80% of data and test the above models out of sample on remaining 20%
knn.fit(X_train, Y_train)
y_pred_knn = knn.predict(X_validation)
print("{0} / {1} correct".format(np.sum(Y_validation == y_pred_knn), len(Y_validation)))

#CALCULATE ACCURACY SCORE
print(accuracy_score(Y_validation, y_pred_knn))

#can folllow same procedure for svc
svc.fit(X_train, Y_train)
y_pred_svc = svc.predict(X_validation)
print("{0} / {1} correct".format(np.sum(Y_validation == y_pred_svc), len(Y_validation)))

#CALCULATE ACCURACY SCORE
print(accuracy_score(Y_validation, y_pred_svc))
