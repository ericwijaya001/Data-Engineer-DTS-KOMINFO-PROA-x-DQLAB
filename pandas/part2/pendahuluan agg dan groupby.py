# Teknik agregasi diperlukan ketika mau melihat dataset dengan view yang berbeda, bisa set data tersebut akan dikelompokkan seperti apa, yang kemudian juga bisa menerapkan beberapa fungsi atau metode statistik ke hasil group dataset itu untuk mengetahui behavior dari data tersebut secara summary/overview.

 

# Basic Concept of Groupby & Aggregation



# Groupby memiliki konsep untuk:

# Split: melakukan indexing/multi-indexing dengan apa yang di specify as groupby menjadi kelompok
# Apply: menerapkan fungsi pada masing-masing kelompok tersebut
# Combine: mengumpulkan semua hasil fungsi dari tiap kelompok kembali menjadi dataframe











# Review Inspeksi Data
# Mari review kembali terkait dengan inspeksi data yang pernah dilakukan pada modul sebelumnya. Akan menggunakan dataset https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv

# [1] Load data dari csv



# dengan output:



 

# [2] Melakukan pengecekan terhadap data



# dengan output:



 

# [3] Melakukan count tanpa groupby



# dengan output:



 

# [4] Melakukan count dengan groupby



# dengan output:



 

# Terdapat perbedaan antara melakukan count dengan groupby dan tanpa groupby:

# Terdapat index apa yang di specify as groupby
# Perhitungan jadi berdasarkan apa yang di specify as groupby
# Overall, lebih mudah untuk membaca data summary yang telah di groupby


import pandas as pd
# Load data global_air_quality.csv
global_air_quality = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv')
print('Lima data teratas:\n', global_air_quality.head())
# Melakukan pengecekan terhadap data
print('Info global_air_quality:\n', global_air_quality.info())
# Melakukan count tanpa groupby
print('Count tanpa groupby:\n', global_air_quality.count())
# Melakukan count dengan groupby 
gaq_groupby_count = global_air_quality.groupby('source_name').count()
print('Count dengan groupby (5 data teratas):\n', gaq_groupby_count.head())