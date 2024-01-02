import streamlit as st
from cyk import CYK
cek = 'cek'        

def GUI():
    n = 0
    # k = 0
    st.set_page_config(page_title="Kelompok 4", layout="wide")    
    st.title("Tata :red[Bahasa] Indonesia")
    st.write("---")   

    left_column, right_column = st.columns(2)

    with left_column:
        sentence = st.text_input("Masukan Kalimat", placeholder="itu adalah kambing")
        button_click = 0
        if st.button('Cek Aturan'):
            print(button_click)
            button_click = 1
            kata = sentence.split()
            n = len(kata)
            print(n)
            for i in range(n):
                kata[i] = kata[i].lower()
            if n != 0:
                T = CYK(kata, n)
                    

    with right_column:
        if cek == 'cek' and button_click == 0:
            st.write("# Masukan kalimat")
        elif n == 0 :
            st.write("# Kolom tidak boleh :red[Kosong]") 
        elif cek == 'fek':
            st.write("# Kalimat :red[Tidak Valid]")
            # st.write(T)
        else:
            st.write("# Kalimat :green[Valid]") 
            # st.write(T);
            st.balloons()
            
    st.write("---")
