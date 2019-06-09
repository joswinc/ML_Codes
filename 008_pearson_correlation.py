# Pairwise Pearson correlations
from pandas import read_csv
from pandas import set_option
filename = "pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
set_option('precision', 3)
correlations = data.corr(method='pearson')
print(correlations)


# https://www.spss-tutorials.com/pearson-correlation-coefficient/

#Correlation Coefficient - Basics
#Correlations are never lower than -1. 
# A correlation of -1 indicates that the data points in a scatter plot 
# lie exactly on a straight descending line; the two variables are 
#perfectly negatively linearly related.

# A correlation of 0 means that two variables don't have any linear relation 
#whatsoever. However, some non linear relation may exist between the two variables.

# Correlation coefficients are never higher than 1. 
# A correlation coefficient of 1 means that two variables 
# are perfectly positively linearly related; 
# the dots in a scatter plot lie exactly on a straight ascending line