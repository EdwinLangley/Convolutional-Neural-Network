from cnn import NNet
from databasehelper import database_object
import time
import threading
from pydarknet import Detector, Image
import cv2
import os
import numpy as np

class DB_Runner():

    def __init__(self):
        self.db = database_object()
        self.nnet = NNet()
        self.nnet.load_model("Models/Models/epoch100spe200.h5")
        self.runner()        

    def runner(self):
        cur = self.db.get_all_entries()
        
        if len(cur) > 0:
            for i in range(0,len(cur)):
                print(cur[i]['Outcome'])
                if cur[i]['Outcome'] == 'Not Yet Classified':
                    imgname = cur[i]['FileName']
                    prediction = self.nnet.make_prediction_on_model("static/img/"+imgname)
                    multiply = self.feature_predict(imgname)
                    array_sum = 0
                    for j in range(0,10):
                        prediction[0][j] = prediction[0][j] * multiply[j]
                        array_sum += prediction[0][j]
                    array_total = 0
                    for k in range(0,10):
                        prediction[0][k] /= array_sum
                        array_total += prediction[0][k]
                    print("now")
                    print(prediction)
                    print(array_total)
                    self.nnet.make_pie_chart(imgname)
                    self.db.set_new_outcome('output_'+ imgname +'.png',cur[i]['Time'])
                    self.db.set_new_features(imgname,cur[i]['Time'])

    def feature_predict(self,imgpath):
        net = Detector(bytes("custom/yolov3-tiny.cfg", encoding="utf-8"), bytes("custom/yolov3-tiny_400.weights", encoding="utf-8"),0, bytes("cfg/coco.data",encoding="utf-8"))

        multiplier_array = [1,1,1,1,1,1,1,1,1,1]
        print(multiplier_array)

        img = cv2.imread("static/img/"+imgpath,cv2.COLOR_BGR2RGB)
        img2 = Image(img)
        results = net.detect(img2,0.4)

        if "Black Spots on Orange" in str(results):
            print("Black Spots found in input image, creating bias for class")
            multiplier_array[4] = 1.5
        if "Top White Fringe" in str(results):
            print("Top White Fringe found in input image, creating bias for class")
            multiplier_array[4] = 1.5

        for cat, score, bounds in results:
            x, y, w, h = bounds
            cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)
            cv2.putText(img,str(cat.decode("utf-8")),(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))

        cv2.imwrite('static/features/'+imgpath,img)
        return multiplier_array


if __name__ == '__main__':
    dbrun = DB_Runner()
                




