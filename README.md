# Facial Recognition-Based Attendance Management System

## Overview

This project implements a robust facial recognition system to automate attendance tracking using real-time video feed analysis. It employs classical computer vision techniques alongside machine learning models to detect and recognize faces with high accuracy. The system captures, processes, and identifies student faces in live video streams to mark attendance efficiently and reliably.

## Main Features

- **Face Detection:** Utilizes Haar Cascade classifiers to detect faces in real-time from webcam video streams.
- **Face Recognition:** Implements LBPH (Local Binary Patterns Histograms) algorithm to uniquely identify students by matching detected faces against a trained facial dataset.
- **Preprocessing:** Enhances input images by converting frames to grayscale and applying contrast enhancement to improve recognition accuracy, especially in low-light conditions.
- **Face Cropping & Resizing:** Extracts face regions and normalizes them for consistent recognition.
- **Visual Feedback:** Displays bounding boxes and student names on the live video feed for clear and immediate identification.
- **Data Collection & Model Training:** Supports capturing multiple facial images per new student, storing structured data, and retraining the LBPH model for improved recognition performance.
- **Attendance Visualization:** Integrates with **Power BI** to generate interactive dashboards and visual analytics for attendance trends, helping administrators analyze data effectively.

## Tech Stack

- **Programming Language:** Python  
- **Face Detection:** OpenCV Haar Cascade Classifiers  
- **Face Recognition:** OpenCV LBPH Face Recognizer  
- **Image Processing:** OpenCV (Grayscale conversion, histogram equalization)  
- **Data Visualization:** Power BI (for attendance dashboards and insights)  
- **Data Storage:** Structured folder-based image datasets and attendance records  
- **Hardware:** Standard webcam for real-time video feed

  ## Results

- Real-time face detection and recognition with bounding box visualization.
- High recognition accuracy under varied lighting conditions due to preprocessing.
- Automated attendance marking with minimal manual intervention.
- Interactive and insightful attendance dashboards created using Power BI.
- Demonstrated system robustness and reliability in live environments.

## Conclusion

By integrating real-time face detection and LBPH-based recognition, this system automates attendance tracking with accuracy and ease. The image preprocessing steps enhance recognition reliability, making it suitable for diverse environments. Coupled with Power BI visualizations, the project empowers administrators with actionable insights into attendance patterns, enabling data-driven decisions. Its lightweight and accessible design make it ideal for deployment even in resource-limited institutions, moving towards smarter, contactless attendance management.

