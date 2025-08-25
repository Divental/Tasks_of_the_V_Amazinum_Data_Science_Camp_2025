import os
from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from PIL import Image
import numpy as np

MODEL_PATH = 'mnist_model.h5'
app = FastAPI()

# Якщо файл моделі не існує, створимо і навчимо її
if not os.path.exists(MODEL_PATH):
    print("Training model...")
    (x_train, y_train), _ = mnist.load_data()
    x_train = x_train / 255.0

    model = Sequential([
        Flatten(input_shape=(28,28)),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=1)  # 1 епоха для швидкого запуску
    model.save(MODEL_PATH)
else:
    model = load_model(MODEL_PATH)

@app.get("/")
def root():
    return {"message": "MNIST CV API is running"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    img = Image.open(file.file).convert('L').resize((28,28))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1,28,28)
    prediction = model.predict(img_array)
    predicted_digit = int(np.argmax(prediction))
    return {"predicted_digit": predicted_digit}
