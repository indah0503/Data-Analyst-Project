'''
Lakukan analisis untuk top brands di bulan Desember 2019.
Silakan ditambahkan dengan visualisasi-visualisasi lain yang dapat memberikan insight tambahan.
'''

# CASE I
# Buat variabel baru yang berisi data penjualan bulan Desember 2019,
# hanya untuk top 5 brand dengan quantity terjual terbanyak selama bulan Desember 2019. 
import datetime
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']
#mengambil informasi top 5 brands berdasarkan quantity
top_brands = (dataset[dataset['order_month']=='12-2019'].groupby('brand')['quantity']
                .sum()
                .reset_index()
                .sort_values(by='quantity',ascending=False)
                .head(5))

#membuat dataframe baru, filter hanya di bulan Desember 2019 dan hanya top 5 brands
dataset_top5brand_dec = dataset[(dataset['order_month']=='12-2019') & (dataset['brand'].isin(top_brands['brand'].to_list()))]
# print top brands
print(top_brands)

# CASE II
# Buat visualisasi multi-line chart untuk daily quantity terjualnya, breakdown per brand.
# Beri anotasi untuk titik lonjakan (quantity lebih tinggi dari tanggal-tanggal lain).
