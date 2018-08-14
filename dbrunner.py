from cnn import NNet
from databasehelper import database_object
import time
import threading

class DB_Runner():

    def __init__(self):
        self.db = database_object()
        self.nnet = NNet()
        self.nnet.load_model("Models/Models/epoch100spe200.h5")
        self.runner()        

    def runner(self):
        cur = self.db.get_all_entries()
        for i in range(0,len(cur)):
            print(cur[i]['Outcome'])
            if cur[i]['Outcome'] == 'Not Yet Classified':
                imgname = cur[i]['FileName']
                self.nnet.make_prediction_on_model("static/img/"+imgname)
                self.nnet.make_pie_chart(imgname)
                self.db.set_new_outcome('output_'+ imgname +'.png',cur[i]['Time'])


if __name__ == '__main__':
    dbrun = DB_Runner()
                




