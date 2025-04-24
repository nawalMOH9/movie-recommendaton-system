import streamlit as st
import os
with st.sidebar: 
    st.title('🎬 Film Recommendation System')
    st.info('Enter your preferences and get Film recommendations instantly!')

st.title("🎬 Film Recommendation System'")

c1,c2 =st.columns(2)


with c1:
    st.text("Login if you aredy have an acount")
    if st.button("LOGIN"):
        
        st.success("Button clicked!")
        os.system("streamlit run app\login_register.py")

with c2:
    st.text("If Don't have an acount ")
    if st.button("REGITER"):
        
        st.success("Button clicked!")
        os.system("streamlit run app\login_register.py")