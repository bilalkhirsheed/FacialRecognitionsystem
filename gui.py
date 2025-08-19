import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# Initialize emotion model
emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('model.weights.h5')

emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
emoji_dist = {
    0: r"C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\emojis\angry.png",
    1: r"C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\emojis\disgusted.png",
    2: r"C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\emojis\fearful.png",
    3: r"C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\emojis\happy.png",
    4: r"C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\emojis\neutral.png",
    5: r"C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\emojis\sad.png",
    6: r"C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\emojis\surprised.png"
}

# Initialize camera
global cap
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a Tkinter window
root = tk.Tk()
root.title("Facial Emotion Recognition")
root.geometry("900x700")
root.configure(bg='black')

# Title label
title_label = tk.Label(root, text="Facial Emotion Recognition", font=('Arial', 30, 'bold'), fg='#ffffff', bg='black', pady=20)
title_label.pack()

# Create a frame for webcam feed and emoji display side by side
frame = tk.Frame(root, bg='black')
frame.pack(pady=20)

# Create a label for video (webcam)
lmain = tk.Label(frame, padx=50, pady=50)
lmain.grid(row=0, column=0, padx=20)

# Create a label for the emoji
emoji_frame = tk.Frame(frame, bg='black')
emoji_frame.grid(row=0, column=1)

# Create a label for the emoji name
emoji_name_label = tk.Label(emoji_frame, text="Neutral", font=('Arial', 20, 'bold'), fg='#00ff00', bg='black')
emoji_name_label.pack()

# Load a default emoji image
default_emoji_path = emoji_dist[4]  # Neutral emoji as default
default_emoji_image = Image.open(default_emoji_path)
default_emoji_image = default_emoji_image.resize((250, 250), Image.LANCZOS)  # Medium size emoji
default_emoji_photo = ImageTk.PhotoImage(default_emoji_image)
emoji_label = tk.Label(emoji_frame, image=default_emoji_photo, bg='black')
emoji_label.pack()

# Variable to store the last displayed emotion index
last_emotion_index = None

def show_vid():
    global last_emotion_index
    _, frame = cap.read()
    if frame is None:
        print("Error: Frame capture failed.")
        return

    frame = cv2.resize(frame, (600, 500))
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(r'C:\Users\Zubair\Documents\Javascript\ML\Facial Emotion Recognition\haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        (x, y, w, h) = faces[0]  # Only consider the first detected face
        roi_gray_frame = gray_frame[y:y+h, x:x+w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
        prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(prediction))

        # Display emotion text
        cv2.putText(frame, emotion_dict[maxindex], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display emoji and its name
        if last_emotion_index != maxindex:
            last_emotion_index = maxindex
            emoji_path = emoji_dist[maxindex]
            emoji_name_label.config(text=emotion_dict[maxindex])  # Update emoji name label

            try:
                emoji_image = Image.open(emoji_path)
                emoji_image = emoji_image.resize((250, 250), Image.LANCZOS)  # Medium size emoji
                emoji_photo = ImageTk.PhotoImage(emoji_image)

                # Update emoji label
                emoji_label.configure(image=emoji_photo)
                emoji_label.image = emoji_photo  # Keep a reference to avoid garbage collection
            except FileNotFoundError:
                print(f"Error: Emoji file not found: {emoji_path}")
                emoji_label.configure(image=default_emoji_photo)  # Fallback to default emoji
                emoji_label.image = default_emoji_photo
    else:
        # Clear the emoji label if no faces are detected
        emoji_label.configure(image=default_emoji_photo)
        emoji_label.image = default_emoji_photo

    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_vid)

# Start showing video
show_vid()

# Create exit button
exit_button = Button(root, text="Exit", command=root.quit, font=('Arial', 15, 'bold'), fg='white', bg='#ff0000', width=10)
exit_button.pack(pady=20)

root.mainloop()

# Release the camera when done
cap.release()
cv2.destroyAllWindows()
