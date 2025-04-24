import streamlit as st
import requests
import pandas as pd
import json 
st.title("🎬 Film Recommendation System")
st.write("Enter your preferences and get Film recommendations instantly!")


year = st.number_input("Select Year", min_value=2020, max_value=2024, value=2020)
duration = st.slider("Duration (minutes)", min_value=60, max_value=240, value=150)
mpa = st.selectbox("MPA Rating", ['Unknown', 'R', 'Not Rated', 'TV-MA', 'PG-13', 'PG', 'TV-14',
                                  'Unrated', 'TV-PG', 'TV-G', 'G', '18+', 'TV-Y7-FV', 'TV-Y7', '16+',
                                   'Approved', '13+', 'NC-17', 'TV-Y'])
rating = st.slider("Minimum Rating", min_value=0.0, max_value=10.0, value=8.5, step=0.1)

recommendations=None
if st.button("Get Recommendations 🎥"):
    api_url = "http://127.0.0.1:5000/recommend"  
    payload = {
        "Year": year,
        "Duration": duration,
        "MPA": mpa,
        "Rating": rating
    }

    try:
        response = requests.post(api_url, json=payload, timeout=10)  
        
        

        if response.status_code == 200:
            try:
                recommendations = json.loads(response.text)['result']
                if not recommendations:
                    st.warning("⚠️ API returned an empty list. Try different filters.")
            except requests.exceptions.JSONDecodeError:
                st.error("❌ Error: API returned an invalid JSON response.")
        else:
            st.error(f"❌ API Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection Error: {e}")

    if recommendations:
        df = pd.DataFrame(recommendations)
        df = df.drop(columns=["Unnamed: 0", "index"], errors="ignore")  
        df["Movie Link"] = df["Movie Link"].apply(lambda x: f"[IMDb Link]({x})")  
        st.subheader("🎬 Movie Details")
        
        for i, movie in enumerate(recommendations[:5]): 
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    d= requests.get(f"https://www.omdbapi.com/?i=tt3896198&apikey=5f1f1744&t={movie['Title']}",timeout=105) 
                    film_info=json.loads(d.text)
                    print(film_info['Poster'])
                    poster_url = film_info.get("Poster", "N/A")
                    if poster_url and poster_url != "N/A":
                        st.image(poster_url, width=150)
                with col2:
                    st.markdown(f"**Title:** {movie['Title']}")
                    st.markdown(f"**Year:** {movie['Year']}")
                    st.markdown(f"**Duration:** {movie['Duration']}")
                    st.markdown(f"**MPA Rating:** {movie['MPA']}")
                    st.markdown(f"**Rating:** ⭐ {movie['Rating']}")
                    st.markdown(f"[IMDb Link]({movie['Movie Link']})", unsafe_allow_html=True)
            st.write("---")  

