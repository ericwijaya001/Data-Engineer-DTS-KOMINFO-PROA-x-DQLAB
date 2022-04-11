#     Method .concat() dapat digunakan pada dataframe yang ditujukan untuk penggabungan baik dalam row-wise (dalam arah) atau column-wise.

 

# Perhatikan contoh berikut, mulai dengan method .concat pada row-wise.



# Output-nya:



 

# Untuk penerapan concat pada column-wise:



# Output-nya:



 

# Dapat juga menambahkan identifier dari dataframe untuk data yang ditambahkan.



# Output-nya:



 

# Tugas Praktik:

# Balikkanlah posisi kedua dataframe yang akan digabungkan dengan concat. 

# Jika dijalankan dengan menekan tombol , output berikut yang akan diperoleh pada console


import pandas as pd
# Buat dataframe df1 dan df2
df1 = pd.DataFrame({'a':[1,2],
					'b':[3,4]})
df2 = pd.DataFrame({'b':[1,2],
					'a':[3,4]})
# Terapkan method concat row-wise
row_wise_concat = pd.concat([df2, df1])
print("Row-wise - concat:\n", row_wise_concat)
# Terapkan method concat column-wise
col_wise_concat = pd.concat([df2, df1], axis=1)
print("Column-wise - concat:\n", col_wise_concat)
# Penambahan identifier --> membentuk hasil penggabungan multiindex
multiindex_concat = pd.concat([df2,df1], axis=0, keys=['df2','df1'])
print("Multiindex - concat:\n", multiindex_concat)