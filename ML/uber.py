from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt
data = pd.read_csv('uber.csv')
data.head()
data.tail()
data.shape
data.isnull().sum()
data.dropna(inplace=True)
data.isnull().sum()
X = data[["pickup_longitude", "dropoff_longitude","pickup_latitude", "dropoff_latitude"]]
X.head()
y = data["fare_amount"]
y.shape
corr = data.corr()
print(corr)
dataplot = sns.heatmap(data.corr(), annot=True, cmap="YlGnBu")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
error_rate_test = r2_score(y_test, y_pred)
error_rate_test
print(mean_squared_error(y_test, y_pred, squared=False))
rmse = sqrt(mean_squared_error(y_test, y_pred, ))
rmse
from sklearn.ensemble import RandomForestRegressor
model2= RandomForestRegressor()
model2.fit(X_train, y_train)
y_predrf = model2.predict(X_test)
r2 = r2_score(y_test, y_pred)
r2
