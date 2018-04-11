###################################################################################################################
#GMIT Higher Diploma in Data Analytics
#Scripting and Programming
#Python Project
#Diarmuid Whelan, 2018-04-10
#Iris Dataset initial exploration
#Will provide summary stats and plots for the Iris Dataset
######################################################################################################################

import numpy
import matplotlib.pyplot as pl
#Open the IRIS.CSV FILE
iris=numpy.genfromtxt('C:/Users/DELL PC/Documents/GMIT DATA ANALYTICS/Programming and Scripting/iris.csv',delimiter=',')
print(iris)

#Print the shape of the data
print(iris.data.shape)
#Iris data has 150 rows and 5 columns

#Print mean of First 4 columns

for i in range (0,4):
    column =iris[:,i]
    meancolumn=numpy.mean(column)
    print("Mean of column ", i+1," is:",meancolumn)
#Plot each columns data
    pl.hist(column)
    pl.show()
