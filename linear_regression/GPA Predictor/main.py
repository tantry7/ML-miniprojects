import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
import statsmodels.api as sm

data = pd.read_csv('1.01. Simple linear regression.csv')
#reading the csv file and storing it into a dataframe
y = data['GPA']
x1 = data['SAT']

# y = b0 + b1x1
x = sm.add_constant(x1)# finding the constansts value,saying
results = sm.OLS(y,x).fit()
results.summary()# summary , gives dependent variable,model,method etc.
print(x)
#constant value is b0

plt.scatter(x1, y)

yhat = 0.0017 * x1 + 0.275

fig = plt.plot(x1, yhat, lw=4, c='orange', label = 'regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()