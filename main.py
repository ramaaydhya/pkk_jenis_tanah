import streamlit as st

jenis_tanah = ""
jenis_sayur = {
"sand" : ['Kaktus', 'Buah Naga', "Lavender", 'Rosemary'],
"loam_sand" : ['sayuran berdaun hijau'],
"sandy_loam" : ['wortel', 'kentang', 'tomat', 'bunga mawar', 'bunga matahari'],
"loam" : ['kacang-kacangan', 'stroberi', 'pepaya'],
"silty_loam" : ['terong', 'bayam', 'bunga aster', 'bunga matahari'],
"sandy_clay_loam" : ['buncis', 'terong', 'apel', 'pir'],
"clay_loam" : ['kubis', 'bawang', 'kentang'],
"silty_clay_loam ": ['kentang', 'wortel'],
"sandy_clay ": ['kacang polong', 'jagung', 'bayam'],
"clay ": ['kacang panjang', 'kacang merah'],
"silty_clay ": ['kentang', 'lobak'],
}


con = st.container()
con.title("Langkah-Langkah Identifikasi Jenis Tanah")
con.header("Langkah 1")
con.write("Tambahkan air pada 25 gram tanah atau lebih. Lalu, remas (uleni) sampai plastis.")
con.write("Apakah dapat dibentuk bola di telapak tangan? Jika Ya, teruskan ke **Langkah 4**" )

radio_bentuk_bola = con.radio("", ["Ya", "Tidak"], key=1, index=None)

con.header("Langkah 2")
con.write("Apakah campuran tanah terlalu kering? Jika **Ya**, **ulangi Langkah 1**")
radio_kering = con.radio("", ["Ya", "Tidak"], key=2, index=None)
con.header("Langkah 3")
con.write("Apakah campuran tanah terlalu basah? Jika **Ya**, tambahkan tanah kering lagi ke campuran tanah tadi dan **ulangi Langkah 1**")
radio_basah = con.radio("", ["Ya", "Tidak"], key=3, index=None)


con.header("Langkah 4")
con.write("Bentuk menjadi pita dengan menekan tanah menggunakan kedua ujung telunjuk dan ibu jari, kemudian dipilin.")
con.write("Apakah mampu membentuk pita (lempengan tanah panjang) ?, Jika  **Tidak**, berhenti")
radio_bentuk_pita = con.radio("", ["Ya", "Tidak"], key=4, index=None)


con.header("Langkah 5")
con.write("Bentuk pita hingga terputus kemudian ukur panjang pita. Berapakah panjangnya?")
radio_tanya_panjang = con.radio("", ["Panjang pita < 2.5 cm sebelum terputus", "Panjang pita 2.5 - 5 cm sebelum terputus", "Panjang pita > 5 cm sebelum terputus"], key=5, index=None)

con.header("Langkah 6a : Jika panjang pita < 2.5 cm")
con.write("Sentuh pita tersebut. Apa yang Anda rasakan?")
radio_kategori_1 = con.radio("", ["Pita terasa kasar (pasir)", "Pita tidak terasa kasar (pasir) dan tidak terasa licin", "Pita terasa licin"], key=6, index=None)

con.header("Langkah 6b : Jika panjang pita 2.5 - 5 cm")
con.write("Sentuh pita tersebut. Apa yang Anda rasakan?")
radio_kategori_2 = con.radio("", ["Pita terasa kasar (pasir)", "Pita tidak terasa kasar (pasir) dan tidak terasa licin", "Pita terasa licin"], key=7, index=None)

con.header("Langkah 6c : Jika panjang pita > 5 cm")
con.write("Sentuh pita tersebut. Apa yang Anda rasakan?")
radio_kategori_3 = con.radio("", ["Pita terasa kasar (pasir)", "Pita tidak terasa kasar (pasir) dan tidak terasa licin", "Pita terasa licin"], key=8, index=None)

if radio_bentuk_bola == "Tidak" and radio_kering == "Tidak" and radio_basah == "Tidak" :
  jenis_tanah = "sand"

elif radio_bentuk_bola == "Ya" :
  if radio_bentuk_pita == "Tidak" :
    jenis_tanah = "loam_sand"

  elif radio_bentuk_pita == "Ya" :
    if radio_tanya_panjang == "Panjang pita < 2.5 cm sebelum terputus" :
      if radio_kategori_1 == "Pita terasa kasar (pasir)" :
        jenis_tanah = "sandy_loam"

      elif radio_kategori_1 ==  "Pita tidak terasa kasar (pasir) dan tidak terasa licin" :
        jenis_tanah = "loam"

      elif radio_kategori_1 == "Pita terasa licin" :
        jenis_tanah = "silty_loam"

      else :  
        jenis_tanah = "Tidak diketahui"

    elif radio_tanya_panjang == "Panjang pita 2.5-5 cm sebelum terputus" :
      if radio_kategori_2 == "Pita terasa kasar (pasir)" :
        jenis_tanah = "sandy_clay_loam"

      elif radio_kategori_2 ==  "Pita tidak terasa kasar (pasir) dan tidak terasa licin" :
        jenis_tanah = "clay_loam"

      elif radio_kategori_2 == "Pita terasa licin" :
        jenis_tanah = "silty_clay_loam"

      else :  
        jenis_tanah = "Tidak diketahui"

    elif radio_tanya_panjang == "Panjang pita > 5 cm sebelum terputus" :
      if radio_kategori_3 == "Pita terasa kasar (pasir)" :
        jenis_tanah = "sandy_clay"

      elif radio_kategori_3 ==  "Pita tidak terasa kasar (pasir) dan tidak terasa licin" :
        jenis_tanah = "clay"

      elif radio_kategori_3 == "Pita terasa licin" :
        jenis_tanah = "silty_clay"

      else :  
        jenis_tanah = "Tidak diketahui"

    else :  
      jenis_tanah = "Tidak diketahui"

  else :  
    jenis_tanah = "Tidak diketahui"

else :  
  jenis_tanah = "Tidak diketahui"


def process_string(input_string):
    capitalized_string = input_string.capitalize()
    replaced_string = capitalized_string.replace('_', ' ')

    return replaced_string

def output_result(jenis_tanah):
  if jenis_tanah == "Tidak diketahui" :
    st.header("Jenis tanah ini belum dapat diketahui")
    st.write("Mohon ikuti petunjuk dengan benar sehingga jenis tanah dapat ditampilkan disini")
  else :
    st.header("Jenis tanah ini adalah : " + process_string(jenis_tanah))
    st.write("Tanah ini dapat ditanami tumbuhan seperti " + ', '.join(map(lambda i : "**"+i+"**", jenis_sayur[jenis_tanah])) )

output_result(jenis_tanah)

