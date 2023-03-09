import cv2
import streamlit as st

def main():
    st.title("Aplicación de cámara en tiempo real")
    run_camera = st.button("Iniciar cámara")
    video_display = st.empty()

    if run_camera:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            video_display.image(frame)
        cap.release()

if __name__ == "__main__":
    main()
