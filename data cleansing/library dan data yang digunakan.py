# Pandas

# Pandas (Python for Data Analysis) adalah library Python yang fokus untuk proses analisis data seperti manipulasi data, persiapan data, dan pembersihan data.

# read_csv() digunakan untuk membaca file csv
# str.match() digunakan untuk mencocokan dengan karakter tertentu
# drop() digunakan untuk menghapus
# count() digunakan untuk menghitung masing-masing variable
# drop_duplicates() digunakan untuk menghapus data duplicate rows
# fillna() digunakan untuk mengisi dengan nilai tertentu
# quantile() digunakan untuk melihat quantile ke tertentu
# mask() mengganti nilai tertentu jika kondisi memenuhi
# astype() mengubah tipe data
# value_counts() digunakan untuk menghitung unik dari kolom
# sort_values() digunakan untuk sort values
# isnull() digunakan untuk mendeteksi missing values
# dropna() digunakan untuk menghapus missing values
# replace() digunakan untuk mengganti nilai
# Matplotlib

# Matplotlib adalah library Python yang fokus pada visualisasi data seperti membuat plot grafik. Matplotlib dapat digunakan dalam skrip Python, Python dan IPython shell, server aplikasi web, dan beberapa toolkit graphical user interface (GUI) lainnya.

# figure() digunakan untuk membuat figure gambar baru
# Seaborn

# Seaborn membangun di atas Matplotlib dan memperkenalkan tipe plot tambahan. Ini juga membuat plot Matplotlib tradisional Anda terlihat sedikit lebih cantik.

# box_plot() digunakan untuk membuat box plot







# Data yang Digunakan
# Untuk dataset yang digunakan sudah disediakan dalam format csv, silahkan baca melalui fungsi pandas di python df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')

 
# Untuk detail datanya adalah sebagai berikut:

# UpdatedAt Periode of Data taken
# customerID Customer ID
# gender Whether the customer is a male or a female (Male, Female)
# SeniorCitizen Whether the customer is a senior citizen or not (1, 0)
# Partner Whether the customer has a partner or not (Yes, No)
# Dependents Whether the customer has dependents or not (Yes, No)
# tenure Number of months the customer has stayed with the company
# PhoneService Whether the customer has a phone service or not (Yes, No)
# MultipleLines Whether the customer has multiple lines or not (Yes, No, No phone service)
# InternetService Customer’s internet service provider (DSL, Fiber optic, No)
# OnlineSecurity Whether the customer has online security or not (Yes, No, No internet service)
# OnlineBackup Whether the customer has online backup or not (Yes, No, No internet service)
# DeviceProtection Whether the customer has device protection or not (Yes, No, No internet service)
# TechSupport Whether the customer has tech support or not (Yes, No, No internet service)
# StreamingTV Whether the customer has streaming TV or not (Yes, No, No internet service)
# StreamingMovies Whether the customer has streaming movies or not (Yes, No, No internet service)
# Contract The contract term of the customer (Month-to-month, One year, Two year)
# PaperlessBilling Whether the customer has paperless billing or not (Yes, No)
# PaymentMethod The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
# MonthlyCharges The amount charged to the customer monthly
# TotalCharges The total amount charged to the customer
# Churn Whether the customer churned or not (Yes or No)








# Import Library dan Dataset
# Berdasarkan penjelasan mengenai library dan dataset yang akan digunakan, sekarang hal pertama yang akan kita lakukan adalah melakukan import library dan dataset ke dalam workspace kita.

# Setelah dataset di-import ke dalam workspace, tampilkan jumlah kolom dan baris dari data set dengan menggunakan .shape dan print 5 baris teratas dengan menggunakan head() dan carilah ada berapa nilai customerID yang bersifat unique dengan menggunakan .unique

# import pandas as pd
# pd.options.display.max_columns = 50

# df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')
# Notes:

# 1. pd.options.display.max_columns = 50 digunakan untuk mempermudah penampilan row data

# 2. Simpan dataset ke dalam variabel df_load


import pandas as pd
pd.options.display.max_columns = 50
# Importing Data Source
df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')
print(df_load.shape)
print(df_load.head(5))
print(df_load.customerID.nunique())