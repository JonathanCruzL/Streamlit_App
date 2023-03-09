import cv2
import streamlit as st
import streamlit_webrtc as webrtc
from streamlit_webrtc import webrtc_streamer as webStreamer

def app():
    st.title("Aplicación de cámara en tiempo real")

    webrtc_streamer = webStreamer(
        key="camera",
        type="video",
        source=webrtc.VideoTransformerBase(
            fps=24,
            transform_func=lambda frame: cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),
        ),
    )

    if not webrtc_streamer:
        st.warning("No se ha podido acceder a la cámara.")
        return

    image = webrtc_streamer.image_in_color
    st.image(image, use_column_width=True)

if __name__ == "__main__":
    app()
