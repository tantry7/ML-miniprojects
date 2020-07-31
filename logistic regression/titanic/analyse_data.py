sns.countplot(x ="Survived",data= titanic_data)
#data analysis
sns.countplot(x ="Survived",hue ="Sex",data=titanic_data)
sns.countplot(x ="Survived",hue ="Pclass",data=titanic_data)
titanic_data["Fare"].plot.hist(bins=20, fig=(10,5))
titanic_data["Age"].plot.hist()
titanic_data.info()
sns.countplot(x = "SibSp",data= titanic_data)
titanic_data.isnull()
