from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
data = pandas.read_csv("diabetes.csv")
data.head()
data.tail()
data.shape
data.isnull().sum()
X = data.drop('Outcome', axis=1)
y = data['Outcome']
X.shape, y.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
scaler = MinMaxScaler()
Xtrain_scaled = scaler.fit_transform(X_train)
Xtest_scaled = scaler.fit_transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(Xtrain_scaled, y_train)
y_pred = knn.predict(Xtest_scaled)
from sklearn.metrics import accuracy_score
print(f"Accuracy for KNN model : {accuracy_score(y_test, y_pred)}")
from sklearn.metrics import classification_report
print(classification_report(y_pred, y_test))
from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(y_pred, y_test)
sns.heatmap(cm, annot=True)

