'''
Divisi e-commerce ingin memprediksi apakah user-user yang sedang mengunjungi halaman website yang baru akan mengklik banner promo (ads) di halaman tersebut atau tidak berdasarkan feature yang ada.
Tolong buatkan machine learning model untuk menyelesaikan permasalahan dari e-commerce kita ini.
Adapun feature - feature dalam dataset ini adalah :
- 'Daily Time Spent on Site' : lama waktu user mengunjungi site (menit)
- 'Age' : usia user (tahun)
- 'Area Income' : rata - rata pendapatan di daerah sekitar user
- 'Daily Internet Usage' : rata - rata waktu yang dihabiskan user di internet dalam sehari (menit)
- 'Ad Topic Line' : topik/konten dari promo banner
- 'City' : kota dimana user mengakses website
- 'Male' : apakah user adalah Pria atau bukan
- 'Country' : negara dimana user mengakses website
- 'Timestamp' : waktu saat user mengklik promo banner atau keluar dari halaman website tanpa mengklik banner
- 'Clicked on Ad' : mengindikasikan user mengklik promo banner atau tidak (0 = tidak; 1 = klik).
'''

''' LANGKAH 1: Data eksplorasi '''
#import library 
import pandas as pd

# Baca data 'ecommerce_banner_promo.csv'
data = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/ecommerce_banner_promo.csv')

#1. Data eksplorasi dengan head(), info(), describe(), shape
print("\n[1] Data eksplorasi dengan head(), info(), describe(), shape")
print("Lima data teratas:")
print(data.head())
print("Informasi dataset:")
print(data.info())
print("Statistik deskriptif dataset:")
print(data.describe())
print("Ukuran dataset:")
print(data.shape)

#2. Data eksplorasi dengan dengan mengecek korelasi dari setiap feature menggunakan fungsi corr()
print("\n[2] Data eksplorasi dengan dengan mengecek korelasi dari setiap feature menggunakan fungsi corr()")
print(data.corr())

#3. Data eksplorasi dengan mengecek distribusi label menggunakan fungsi groupby() dan size()
print("\n[3] Data eksplorasi dengan mengecek distribusi label menggunakan fungsi groupby() dan size()")
print(data.groupby('Clicked on Ad').size())
