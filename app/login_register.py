import streamlit as st
import database as db
import os
import re

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)

def is_valid_password(password):
    return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$.!%*#?&]{8,}$", password)

st.title("🎬 Film Recommendation System")

menu_choice = st.sidebar.radio("Menu", ["Login", "Register"])

if menu_choice == "Login":
    st.subheader("Login")
    username = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username and password:
            if is_valid_email(username):
                if db.check_exist(username,password):
                    os.system("streamlit run app\streamlit_app.py")
                    st.success(f"Welcome, {username}!")
                  
                else:
                    st.error("this user is not found")
            else:
                st.error("Username and password are not correct.")
        else:
            st.error("Invalid username or password.")
            

elif menu_choice == "Register":
    st.header("Register Page")
    email = st.text_input("Email")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    register_button = st.button("Register")

    if register_button:
        if not is_valid_email(email):
            st.error("Invalid email format. Please enter a valid email.")
        elif not is_valid_password(new_password):
            st.error("Password must be at least 8 characters, include an uppercase letter, a lowercase letter, and a number.")
        else:
            st.success("Registration successful. You can now login.")
            db.add_elemet(new_username, new_password)
            os.system("streamlit run app\streamlit_app.py")
