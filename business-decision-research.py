'''
Tujuan dari proyek ini adalah melakukan churn analysis terhadap produk.
Harapannya dapat memberikan rekomendasi dan strategi untuk menurunkan churn dari pelanggan.
'''

'''
Studi Kasus:
DQLab sport center adalah toko yang menjual berbagai kebutuhan olahraga seperti Jaket, Baju, Tas, dan Sepatu.
Toko ini mulai berjualan sejak tahun 2013, sehingga sudah memiliki pelanggan tetap sejak lama, dan tetap berusaha untuk mendapatkan pelanggan baru sampai saat ini.
Di awal tahun 2019, manajer toko merekrut junior DA untuk membantu memecahkan masalah menurunnya pelanggan yang membeli kembali ke tokonya.
Customer termasuk sudah bukan disebut pelanggan lagi (churn) ketika dia sudah tidak bertransaksi ke tokonya lagi sampai dengan 6 bulan terakhir dari update data terakhir.  
Manajer toko pun memberikan data transaksi dari tahun 2013 - 2019 dalam bentuk csv (data_retail.csv) dengan 100.000 baris data.

* Field yang ada pada data tersebut antara lain:
  - No
  - Row_Num
  - Customer_ID
  - Product
  - First_Transaction
  - Last_Transaction
  - Average_Transaction_Amount
  - Count_Transaction
'''

'''
Alur Kerja:
- Data preparation test
  - Importing data: Melakukan import data_retail.csv ke python environment.
  - Cleansing data: Melakukan pembersihan dan modifikasi data sehingga siap digunakan untuk analisis lebih lanjut.
- Data visualization test: Mendapatkan insight dari hasil visualisasi yang telah dibuat.
- Basic stats method test: Mendapatkan insight dari model dan evaluasi model yang sudah dibuat dan diuji.
'''

''' [1] DATA PREPARATION '''
# Importing Data dan Inspection
import pandas as pd
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/data_retail.csv', sep=';')
print('Lima data teratas:')
print(df.head())
print('\nInfo dataset:')
print(df.info())

# Output:
# Lima data teratas:
#    no  Row_Num  ...  Average_Transaction_Amount Count_Transaction
# 0   1        1  ...                     1467681                22
# 1   2        2  ...                     1269337                41
# 2   3        3  ...                      310915                30
# 3   4        4  ...                      722632                27
# 4   5        5  ...                     1775036                25
# 
# [5 rows x 8 columns]
# 
# Info dataset:
# RangeIndex: 100000 entries, 0 to 99999
# Data columns (total 8 columns):
# no                            100000 non-null int64
# Row_Num                       100000 non-null int64
# Customer_ID                   100000 non-null int64
# Product                       100000 non-null object
# First_Transaction             100000 non-null int64
# Last_Transaction              100000 non-null int64
# Average_Transaction_Amount    100000 non-null int64
# Count_Transaction             100000 non-null int64
# dtypes: int64(7), object(1)

# Data Cleansing
df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit='s', origin='1970-01-01')
df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit='s', origin='1970-01-01')
print('\nInfo dataset:')
print(df.info())

# Output:
# Info dataset:
# Data columns (total 8 columns):
# no                            100000 non-null int64
# Row_Num                       100000 non-null int64
# Customer_ID                   100000 non-null int64
# Product                       100000 non-null object
# First_Transaction             100000 non-null datetime64[ns]
# Last_Transaction              100000 non-null datetime64[ns]
# Average_Transaction_Amount    100000 non-null int64
# Count_Transaction             100000 non-null int64
# dtypes: datetime64[ns](2), int64(5), object(1)

# Churn Customers
# Untuk menentukan churn customers sesuai definisi yang telah diberikan, carilah:
# 1. transaksi paling terakhir kapan dilakukan
# 2. klasifikasikanlah mana customer yang berstatus churn dan mana yang tidak.
print(max(df['Last_Transaction']))
df.loc[df['Last_Transaction'] <= '2018-08-01', 'is_churn'] = True 
df.loc[df['Last_Transaction'] > '2018-08-01', 'is_churn'] = False
print('Lima data teratas:')
print(df.head())
print('\nInfo dataset:')
print(df.info())

# Output:
# Lima data teratas:
#    no  Row_Num  ...  Count_Transaction is_churn
# 0   1        1  ...                 22    False
# 1   2        2  ...                 41    False
# 2   3        3  ...                 30    False
# 3   4        4  ...                 27    False
# 4   5        5  ...                 25    False
# [5 rows x 9 columns]
# 
# Info dataset:
# Data columns (total 9 columns):
# no                            100000 non-null int64
# Row_Num                       100000 non-null int64
# Customer_ID                   100000 non-null int64
# Product                       100000 non-null object
# First_Transaction             100000 non-null datetime64[ns]
# Last_Transaction              100000 non-null datetime64[ns]
# Average_Transaction_Amount    100000 non-null int64
# Count_Transaction             100000 non-null int64
# is_churn                      100000 non-null bool
# dtypes: bool(1), datetime64[ns](2), int64(5), object(1)

# Menghapus kolom yang tidak diperlukan
del df['no']
del df['Row_Num']
# Cetak lima data teratas
print(df.head())

# Output:
#    Customer_ID Product  ... Average_Transaction_Amount Count_Transaction
# 0        29531   Jaket  ...                    1467681                22
# 1        29531  Sepatu  ...                    1269337                41
# 2       141526     Tas  ...                     310915                30
# 3       141526   Jaket  ...                     722632                27
# 4        37545  Sepatu  ...                    1775036                25
# [5 rows x 6 columns]


''' [2] DATA VISUALIZATION '''
# Customer Acquisition by Year
import matplotlib.pyplot as plt
df['Year_First_Transaction'] = df['First_Transaction'].dt.year
df['Year_Last_Transaction'] = df['Last_Transaction'].dt.year
df_year = df.groupby(['Year_First_Transaction'])['Customer_ID'].count()
df_year.plot(x='Year_First_Transaction', y='Customer_ID', kind='bar', title='Graph of Customer Acquisition')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

# Transaction by Year
import matplotlib.pyplot as plt
plt.clf()
df_year = df.groupby(['Year_First_Transaction'])['Count_Transaction'].sum()
df_year.plot(x='Year_First_Transaction', y='Count_Transaction', kind='bar', title='Graph of Transaction Customer')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Transaction')
plt.tight_layout()
plt.show()

# Average Transaction Amount by Year
import matplotlib.pyplot as plt
import seaborn as sns
plt.clf()
sns.pointplot(data = df.groupby(['Year_First_Transaction', 'Product']).mean().reset_index(),
			        x='Year_First_Transaction', 
              y='Average_Transaction_Amount', 
              hue='Product')
plt.tight_layout()
plt.show()

# Proporsi Churned Customer untuk Setiap Produk
import matplotlib.pyplot as plt
plt.clf()
df_piv = df.pivot_table(index='is_churn', 
                        columns='Product',
                        values='Customer_ID', 
                        aggfunc='count', 
                        fill_value=0)
plot_product = df_piv.count().sort_values(ascending=False).head(5).index
df_piv = df_piv.reindex(columns=plot_product)
df_piv.plot.pie(subplots=True,
                figsize=(10, 7),
                layout=(-1, 2),
                autopct='%1.0f%%',
                title='Proportion Churn by Product')
plt.tight_layout()
plt.show()

# Distribusi Kategorisasi Count Transaction
import matplotlib.pyplot as plt
plt.clf()
def func(row):
    if row['Count_Transaction'] == 1:
        val = '1. 1'
    elif (row['Count_Transaction'] > 1 and row['Count_Transaction'] <= 3):
        val ='2.2 - 3'
    elif (row['Count_Transaction'] > 3 and row['Count_Transaction'] <= 6):
        val ='3.4 - 6'
    elif (row['Count_Transaction'] > 6 and row['Count_Transaction'] <= 10):
        val ='4.7 - 10'
    else:
        val ='5. >10'
    return val
df['Count_Transaction_Group'] = df.apply(func, axis=1)
df_year = df.groupby(['Count_Transaction_Group'])['Customer_ID'].count()
df_year.plot(x='Count_Transaction_Group', y='Customer_ID', kind='bar', title='Customer Distribution by Count Transaction Group')
plt.xlabel('Count_Transaction_Group')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

# Distribusi Kategorisasi Average Transaction Amount
import matplotlib.pyplot as plt
plt.clf()
def f(row):
    if (row['Average_Transaction_Amount'] >= 100000 and row['Average_Transaction_Amount'] <=250000):
        val ='1. 100.000 - 250.000'
    elif (row['Average_Transaction_Amount'] > 250000 and row['Average_Transaction_Amount'] <=500000):
        val ='2. >250.000 - 500.000'
    elif (row['Average_Transaction_Amount'] > 500000 and row['Average_Transaction_Amount'] <=750000):
        val ='3. >500.000 - 750.000'
    elif (row['Average_Transaction_Amount'] > 750000 and row['Average_Transaction_Amount'] <=1000000):
        val ='4. >750.000 - 1.000.000'
    elif (row['Average_Transaction_Amount'] > 1000000 and row['Average_Transaction_Amount'] <=2500000):
        val ='5. >1.000.000 - 2.500.000'
    elif (row['Average_Transaction_Amount'] > 2500000 and row['Average_Transaction_Amount'] <=5000000):
        val ='6. >2.500.000 - 5.000.000'
    elif (row['Average_Transaction_Amount'] > 5000000 and row['Average_Transaction_Amount'] <=10000000):
        val ='7. >5.000.000 - 10.000.000'
    else:
        val ='8. >10.000.000'
    return val
df['Average_Transaction_Amount_Group'] = df.apply(f, axis=1)
df_year = df.groupby(['Average_Transaction_Amount_Group'])['Customer_ID'].count()
df_year.plot(x='Average_Transaction_Amount_Group', y='Customer_ID', kind='bar', title='Customer Distribution by Average Transaction Amount Group')
plt.xlabel('Average_Transaction_Amount_Group')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

