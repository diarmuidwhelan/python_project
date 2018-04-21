###################################################################################################################
#GMIT Higher Diploma in Data Analytics
#Scripting and Programming
#Python Project
#Diarmuid Whelan, 2018-04-10
#Iris Dataset initial exploration
#Will provide summary stats and plots for the Iris Dataset
######################################################################################################################
import pandas
import numpy
import matplotlib.pyplot as pl
#Open the IRIS.CSV FILE
iris=numpy.genfromtxt('C:/Users/DELL PC/Documents/GMIT DATA ANALYTICS/Programming and Scripting/iris.csv',delimiter=',')
print(iris)

#Print the shape of the data
print(iris.data.shape)
#Iris data has 150 rows and 5 columns

#loop through each of first four columns using for loop
#Print mean,max,min and median of first 4 columns

for i in range (0,4):
    column =iris[:,i]
    meancolumn=numpy.mean(column)
    print("Mean of column ", i+1," is:",meancolumn)
    mediancolumn=numpy.median(column)
    print("Median of column ", i+1," is:",mediancolumn)
    maxcolumn=numpy.max(column)
    print("Max of column ", i+1," is:",maxcolumn)
    mincolumn=numpy.min(column)
    print("Min of column ", i+1," is:",mincolumn)
#Plot each columns data
    pl.hist(column)
    pl.show()


#Use pandas to capture the categorical variables in column 5 and solve issues of the NANs 
#Iris_data.csv includes column headers   
dataset = pandas.read_csv('C:/Users/DELL PC/Documents/GMIT DATA ANALYTICS/Programming and Scripting/iris_data.csv')
print(dataset)
#Dataset formatted neater and includes the categorical variables
#Number of each species in each sample
print(dataset.groupby('species').size())
#Print a statistical summary about the dataset
print(dataset.describe()) 
#Means are same as calculated above. Describe function also provides percentile and standard deviation information to summarise the distribution of the data
# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pl.show()
