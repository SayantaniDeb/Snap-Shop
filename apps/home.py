import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def app():
    
    st.title('What is Snap&Shop?')
    with st.spinner('Loading...') :
        st.write("Snap&Shop is a visual search engine that helps you find the best clothes for your daily look. It is a free and open-source project, and you can use it for free. You can find more information about Snap&Shop in the [README](https://github.com/SayantaniDeb/Snap-Shop/blob/master/README.md).")
    
    #video
    video_file = open('./images/demo.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    def load_lottieurl(url: str):
      r=requests.get(url)
      if r.status_code != 200:
          return None
      return r.json()

    st.title('How it works?')
#--load assets---

    
    lottie_search=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_svuxrlnw.json")
    lottie_biased=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_itqzcfzd.json")
    lottie_pic=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_ydcu5a0y.json")
    #--Header section--
    with st.container():
        left_column,middle_column,right_column=st.columns(3)
        with left_column:
            image = Image.open('./images/1.png')
            st.image(image,width=230)
        with middle_column:
            image = Image.open('./images/2.png')
            st.image(image,width=230)
        with right_column:
            image = Image.open('./images/3.png')
            st.image(image,width=230)
    st.write("---")    
    st.title('Advantages')  
    with st.container():
        col1,col2=st.columns((3,1))
        with col1:
            st.subheader("Find Clothes By Photo")
            st.write("Just upload a photo of the outfit you love and get a list with the exact or similar items available")
        with col2:
            st_lottie(lottie_search,key="search",width=200)
    st.write("---")
    with st.container():
        col3,col4=st.columns((3,1))
        with col4:
            st_lottie(lottie_biased,key="biased",width=200)
        with col3:
            st.subheader("Unbiased search results")
            st.write("We use a machine learning model to find the most similar items to your search.We rank the items based solely on visual similarity as we get it from our AI platform.")
    st.write("---")
    with st.container():
        col5,col6=st.columns((3,1))
        with col5:
            
            st.subheader("Use pictures instead of words")
            st.write("Not sure how to describe what you’re looking for? The image shows everything just as it is, without effort.")
        with col6:
            st_lottie(lottie_pic,key="pic",width=200)
        

    