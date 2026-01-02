import pandas as pd
import datetime

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')

''' Penambahan Kolom Order Month '''
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%Y-%m'))

''' Penambahan Kolom GMV (Gross Merchandise Value) => nilai total bruto '''
dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)

''' Menampilkan GMV Per Bulan '''
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()

''' Membuat Line Chart Trend Pertumbuhan GMV '''
plt.plot(monthly_amount['order_month'], monthly_amount['gmv'])
plt.show()

''' Cara Lain: Menggunakan .plot() '''
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

''' Mengubah Figure Size '''
plt.figure(figsize=(15,5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

''' Menambahkan Title and Axis Labels '''
plt.title('Monthly GMV Year 2019')
plt.xlabel('Order Month')
plt.ylabel('Total GMV')
plt.show()

''' Kustomisasi Title and Axis Labels '''
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)

''' Kustomisasi Line dan Point '''
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)

''' Kustomisasi Grid '''
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.show()

''' Kustomisasi Axis Ticks '''
# Kalau titik-titik di sumbu nilainya aneh, seperti 2.0, 2.5, 3.0 dsb atau 1e11.
# Buat saja dalam bentuk miliar agar lebih mudah dipahami (alias bulatkan).
# Nilai-nilai di sumbu x dan y bisa diakses melalui function plt.xticks() dan plt.yticks().
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.show()

''' Menentukan Batas Minimum dan Maksimum Axis Ticks '''
# Untuk setting agar sumbu-y nya dimulai dari 0, cukup tambahkan plt.ylim(ymin=0)
# Kita juga bisa mengatur batas minimum dan maksimum sumbu-x dengan function plt.xlim.
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.show()

''' Menambahkan Informasi Pada Plot '''
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', transform=fig.transFigure, color='red')
plt.show()
# Dua angka pertama itu adalah koordinat, x dan y.
# Saat set transform=fig.transFigure, maka koordinatnya berkisar 0 sampai 1.
# Jika parameter transform tidak diisi, maka koordinatnya dalam satuan inch.
# Seperti halnya title atau label, dimungkinkan juga untuk set warna dan ukuran hurufnya.

''' Menyimpan Hasil Plot Menjadi File Image '''
plt.savefig('monthly_gmv.png')
plt.show()
# Untuk mengetahui format file apa saja yang bida digunakan, kita bisa menjalankan code berikut: plt.gcf().canvas.get_supported_filetypes().

''' Pengaturan Parameter untuk Menyimpan Gambar '''
# Ada berbagai parameter yang bisa diatur saat menyimpan gambar, antara lain:
## dpi: Resolusi gambar (dots per inch). 
## quality: Kualitas gambar (hanya berlaku jika formatnya jpg atau jpeg), bisa diisi nilai 1 (paling buruk) hingga 95 (paling bagus).
## facecolor: Memberikan warna bagian depan figure, di luar area plot 
## edgecolor: Memberikan warna pinggiran gambar
## transparent: Jika nilainya True, maka gambarnya jadi transparan (jika file-nya png)
plt.savefig('monthly_gmv.png', quality=95)
plt.show()
