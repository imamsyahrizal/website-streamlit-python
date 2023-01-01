import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Set web page
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout='wide')

# ---- FUNCTION ----
# load lottie from url
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
local_css("style/style.css")


# --- LOAD ASSETS
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_kkn = Image.open("images/kkn.png")
img_BrainMRI = Image.open("images/BrainMRI.png")


# --- HEADER SECTION --- 
with st.container():
    st.subheader("Hi, I am Imam Syahrizal :wave:")
    st.title("A Freshgraduate Electrical Engineering")
    st.write("I was graduate in august 2018. I have several experience during collage. Machine Learning experience I Get during finish my Final Assessmen")
    st.write("[Learn More >](https://github.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---") # make line
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """Now I am try to make website page from python code using 
            streamlit library. I think it is cool tool because we can make
            website in python language..."""
        )
    with right_column:
        st_lottie(lottie_coding, key='coding')

# --- PROJECT
with st.container():
    st.write('---')
    st.header("My Projects")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
        st.image(img_kkn)
    with text_column:
        st.subheader("Sistem monitoring kualitas air kolam ikan")
        st.write(
            """
            Proyek KKN PPM UGM 2021 di Desa Nanggulan. Sistem untuk memonitoring
            kualitas air kolam ikan berbasis IoT. Dashboard menggunakan Grafana. 
            MQTT menggunakna Mosquitto MQTT. NodeRed digunakan untuk menghubungkan 
            MQTT dengan database. Data base menggunakna InfluxDB. \n
            Perangkat Utama berupa ESP32."""
        )
        st.markdown("[Code here](https://github.com/imamsyahrizal/KKN-Nanggulan)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_BrainMRI)
    with text_column:
        st.subheader("BrainMRI")
        st.write(
            """
            Klasifikasi Kanker otak dengan 7 model CNN

            Model :

            MobileNetV2
            MobileNetV3
            ResNet50
            ResNet50v2
            ResNet152
            ResNet152v2
            Xception
            semua menggunakan pre-train model"""
        )
        st.markdown("[Code here](https://github.com/imamsyahrizal/BrainMRI)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
