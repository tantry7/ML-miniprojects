X = titanic_data.drop("Survived",axis=1)
y = titanic_data['Survived']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=1)
from sklearn.linear_model import LogisticRegression
logmodel =LogisticRegression()

logmodel.fit(X_train, y_train)
predections = logmodel.predict(X_test)
from sklearn.metrics import classification_report
classification_report(y_test,predictions)
