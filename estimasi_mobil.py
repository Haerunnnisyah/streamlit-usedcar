import pickle
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Judul aplikasi
st.title('Estimasi Harga Mobil Bekas')

# Input dari pengguna
year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

# Variabel untuk menyimpan prediksi
predict = ''

# Tombol untuk melakukan prediksi
if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write('Estimasi harga mobil bekas dalam Pounds : ', predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta) : ', predict*16000)