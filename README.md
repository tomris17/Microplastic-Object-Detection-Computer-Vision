# Microplastic Object Detection & Visualization Project

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Visualization-green.svg)](https://opencv.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains an exploratory image processing project that reads microplastic image files alongside their corresponding bounding box annotations from CSV files and visualizes them using OpenCV.

---

## Dataset Notice
*Note: The dataset directory (`train/`) containing images and `_annotations.csv` is structured for object detection tasks.*

---

## Project Workflow
1. **Annotation Loading**: Reading object detection bounding boxes from `_annotations.csv` using Pandas.
2. **Image Processing**: Reading microplastic image files via OpenCV (`cv2`).
3. **Bounding Box Rendering**: Drawing rectangular detection boxes onto the images based on coordinate variables (`xmin`, `ymin`, `xmax`, `ymax`).
4. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/microplastic-object-detection.git](https://github.com/YOUR_USERNAME/microplastic-object-detection.git)
   cd microplastic-object-detection
