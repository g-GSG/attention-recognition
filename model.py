from tensorflow.keras.models import model_from_json
import numpy as np

import tensorflow as tf


class FacialExpressionModel(object):

    EMOTIONS_LIST = ["Raiva", "Desgosto",
                    "Medo", "Feliz",
                    "Neutro", "Triste",
                    "Surpreso"]

    def __init__(self, model_json_file, model_weights_file):
        # Carrega o modelo a partir do arquivo JSON
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        # Carrega os pesos no novo modelo
        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model.make_predict_function()

    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]