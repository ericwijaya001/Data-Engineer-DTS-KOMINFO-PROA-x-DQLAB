# Downsampling Data
# Sekarang akan dicoba melakukan proses downsampling pada dataset 'https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv' yang telah di load sebelumnya.

# Perhatikan dataset awal:



# yaitu:



 

# Dengan men-downsampling dari:

# [1] Daily to monthly



# dengan output:



 

# [2] Daily to yearly



# dengan output:



 

# Tugas Praktek:

# Kerjakanlah proses downsampling

# Daily to weekly dan apply max
# Daily to quaterly dan apply min
# di code editor dengan jalan mengisi kode yang tidak lengkap (_ _ _).

# Jika dengan benar ditulis dan dijalankan dengan menekan , maka diperoleh output berikut di console:





import pandas as pd
# Load dataset https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv
gaq = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv')
gaq['timestamp'] = pd.to_datetime(gaq['timestamp'])
gaq = gaq.set_index('timestamp')
print('Dataset sebelum di-downsampling (5 teratas):\n', gaq.head())
# [1] Downsampling dari daily to weekly dan kita hitung maksimum untuk seminggu
gaq_weekly = gaq.resample('W').max()
print('Downsampling daily to weekly - max (5 teratas):\n', gaq_weekly.head())
# [2] Downsampling dari daily to quaterly dan kita hitung minimumnya untuk tiap quarter
gaq_quaterly = gaq.resample('Q').min()
print('Downsampling daily to quaterly - min (5 teratas):\n', gaq_quaterly.head())