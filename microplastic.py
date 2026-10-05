import os
import cv2
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Microplastic Object Detection App", layout="centered")

st.title("Microplastic Object Detection & Visualization App")
st.write(
    "Bu uygulama, mikroplastik görüntüleri ve CSV dosyasındaki koordinat (bounding box) etiketlerini yükleyerek görselleştirir."
)

@st.cache_data
def load_data():
    return pd.read_csv("train/_annotations.csv")

try:
    df = load_data()
    st.subheader("Annotations (Etiketler) Veri Seti On Izleme")
    st.dataframe(df.head())

    st.subheader("Gorsellestirme Paneli")
    unique_files = df["filename"].unique()
    selected_file = st.selectbox("Bir Gorsel Dosyasi Secin", unique_files)

    if selected_file:
        image_dir = "train"
        image_path = os.path.join(image_dir, selected_file)
        
        if os.path.exists(image_path):
            img = cv2.imread(image_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Secilen dosyaya ait koordinatlari filtreleme
            file_annotations = df[df["filename"] == selected_file]
            
            for _, row in file_annotations.iterrows():
                xmin, ymin, xmax, ymax = int(row["xmin"]), int(row["ymin"]), int(row["xmax"]), int(row["ymax"])
                cv2.rectangle(img_rgb, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
            
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(img_rgb)
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning(f"Gorsel dosyasi bulunamadi: {image_path}")

except Exception as e:
    st.error(f"Veri yuklenirken veya gorsellestirilirken bir hata olustu: {e}")