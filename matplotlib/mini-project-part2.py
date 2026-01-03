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
dataset_top5brand_dec.groupby(['order_date','brand'])['quantity'].sum().unstack().plot(marker='.', cmap='plasma')
plt.title('Daily Sold Quantity Dec 2019 - Breakdown by Brands',loc='center',pad=30, fontsize=15, color='blue')
plt.xlabel('Order Date', fontsize = 12)
plt.ylabel('Quantity',fontsize = 12)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 1), shadow=True, ncol=1)
plt.annotate('Terjadi lonjakan', xy=(7, 310), xytext=(8, 300),
             weight='bold', color='red',
             arrowprops=dict(arrowstyle='->',
                             connectionstyle="arc3",
                             color='red'))
plt.gcf().set_size_inches(10, 5)
plt.tight_layout()
plt.show()

# CASE III
# Cari tahu jumlah product untuk masing-masing brand yang laku selama bulan Desember 2019.
# Gunakan barchart untuk visualisasinya, urutkan dengan yang kiri adalah brand dengan product lebih banyak.
