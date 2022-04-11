# Diberikan variabel

sample_csv = pd.read_csv('sample_csv.csv')
sample_csv = sample_csv.set_index(['province','product_id'])
idx = pd.IndexSlice
# Code mana yang akan menghasilkan semua kolom, dengan filter province = ‘Sulawesi Selatan’ dan product_id dari ‘P3082’ sampai ‘P3357’?

# JAWABAN

# sample_csv.sort_index().loc[idx['Sulawesi Selatan', 'P3082':'P3357'], :]
