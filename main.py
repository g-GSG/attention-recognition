import cv2
from model import FacialExpressionModel
import numpy as np

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
result = []


class VideoCamera(object):

    def calculate_emotion(self):
        dictionary = {}

        count, itm = 0, ''
        for item in reversed(result):
            dictionary[item] = dictionary.get(item, 0) + 1
            if dictionary[item] >= count:
                count, itm = dictionary[item], item
        return (itm)

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        print("A expressão mais predominante foi: ", self.calculate_emotion())
        self.video.release()

    # retorna os frames da camera junto do quadrado delimitador da face e a predição da emoção
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y + h, x:x + w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
            result.append(pred)
            print(pred)

            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(fr, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return fr


def gen(camera):
    while True:
        frame = camera.get_frame()
        cv2.imshow('Reconhecedor de Expressoes Faciais', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


gen(VideoCamera())