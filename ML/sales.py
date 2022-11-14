from collections import Counter
from sklearn import preprocessing
from sklearn.cluster import KMeans
df = pd.read_csv('sales_data_sample.csv')
df.head()
df.info()
to_drop = ['ORDERNUMBER', 'PHONE', 'ADDRESSLINE1', 'ADDRESSLINE2', 'STATE', 'POSTALCODE', 'ORDERDATE', 'CUSTOMERNAME',
           'COUNTRY', 'TERRITORY', 'CONTACTLASTNAME']
df = df.drop(to_drop, axis=1)
le = preprocessing.LabelEncoder()
for i in df.columns:
    if df[i].dtype == 'object':
        df[i] = le.fit_transform(df[i])
df.info()
df.sample(5)
#  Elbow method to find the optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++',   # init = 'k-means++' is used to avoid random initialization trap
                    max_iter=300, n_init=10, random_state=0)
# n_init = 10 is used to run the algorithm 10 times with different initial centroids to choose the
#        final model as the one with the lowest SSE (Sum of Squared Errors)
# max_iter = 300 is used to set the maximum number of iterations for each single run
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss, 'bx-')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(df)
Counter(k_means.labels_)
sns.scatterplot(x=df['SALES'], y=df["PRODUCTCODE"], hue=k_means.labels_)
