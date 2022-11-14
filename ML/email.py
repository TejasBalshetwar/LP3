from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
data = pd.read_csv("emails.csv")
data.head()
data.columns
data.isnull().sum()
data.dropna(inplace=True)
data.drop(["Email No."], axis=1, inplace=True)
X = data.drop(["Prediction"], axis=1)
y = data["Prediction"]
X = scale(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", metrics.confusion_matrix(y_test, y_pred))
model2 = SVC(C=1)
model2.fit(X_train, y_train)
y_pred = model2.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", metrics.confusion_matrix(y_test, y_pred))
