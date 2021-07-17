# *** Machine Learning *** 
#. How to run Linear regression in Python scikit-Learn

** Scikit-learn is a powerful Python module for machine learning. It contains function for regression, classification, clustering, model selection and dimensionality reduction.

## Exploring Boston Housing Data Set
The first step is to import the required Python libraries into Ipython Notebook.

-----------------
%matplotlib inline

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
-----------------


## I will access it using scikitlearn. I am going to import Boston data set into Ipython notebook and store it in a variable called boston.

-----------------
from sklearn.datasets import load_boston
bost = load_boston()
-----------------



the object BOSTON is a dictionary, so you can explore the keys of this dictionary.
-----------------
boston.keys()
['data', 'feature_names', 'DESCR', 'target']

boston.data.shape
(506, 13)
-----------------

print the feature nanes of BOSTON data set

-----------------

print boston.feature_names

-----------------

in this next section, it will take the 503 instances (rows) and 13 attributes or parameters(columns), with the goal of predicting the housing prices in boston region useing the data.

-----------------
print boston.DESCR
-----------------


Coverting boston.data into a pandas data frame

-----------------
bos = pd.dataframe(boston.data)
bos.head()
-----------------

With the example above it would return just numbers in the column names, this next code block would change that to feature names

-----------------
bos.columns =boston.feature_names
bos.head()
-----------------

boston.target contains the housing prices

-----------------
boston.target[5]
array([ 24., 21.6, 34.7, 33.4, 36.2,])
-----------------

next is to add these target prices to the bos data frame.

-----------------
bos['PRICE'] = boston.target
-----------------


# Scikit Learn

In this section I am going to fit a linear regression model and predict the Boston housing prices. I will use the least squares method as the way to estimate the coefficients.

Y = boston housing price(also called “target” data in Python)

and

X = all the other features (or independent variables)

First, I am going to import linear regression from sci-kit learn module. Then I am going to drop the price column as I want only the parameters as my X values. I am going to store linear regression object in a variable called lm.


-----------------
from sklearn.linear_model import LinearRegression
X = bos.drop('PRICE', axis=1)

#### This creates a LinearRegression object
lm = LinearRegression()
lm
-----------------

If you want to look inside the linear regression object, you can do so by typing LinearRegression. and the press <tab> key. This will give a list of functions available inside linear regression object.

Important functions to keep in mind while fitting a linear regression model are:

lm.fit() -> fits a linear model

lm.predict() -> Predict Y using the linear model with estimated coefficients

lm.score() -> Returns the coefficient of determination (R^2). A measure of how well observed outcomes are replicated by the model, as the proportion of total variation of outcomes explained by the model.

You can also explore the functions inside lm object by pressing lm.<tab>

.coef_ gives the coefficients and .intercept_ gives the estimated intercepts.



## Fitting a Linear Model
I am going to use all 13 parameters to fit a linear regression model. Two other parameters that you can pass to linear regression object are fit_intercept and normalize.

In [20]: lm.fit(X, bos.PRICE)

Out[20]: LinearRegression(copy_X=True, fit_intercept=True, normalize=False)

I am going to print the intercept and number of coefficients.


-----------------
print 'estimated intercept coefficient:', lm.intercept_
estimated intercept coefficient: 36.491132805
-----------------

-----------------
print 'Number of coefficients:' , len(lm.conf_)
Number of coefficients: 13
-----------------

Than construct a data frame that contains features and estimated coefficients

-----------------
pd.DataFrame(zip(x.columns, lm.coef_), columns = ['features', 'estimatedcoefficients'])
-----------------

That would return a table but it has a high correlation between RM and prices. So next we will do a scatter plat between true housing prices and true RM

-----------------
plt.scatter(bos.RM, box.PRICE)
plt.xlabel("average number of rooms per dwelling(RM)")
plt.ylabel("housing Price")
plt.title("Relationship between RM and Price")
plt.show()
-----------------

Returns a scatter plot graph


Predicting Prices
I am going to calculate the predicted prices (Y^i) using lm.predict. Then I display the first 5 housing prices. These are my predicted housing prices.

-----------------
in: lm.predict(x)[0:5]
out: array([ 30.008, 25.029, 30.570, 28.608, 27.942])
-----------------

then you plot a scatter plot to compare true prices and the predicted prices.

-----------------
plt.scatter(bos.price, lm.predict(X))
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted Prices: $\hat{y}_i$")
plt.title("Prices vs predicted Prices: $Y_i$ vs $\hat{Y}_i$")
-----------------

There is some errors in the prediction as the housing prices increase That is normal

Now to calculate the mean squared error.
-----------------
mseFull = np.mean((bos.PRICE - lm.predict(x)) ** 2)
print mseFull
-----------------

but if you fit linear regression for one feature the error will be very high. lets take the feature 'PTRATIO' and calculate the mean squared error.

-----------------
lm = LinearRegression()
lm.fit(X[['PTRATIO']], bos.PRICE)

LinearRegression(xopy_x=True, fit_intercept=True, normalize = False)
-----------------
-----------------
msePTration = np.mean((bos.PRICE - lm.predict(X[['PTRATIO']])) ** 2)
print msePTRATIO

62.652
-----------------


Training and validation data sets
In practice you wont implement linear regression on the entire data set, you will have to split the data sets into training and test data sets. So that you train your model on training data and see how well it performed on test data.

You can create training and test data sets manually, but this is not the right way to do, because you may be training your model on less expensive houses and testing on expensive houses.

how NOT TO DO TRAIN-TEST SPLIT: 
-----------------
x_train = x[:-50]
x_test = x[-50]
y_train = bos.PRICE[:-50]
y_test = bos.PRICE[:-50]
print x_train.shape
print x_test.shape
print y_train.shape
print y_test.shape
-----------------
-----------------
Output of above code:
(456, 13)
(50, 13)
(456,)
(50,)
-----------------

X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(x, bos.PRICE, test_size=0.33, random_state=5)
print x_train.shape
print x_test.shape
print y_train.shape
print y_test.shape

OUTPUT - 
(339, 13)
(167, 13)
(339,)
(167,)
-----------------


How to do train-test split:
You have to divide your data sets randomly. Scikit learn provides a function called train_test_split to do this.

building a linear regression model using my train-test data sets.
-----------------
lm = LinearRegression()
lm.fit(s_train, y_train)
pred_train = lm.predict(x_train)
pred_test = lm.predict(x_test)
-----------------

Input:
print “Fit a model X_train, and calculate MSE with Y_train:”, np.mean((Y_train – lm.predict(X_train)) ** 2)

print “Fit a model X_train, and calculate MSE with X_test, Y_test:”, np.mean((Y_test – lm.predict(X_test)) ** 2)

Output:
Fit a model X_train, and calculate MSE with Y_train: 19.5467584735 Fit a model X_train, and calculate MSE with X_test, Y_test: 28.5413672756

Residual Plots
Residual plots are a good way to visualize the errors in your data. If you have done a good job then your data should be randomly scattered around line zero. If you see structure in your data, that means your model is not capturing some thing. Maye be there is a interaction between 2 variables that you are not considering, or may be you are measuring time dependent data. If you get some structure in your data, you should go back to your model and check whether you are doing a good job with your parameters.

