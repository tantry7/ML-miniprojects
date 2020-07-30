import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

data = pd.read_csv('players_20.csv')

x1 =data['overall']
y =data['wage_eur']

x = sm.add_constant(x1)# finding the constansts value,saying
results = sm.OLS(y,x).fit()
results.summary()# summary , gives dependent variable,model,method etc.
print(x)

plt.scatter(x1, y)

yhat = 1762.1523 * x1 + (-1.073e+05)

fig = plt.plot(x1, yhat, lw=4, c='orange', label = 'regression line')
plt.xlabel('overall', fontsize = 20)
plt.ylabel('wage', fontsize = 20)
plt.show()