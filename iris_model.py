###################################################################################################################
#GMIT Higher Diploma in Data Analytics
#Scripting and Programming
#Python Project
#Diarmuid Whelan, 2018-04-22
#Iris Dataset predictive model
#Will attempt to build a predictive model using machine learning techniques for the Iris Dataset
######################################################################################################################
import pandas
from sklearn import model_selection
import matplotlib.pyplot as plt
#Load Data
iris = pandas.read_csv('C:/Users/DELL PC/Documents/GMIT DATA ANALYTICS/Programming and Scripting/iris_data.csv')
#Need to split the data into a test and training set. Will split it 80% training and 20% test
array = iris.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

#FIT KNN
 
#FIT SVM (Support Vector Machine)
from sklearn  import svm 
svc = svm.SVC(kernel='linear') # Support Vector Classifier
svc.fit(X,Y)

#FIT K-MEANS
