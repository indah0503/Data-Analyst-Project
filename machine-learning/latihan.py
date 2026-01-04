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
