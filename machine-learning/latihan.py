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

