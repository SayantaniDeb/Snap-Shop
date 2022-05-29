import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from multiapp import MultiApp
from apps import home, upload, about # import your app modules here
import os

#change title and favicon
st.set_page_config(page_title="Snap&Shop", page_icon="🛒", layout="wide")

app = MultiApp()
#initialize lottie animation
def load_lottieurl(url: str):
      r=requests.get(url)
      if r.status_code != 200:
          return None
      return r.json()
#--load assets---
with st.container():
  
    img,title=st.columns((1,2))
    with img:
      lottie_shop=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_o02kdakv.json")
      st_lottie(lottie_shop,key="shop",width=350)
    with title:
      image = Image.open('./images/4.png')
      st.image(image,width=230)
    

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Upload", upload.app)
app.add_app("About", about.app)
# The main app
app.run()
# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 4rem;
                    padding-right: 4rem;
                }
               .css-1d391kg {
                    padding-top: 8rem;
                    padding-right: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



