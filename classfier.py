from tensorflow.keras.models import load_model
import pickle
import os
import numpy as np
from PIL import Image, ImageOps

def classify(cell_image):

    model = load_model("malaria_predictor.h5")

    data = np.ndarray(shape=(1, 150, 150, 3), dtype=np.float32)
    image = cell_image
    size = (150, 150)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)

    norm_image = (image_array.astype(np.float32) / 127.0) - 1

    data[0] = norm_image

    pred = model.predict(data)

    del model

    return_data = { }

    for i in pred:
        if (i[0] > i[1]):

            return_data = {
                "infected": 1,
                "uninfected": 0,
                "probability": f"{i[0] * 100}%"
            }

        else:
             return_data = {
                "infected": 0,
                "uninfected": 1,
                "probability": f"{ i[1] * 100}%"
            }

    return return_data

    