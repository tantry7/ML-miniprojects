t_data.isnull()
t_data.isnull().sum()
sns.heatmap(t_data.isnull(),  yticklabels='False')
sns.boxplot(x="Pclass",y = "Age",data = t_data)
t_data.head(5)
t_data.drop("Cabin",axis=1,inplace=True)
t_data.head(5)
t_data.dropna(inplace=True)
sns.heatmap(t_data.isnull(),yticklabels='False',cbar='False')
t_data.isnull().sum()
t = pd.read_csv('train.csv')

sex =pd.get_dummies(t['Sex'],drop_first=True)
sex.head(5)

embark = pd.get_dummies(t['Embarked'],drop_first=True)
embark.head(5)

pcl = pd.get_dummies(t['Pclass'],drop_first=True)
pcl.head(5)

titanic_data = pd.concat([t,sex,embark,pcl],axis=1)

titanic_data.head(5)

titanic_data.drop(['Sex','Embarked','PassengerId','Pclass','Name','Ticket'],axis =1,inplace=True)
titanic_data.head(5)
titanic_data.drop(['Age_wiki','Name_wiki','Hometown','Boarded','Destination','Cabin','WikiId','Lifeboat'],axis=1,inplace=True)


titanic_data.head(5)
titanic_data.drop(['Body'],axis=1,inplace=True)
titanic_data.head(5)
