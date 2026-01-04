''' Eksplorasi Data: Memahami Data dengan Statistik - Part 1 '''
import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
print('Shape dataset:', dataset.shape)
print('\nLima data teratas:\n', dataset.head())
print('\nInformasi dataset:')
print(dataset.info())
print('\nStatistik deskriptif:\n', dataset.describe())

''' Eksplorasi Data: Memahami Data dengan Statistik - Part 2 '''
dataset_corr = dataset.corr()
print('Korelasi dataset:\n', dataset.corr())
print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())
# Tugas praktek
print('Korelasi BounceRates-ExitRates:\n', dataset_corr.loc['BounceRates', 'ExitRates'])
print('Korelasi Revenue-PageValues:\n', dataset_corr.loc['Revenue', 'PageValues'])
print('Korelasi TrafficType-Weekend:\n', dataset_corr.loc['TrafficType', 'Weekend'])

''' Eksplorasi Data: Memahami Data dengan Visual '''
# checking the Distribution of customers on Revenue
plt.rcParams['figure.figsize'] = (12,5)
plt.subplot(1, 2, 1) # Arti: baris ada 1, kolom ada 2, kolom ke-1
sns.countplot(dataset['Revenue'], palette = 'pastel')
plt.title('Buy or Not', fontsize = 20)
plt.xlabel('Revenue or not', fontsize = 14)
plt.ylabel('count', fontsize = 14)
# checking the Distribution of customers on Weekend
plt.subplot(1, 2, 2) # Arti: baris ada 1, kolom ada 2, kolom ke-2
sns.countplot(dataset['Weekend'], palette = 'inferno')
plt.title('Purchase on Weekends', fontsize = 20)
plt.xlabel('Weekend or not', fontsize = 14)
plt.ylabel('count', fontsize = 14)
plt.show()

''' Tugas Praktek '''
# Membuat visualisasi berupa histogram yang menggambarkan jumlah customer untuk setiap Region.
# visualizing the distribution of customers around the Region
plt.hist(dataset['Region'], color = 'lightblue')
plt.title('Distribution of Customer', fontsize = 20)
plt.xlabel('Region Codes', fontsize = 14)
plt.ylabel('Count Users', fontsize = 14)
plt.show()

''' Data Pre-processing: Handling Missing Value - Part 1 '''
#checking missing value for each feature  
print('Checking missing value for each feature:')
print(dataset.isnull().sum())
#Counting total missing value
print('\nCounting total missing value:')
print(dataset.isnull().sum().sum())

''' Data Pre-processing: Handling Missing Value - Part 2 '''
# Metode ini dapat diterapkan jika tidak banyak missing value dalam data, sehingga walaupun data point ini dihapus, kita masih memiliki sejumlah data yang cukup untuk melatih model Machine Learning.
# Tetapi jika kita memiliki banyak missing value dan tersebar di setiap variabel, maka metode menghapus missing value tidak dapat digunakan.
# Kita akan kehilangan sejumlah data yang tentunya mempengaruhi performansi model.
#Drop rows with missing value   
dataset_clean = dataset.dropna()  
print('Ukuran dataset_clean:', dataset_clean.shape) 

''' Data Pre-processing: Handling Missing Value - Part 3 '''
# Menggunakan metode impute missing value, yaitu mengisi record yang hilang ini dengan suatu nilai.
# Ada berbagai teknik dalam metode imputing, mengisi missing value dengan nilai mean, median, modus, atau nilai konstan, sampai menggunakan nilai yang diestimasi oleh suatu predictive model.
# Untuk kasus ini, kita akan menggunakan imputing sederhana yaitu menggunakan nilai rataan atau mean.
print("\nAfter imputation:")
# Fill missing value with mean of feature value  
dataset.fillna(dataset.mean(), inplace = True)
# Checking missing value for each feature  
print(dataset.isnull().sum())
# Counting total missing value  
print(dataset.isnull().sum().sum())

''' Tugas Praktek '''
# Praktekkan metode imputing missing value dengan menggunakan nilai median.
print("\nAfter imputation:")
# Fill missing value with median of feature value  
dataset.fillna(dataset.median(), inplace = True)
# Checking missing value for each feature  
print(dataset.isnull().sum())
# Counting total missing value  
print(dataset.isnull().sum().sum())

''' Data Preprocessing: Scaling '''
from sklearn.preprocessing import MinMaxScaler  
#Define MinMaxScaler as scaler  
scaler = MinMaxScaler()  
#list all the feature that need to be scaled
scaling_column = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues']
#Apply fit_transfrom to scale selected feature  
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])
#Cheking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min','max']])

''' Data Pre-processing: Konversi String ke Numerik '''
# Kita memiliki dua kolom yang bertipe object yang dinyatakan dalam tipe data str, yaitu kolom 'Month' dan 'VisitorType'.
import numpy as np
from sklearn.preprocessing import LabelEncoder
# Convert feature/column 'Month'
LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])
print(LE.classes_)
print(np.sort(dataset['Month'].unique()))
print('')
# Convert feature/column 'VisitorType'
LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])
print(LE.classes_)
print(np.sort(dataset['VisitorType'].unique()))
# LabelEncoder akan mengurutkan label secara otomatis secara alfabetik lalu mengkonversi pandas objek ke numeris menurut posisi/indeks dari setiap label.
# Dengan demikian kita telah membuat dataset menjadi bernilai numeris seluruhnya yang siap digunakan untuk pemodelan dengan algoritma machine learning.


''' PEMODELAN DENGAN SCIKIT-LEARN '''
''' Features & Label '''
# Dalam dataset user online purchase, label target sudah diketahui: kolom Revenue = 1 untuk user yang membeli dan 0 untuk yang tidak membeli => pemodelannya klasifikasi.
# Untuk melatih dataset menggunakan Scikit-Learn library, dataset perlu dipisahkan ke dalam Features dan Label/Target.
# Variabel Feature akan terdiri dari variabel yang dideklarasikan sebagai X dan [Revenue] adalah variabel Target yang dideklarasikan sebagai y.
# Gunakan fungsi drop() untuk menghapus kolom [Revenue] dari dataset.
# removing the target column Revenue from dataset and assigning to X
X = dataset.drop(['Revenue'], axis = 1)
# assigning the target column Revenue to y
y = dataset['Revenue']
# checking the shapes
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

''' Training dan Test Dataset '''
from sklearn.model_selection import train_test_split
# splitting the X, and y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# checking the shapes
print("Shape of X_train :", X_train.shape) # Shape of X_train : (9864, 17)
print("Shape of y_train :", y_train.shape) # Shape of y_train : (9864,)
print("Shape of X_test :", X_test.shape) # Shape of X_test : (2466, 17)
print("Shape of y_test :", y_test.shape) # Shape of y_test : (2466,)

''' Training Model: Fit '''
# Sekarang saatnya kita melatih model atau training.
# Dengan Scikit-Learn, proses ini cukup dengan memanggil nama algorithm yang akan kita gunakan:
# - Classifier untuk problem klasifikasi
# - Regressor untuk problem regresi.
from sklearn.tree import DecisionTreeClassifier
# Call the classifier
model = DecisionTreeClassifier()
# Fit the classifier to the training data
model = model.fit(X_train, y_train)

''' Training Model: Predict '''
# Setelah model/classifier terbentuk, selanjutnya kita memprediksi LABEL dari testing dataset (X_test).
# Langkah ini menggunakan fungsi .predict().
# Fungsi ini akan mengembalikan hasil prediksi untuk setiap data point dari X_test dalam bentuk array.
# Proses ini kita kenal dengan TESTING.
# Apply the classifier/model to the test data
y_pred = model.predict(X_test)
print(y_pred.shape) # (2466,)

''' Evaluasi Model Performance '''
# evaluating the model
print('Training Accuracy :', model.score(X_train, y_train))
print('Testing Accuracy :', model.score(X_test, y_test))
# confusion matrix
print('\nConfusion matrix:')
cm = confusion_matrix(y_test, y_pred)
print(cm)
# classification report
print('\nClassification report:')
cr = classification_report(y_test, y_pred)
print(cr)
## [OUTPUT]
## Training Accuracy : 1.0
## Testing Accuracy : 0.8605028386050284

## Confusion matrix:
## [[1881  163]
##  [ 181  241]]

## Classification report:
##               precision    recall  f1-score   support
## 
##        False       0.91      0.92      0.92      2044
##         True       0.60      0.57      0.58       422
## 
##     accuracy                           0.86      2466
##    macro avg       0.75      0.75      0.75      2466
## weighted avg       0.86      0.86      0.86      2466

''' ALGORITMA MACHINE LEARNING '''
''' Classification : Logistic Regression '''
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
# Call the classifier
logreg = LogisticRegression()
# Fit the classifier to the training data  
logreg = logreg.fit(X_train, y_train)
#Training Model: Predict 
y_pred = logreg.predict(X_test)
#Evaluate Model Performance
print('Training Accuracy :', logreg.score(X_train, y_train))  
print('Testing Accuracy :', logreg.score(X_test, y_test))  
# confusion matrix
print('\nConfusion matrix')  
cm = confusion_matrix(y_test, y_pred)  
print(cm)
# classification report  
print('\nClassification report')  
cr = classification_report(y_test, y_pred)  
print(cr)

''' Classification - Decision Tree '''
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# Call the classifier
decision_tree = DecisionTreeClassifier()
# Fit the classifier to the training data
decision_tree = decision_tree.fit(X_train, y_train)
# evaluating the decision_tree performance
print('Training Accuracy :', decision_tree.score(X_train, y_train))
print('Testing Accuracy :', decision_tree.score(X_test, y_test))


''' Regression: Linear Regression '''
# 1. Pisahkan dataset ke dalam Feature dan Label, gunakan fungsi .drop(). Pada dataset ini, label/target adalah variabel MEDV
# 2. Checking dan print jumlah data setelah Dataset pisahkan ke dalam Feature dan Label, gunakan .shape()
# 3. Bagi dataset ke dalam Training dan test dataset, 70% data digunakan untuk training dan 30% untuk testing, gunakan fungsi train_test_split() , dengan random_state = 0
# 4. Checking dan print kembali jumlah data dengan fungsi .shape()
# 5. Import LinearRegression dari sklearn.linear_model
# 6. Deklarasikan  LinearRegression regressor dengan nama reg
# 7. Fit regressor ke training dataset dengan .fit(), dan gunakan .predict() untuk memprediksi nilai dari testing dataset.
## Untuk pemodelan ini kita akan menggunakan data ‘Boston Housing Dataset’,
## karena untuk linear regression target/label harus berupa numerik, sedangkan target dari online purchase data adalah categorical.

#load dataset
import pandas as pd
housing = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/housing_boston.csv')
#Data rescaling
from sklearn import preprocessing
data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
housing[['RM','LSTAT','PTRATIO','MEDV']] = data_scaler.fit_transform(housing[['RM','LSTAT','PTRATIO','MEDV']])
# getting dependent and independent variables
X = housing.drop(['MEDV'], axis = 1)
y = housing['MEDV']
# checking the shapes
print('Shape of X:', X.shape)
print('Shape of y:', y.shape)
# splitting the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# checking the shapes  
print('Shape of X_train :', X_train.shape)
print('Shape of y_train :', y_train.shape)
print('Shape of X_test :', X_test.shape)
print('Shape of y_test :', y_test.shape)
##import regressor from Scikit-Learn
from sklearn.linear_model import LinearRegression
# Call the regressor
reg = LinearRegression()
# Fit the regressor to the training data  
reg = reg.fit(X_train, y_train)
# Apply the regressor/model to the test data  
y_pred = reg.predict(X_test)

''' Regression Performance Evaluation '''
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt 
#Calculating MSE, lower the value better it is. 0 means perfect prediction
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error of testing set:', mse)
#Calculating MAE
mae = mean_absolute_error(y_test, y_pred)
print('Mean absolute error of testing set:', mae)
#Calculating RMSE
rmse = np.sqrt(mse)
print('Root Mean Squared Error of testing set:', rmse)
#Plotting y_test dan y_pred
plt.scatter(y_test, y_pred, c = 'green')
plt.xlabel('Price Actual')
plt.ylabel('Predicted value')
plt.title('True value vs predicted value : Linear Regression')
plt.show()

''' UNSUPERVISED LEARNING '''
''' K-Means Clustering '''
# Untuk praktik  ini, kita akan menggunakan dataset ‘Mall Customer Segmentation’.
# Dataset ini merupakan data customer mall dan berisi kolom : CustomerID, age, gender, annual income, dan spending score.
# Tujuan dari clustering adalah untuk memahami customer - customer mana saja yang sering melakukan transaksi.
#import library
import pandas as pd  
from sklearn.cluster import KMeans
#load dataset
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/mall_customers.csv')
#selecting features  
X = dataset[['annual_income','spending_score']]
#Define KMeans as cluster_model  
cluster_model = KMeans(n_clusters = 5, random_state = 24)  
labels = cluster_model.fit_predict(X)

#import library
import matplotlib.pyplot as plt
#convert dataframe to array
X = X.values
#Separate X to xs and ys --> use for chart axis
xs = X[:,0]
ys = X[:,1]
# Make a scatter plot of xs and ys, using labels to define the colors
plt.scatter(xs,ys,c=labels, alpha=0.5)
# Assign the cluster centers: centroids
centroids = cluster_model.cluster_centers_
# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]
# Make a scatter plot of centroids_x and centroids_y
plt.scatter(centroids_x,centroids_y,marker='D', s=50)
plt.title('K Means Clustering', fontsize = 20)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

''' Measuring Cluster Criteria '''
#import library
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#Elbow Method - Inertia plot
inertia = []
#looping the inertia calculation for each k
for k in range(1, 10):
    #Assign KMeans as cluster_model
    cluster_model = KMeans(n_clusters = k, random_state = 24)
    #Fit cluster_model to X
    cluster_model.fit(X)
    #Get the inertia value
    inertia_value = cluster_model.inertia_
    #Append the inertia_value to inertia list
    inertia.append(inertia_value)
##Inertia plot
plt.plot(range(1, 10), inertia)
plt.title('The Elbow Method - Inertia plot', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('inertia')
plt.show()
