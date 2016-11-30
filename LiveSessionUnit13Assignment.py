# -*- coding: utf-8 -*-
"""
MSDS 6306
Live Session Unit 13 Assignment
Brian Yu

"""

## 1.Create a list named my_list in Python with the following data points
my_list = [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]

### 1a. Print the 5th element in the list
my_list[4]

### 1b. Append 5.2 to my_list
my_list.append(55.2)
print (my_list)

### 1c. Remove the 6th element in the list
del my_list[5]
print (my_list)

### 1d. Iterate over the list to print data points greater than 45
for val in my_list:
    if val > 45:
        print (val)

        
## 2. Introduction to Numpy

### 2a. Import the numpy library using the following command import numpy
import numpy as np

### 2b. Declare numpy array with the same data points as in my_list using numpy.array()
array = np.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])
print (array)

### 2c. Compute the mean and standard deviation using nump.mean() and numpy.std() of the above array
mean_array = np.mean(array)
print ("The mean of array is", mean_array)
std_array = np.std(array)
print ("The standard deviation of array is", std_array)

### 2d. Use logical referencing to get only those values that are less than 45
array[np.where(array < 45)]

### 2e. Compute the max and min of the array using numpy.max() and numpy.min()
max_array = np.max(array)
print ("The max of the array is", max_array)
min_array = np.min(array)
print ("The min of the array is", min_array)


## 2. Introduction to Pandas

### 3a. Import the pandas library - import pandas
import pandas as pd

### 3b. Read the IRIS dataset into iris using pandas.read_csv(). Data file -
iris = pd.read_csv("C:/Users/Brian/Anaconda3/Lib/site-packages/blaze/examples/data/iris.csv"
                   , index_col = False)

### 3c. Using iris.head(), display the head of the data set
iris.head()

### 13d. Use DataFrame.drop() to drop the id column
iris.drop(iris.columns[[0]], axis = 1)

### 13e. Subset dataframe to create a new data frame that includes only the measurements for the setosa species
df_setosa = iris[iris.species == "Iris-setosa"]
df_setosa

### 13f. Use DataFrame.describe() to get the summary statistics
iris.describe()
df_setosa.describe()

### 13g. Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()
df_species_group = iris.groupby(['species'])
df_species_group.describe()

### 13h. Use a DataFrame.boxplot() to plot boxplots by Species
### %matplotlib inline (for Juptier Notebook)

df_species_group.boxplot(return_type = 'both')

### 13i. Plot a scatter matrix plot using the seaborn library. Use the following to load and plot
#### i. Import seaborn
import seaborn as sns
sns.pairplot(iris, hue = 'species')

