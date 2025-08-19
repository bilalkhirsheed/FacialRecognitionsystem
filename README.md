
# 🎭 **Facial Emotion Recognition System** 🤖

Welcome to the **Facial Emotion Recognition System**! This project uses cutting-edge **deep learning** techniques to recognize and display emotions from facial expressions in real-time. Using **OpenCV** and **Keras**, this system processes live webcam feed, classifies facial expressions, and displays corresponding **emojis**. 

---

## 🚀 **Features** ✨

- **🖼️ Real-time Webcam Feed**: Capture and process your webcam in real-time for emotion recognition.
- **🧠 Deep Learning Model**: Classifies facial expressions into seven emotions using a **Convolutional Neural Network (CNN)**.
- **😀 Emoji Display**: For each recognized emotion, a corresponding emoji is displayed on the screen.
- **🖥️ User Interface**: Simple **Tkinter GUI** that shows live video and emotion results clearly.
- **⚡ Continuous Updates**: The emotion recognition updates automatically as long as the webcam is running.
- **🌍 Multi-Platform Support**: Works on Windows, macOS, and Linux.

---

## 📸 **How It Works** 🤖

1. **🖥️ Webcam Feed**: Capture video feed in real-time using OpenCV.
2. **🤔 Emotion Detection**: The system detects faces and predicts emotions using a **pretrained CNN model**.
3. **💡 Real-Time Emotion**: Displays the detected emotion with a corresponding emoji.
4. **🔄 Continuous Recognition**: Keeps recognizing and updating emotions in real-time until the program is stopped.

---

## 📥 **Installation Guide** 🔧

### 🔑 **Prerequisites**

Before running the system, you’ll need the following:

- **Python 3.x** 🐍
- **OpenCV** 🎥
- **TensorFlow/Keras** 🧠
- **Pillow (PIL)** 🖼️
- **NumPy** 🔢

To install the dependencies, use the following command:

```bash
pip install opencv-python tensorflow pillow numpy
```

### 🔄 **Clone the Repository** 💻

Clone this repository to your local machine:

```bash
git clone https://github.com/ZubairZubii/Facial-Emotion-Recognition.git
```

### ▶️ **Run the Program** 🎬

Navigate to the project folder and run the program:

```bash
python emotion_recognition.py
```

Make sure your **webcam** is connected and working!

---

## 🖼️ **Emojis & Model** 🎨

The system uses emojis to represent the detected emotions. The images can be found in the `emojis` folder:

- 😨 **Fearful**: fearful.png
- ![Screenshot 2025-01-01 201152](https://github.com/user-attachments/assets/94320200-c9fc-4004-b88d-2313147f25cb)
 
- 😄 **Happy**: happy.png
- ![Screenshot 2025-01-01 201048](https://github.com/user-attachments/assets/e2e65742-73dc-42d1-ad72-c2646715d6b2)
 
- 😐 **Neutral**: neutral.png
- ![Screenshot 2025-01-01 201015](https://github.com/user-attachments/assets/585c25bf-732b-4f1c-b060-4962e38d70e1)

- 😞 **Sad**: sad.png
- ![Screenshot 2025-01-01 201333](https://github.com/user-attachments/assets/d294cc8c-33ab-40d5-aa72-49e3ca8076f7)

- 😲 **Surprised**: surprised.png
- ![Screenshot 2025-01-01 201420](https://github.com/user-attachments/assets/3f7d56f6-c345-476c-886c-3c115c42e029)

Make sure to **update the paths** for both the emojis and model weights in the code.

---


## 🔄 **Model Weights** 🧑‍🏫

The system uses **CNN-based model weights** for emotion classification. The model architecture is based on **Keras** and is trained to classify **seven emotions**.

- **Model Weights**: `model.weights.h5`
- **Pretrained Model**: Available within the repository.

You can **retrain** the model or update it as needed, but ensure the architecture is consistent with the current one.

---

## 🌱 **Enhancements & Ideas** 💡

Here are some potential improvements you can implement:

- **👥 Multi-Face Detection**: Extend the system to detect and classify emotions for **multiple faces** in real-time.
- **☁️ Cloud Integration**: Integrate with cloud APIs to perform emotion analysis on **uploaded images**.
- **🖥️ Cross-Platform Compatibility**: Ensure the system runs seamlessly across all operating systems (Windows, macOS, Linux).
- **📊 Emotion Analytics**: Display **graphical representations** of detected emotions over time.

---

## 👨‍💻 **Developers** 💻

- **Zubair Ali** - AI Engineer at [FAST University](https://www.fast.edu.pk) 🚀

Feel free to open an **issue** or submit a **pull request** if you want to contribute!

---

## 📜 **License** 📄

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for more details.

---

✨ **Enjoy using the Facial Emotion Recognition System!** ✨

---

### **Contact Me** 📬

- **Email**: zs970120@gmail.com 📧
- **GitHub**: [ZubairZubii](https://github.com/ZubairZubii) 🐙
- **LinkedIn**: [Zubair Ali](https://www.linkedin.com/in/zubair-ali/) 🔗

---

This enhanced README file is full of icons and engaging formatting to help make your project stand out! Let me know if you'd like to tweak anything else!
