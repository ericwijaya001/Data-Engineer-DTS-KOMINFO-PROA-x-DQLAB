# Resampling by Frequency
# Pada bagian ini akan mempelajari bagaimanakah caranya me-resampling data (baik upsampling atau downsampling) berdasarkan frekuensi, misalnya sekali 2 minggu, tiap 12 jam, dsb.

# Kondisi awal data yang dimiliki:



# dengan output:



 

# Untuk memahaminya silakan perhatikan contoh berikut ini:

# [1] Data ini downsampling dari daily to 2 weekly, kemudian dihitung rata-ratanya, jika ada nilai NaN maka dapat diisi dengan fillna method = 'ffill'



# dengan output:



 

# [2] Selanjutnya, data awal di upsampling dari daily to 8 hourly, kemudian hitung rata-ratanya, jika ada nilai NaN maka dapat di isi dengan fillna method = 'bfill'



# dengan output:



 

# Tugas Praktik:

# Kerjakanlah proses data awal resampling dari daily to bi-monthly, kemudian hitung rata-ratanya, jika ada nilai NaN maka dapat diisi dengan fillna method = 'bfill' serta mengisi kode yang tidak lengkap (_ _ _) di code editor.

# Jika dengan benar ditulis dan dijalankan dengan menekan , maka diperoleh output berikut di console.




import pandas as pd
# Load dataset https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv')
gaq['timestamp'] = pd.to_datetime(gaq['timestamp'])
gaq = gaq.set_index('timestamp')
print('Dataset sebelum di-resampling (5 teratas):\n', gaq.head())
# Resample dari daily to 2 monthly, hitung reratanya, dan fillna = 'bfill'
gaq_2monthly = gaq.resample('2M').mean().fillna(method='bfill')
print('Resampling daily to 2 monthly - mean - ffill (5 teratas):\n', gaq_2monthly.head())




Diberikan csv file: 'global_air_quality.csv'

Andra ingin mengetahui bagaimana trend dari nilai rata-rata pollutant SO2 (kolom pollutant) yang dihitung dari perhitungan value SO2 (kolom value) dalam tahunan, apa yang akan aku lakukan untuk membantu Andra?
Jawaban:
gaq.loc[gaq['pollutant'] == 'so2', 'value'].resample('A').mean().plot()
