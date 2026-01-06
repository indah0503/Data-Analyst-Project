''' [1] DATA PROFILING '''
''' Importing Data '''
import pandas as pd
import numpy as np
import io
import pandas_profiling
retail_raw = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

''' Inspeksi tipe data '''
# Cetak tipe data di setiap kolom retail_raw
print(retail_raw.dtypes)

''' Descriptive Statistics - Part 1 '''
# Kolom city
length_city = len(retail_raw['city'])
print('Length kolom city:', length_city)
# Tugas Praktek: Kolom product_id
length_product_id = len(retail_raw['product_id'])
print('Length kolom product_id:', length_product_id)

''' Descriptive Statistics - Part 2 '''
# Count kolom city
count_city = retail_raw['city'].count()
print('Count kolom count_city:', count_city)
# Tugas praktek: count kolom product_id
count_product_id = retail_raw['product_id'].count()
print('Count kolom product_id:', count_product_id)

''' Descriptive Statistics - Part 3 '''
# Missing value pada kolom city
number_of_missing_values_city = length_city - count_city
ratio_of_missing_values_city = number_of_missing_values_city/length_city
pct_of_missing_values_city = '{0:.1f}%'.format(ratio_of_missing_values_city * 100)
print('Persentase missing value kolom city:', pct_of_missing_values_city)
# Tugas praktek: Missing value pada kolom product_id
number_of_missing_values_product_id = length_product_id - count_product_id
ratio_of_missing_values_product_id = number_of_missing_values_product_id/length_product_id
pct_of_missing_values_product_id = '{0:.1f}%'.format(ratio_of_missing_values_product_id * 100)
print('Persentase missing value kolom product_id:', pct_of_missing_values_product_id)

''' Descriptive Statistics - Part 4 '''
# Deskriptif statistics kolom quantity
print('Kolom quantity')
print('Minimum value: ', retail_raw['quantity'].min())
print('Maximum value: ', retail_raw['quantity'].max())
print('Mean value: ', retail_raw['quantity'].mean())
print('Mode value: ', retail_raw['quantity'].mode())
print('Median value: ', retail_raw['quantity'].median())
print('Standard Deviation value: ', retail_raw['quantity'].std())
# Tugas praktek: Deskriptif statistics kolom item_price
print('')
print('Kolom item_price')
print('Minimum value: ', retail_raw['item_price'].min())
print('Maximum value: ', retail_raw['item_price'].max())
print('Mean value: ', retail_raw['item_price'].mean())
print('Median value: ', retail_raw['item_price'].median())
print('Standard Deviation value: ', retail_raw['item_price'].std())

''' Descriptive Statistics - Part 5 '''
# Quantile statistics kolom quantity
print('Kolom quantity:')
print(retail_raw['quantity'].quantile([0.25, 0.5, 0.75]))
# Tugas praktek: Quantile statistics kolom item_price
print('')
print('Kolom item_price:')
print(retail_raw['item_price'].quantile([0.25, 0.5, 0.75]))
# Quantiles adalah titik potong yang membagi distribusi dalam ukuran yang sama.
# Jika akan membagi distribusi menjadi empat grup yang sama, kuantil yang dibuat dinamai quartile.
# Jika dibagi kedalam 10 sepuluh grup yang sama dinamakan percentile.

''' Descriptive Statistics - Part 6 '''
print('Korelasi quantity dengan item_price')
print(retail_raw[['quantity', 'item_price']].corr())
# Korelasi adalah cara yang tepat untuk menemukan hubungan antara variabel numerik.
# Koefisien korelasi berkisar antara -1 hingga 1.
# Korelasi 1 adalah korelasi positif total, korelasi -1 adalah korelasi negatif total, dan korelasi 0 adalah korelasi non-linear.

''' Penggunaan Profiling Libraries '''
import pandas_profiling
pandas_profiling.ProfileReport(retail_raw)


''' [2] DATA CLEANSING '''
''' Missing Data '''
# Check kolom yang memiliki missing data
print('Check kolom yang memiliki missing data:')
print(retail_raw.isnull().any())
# Filling the missing value (imputasi)
print('\nFilling the missing value (imputasi):')
print(retail_raw['quantity'].fillna(retail_raw.quantity.mean()))
# Drop missing value
print('\nDrop missing value:')
print(retail_raw['quantity'].dropna())

''' Tugas Praktek '''
# Terdapat missing value pada kolom item_price.
# Lengkapi missing value tersebut dengan mean dari item_price.
print(retail_raw['item_price'].fillna(retail_raw['item_price'].mean()))

''' Outliers '''
# Q1, Q3, dan IQR
Q1 = retail_raw['quantity'].quantile(0.25)
Q3 = retail_raw['quantity'].quantile(0.75)
IQR = Q3 - Q1
# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang
print('Shape awal: ', retail_raw.shape)
# Removing outliers
retail_raw = retail_raw[~((retail_raw['quantity'] < (Q1 - 1.5 * IQR)) | (retail_raw['quantity'] > (Q3 + 1.5 * IQR)))]
# Check ukuran (baris dan kolom) setelah data yang outliers dibuang
print('Shape akhir: ', retail_raw.shape)

''' Tugas Praktek '''
# Menangani outlier pada kolom item_price
# Q1, Q3, dan IQR
Q1 = retail_raw['item_price'].quantile(0.25)
Q3 = retail_raw['item_price'].quantile(0.75)
IQR = Q3 - Q1
# Check ukuran (baris dan kolom) sebelum data yang outliers dibuang
print('Shape awal: ', retail_raw.shape)
# Removing outliers
retail_raw = retail_raw[~((retail_raw['item_price'] < (Q1 - 1.5 * IQR)) | (retail_raw['item_price'] > (Q3 + 1.5 * IQR)))]
# Check ukuran (baris dan kolom) setelah data yang outliers dibuang
print('Shape akhir: ', retail_raw.shape)

''' Deduplikasi Data '''
# Check ukuran (baris dan kolom) sebelum data duplikasi dibuang
print('Shape awal: ', retail_raw.shape)
# Mengecek duplikasi data
retail_raw.duplicated(subset=None) # hasilnya semua dari True dan False
print('Cek duplikat:\n', retail_raw[retail_raw.duplicated()]) # hasilnya hanya yang True
# Buang data yang terduplikasi
retail_raw.drop_duplicates(inplace=True)
# Check ukuran (baris dan kolom) setelah data duplikasi dibuang
print('Shape akhir: ', retail_raw.shape)
