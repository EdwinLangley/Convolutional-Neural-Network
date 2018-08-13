from PIL import Image
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
import os
from keras.preprocessing.image import ImageDataGenerator
from keras.backend import clear_session
from keras.utils import plot_model


class NNet:

    def __init__(self):
        self.classifier = Sequential()
        self.possible_to_run = False


    def conv_pool_layers(self):
        self.classifier.add(Convolution2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

        # Step 2 - Pooling
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))

        # Adding a second convolutional layer
        self.classifier.add(Convolution2D(64, (3, 3), activation="relu"))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))

        self.classifier.add(Convolution2D(128, (3, 3), activation="relu"))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))

        self.classifier.add(Convolution2D(256, (3, 3), activation="relu"))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))


    def flattening(self):
        self.classifier.add(Flatten())


    def full_connection(self):
        # Step 4 - Full connection
        self.classifier.add(Dense(activation="relu", units=128))
        self.classifier.add(Dense(activation="softmax", units=10))

        # Compiling the CNN
        self.classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


    def gen_train_test(self):
        self.train_datagen = ImageDataGenerator(
            rescale=1. / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

        self.test_datagen = ImageDataGenerator(
            rescale=1. / 255)

        self.training_set = self.train_datagen.flow_from_directory('dataset/training_data',
                                                         target_size=(64, 64),
                                                         batch_size=16,
                                                         class_mode='categorical')

        self.test_set = self.test_datagen.flow_from_directory('dataset/testing_data',
                                                    target_size=(64, 64),
                                                    batch_size=16,
                                                    class_mode='categorical')


    def save_model(self, path):
        self.classifier.save(path)

    def load_model(self, path):
        self.classifier = load_model(path)
        self.possible_to_run = True


    def fit_data_to_model(self,numEpoch):
        self.classifier.fit_generator(
            self.training_set,
            steps_per_epoch=80,
            epochs=numEpoch,
            validation_data=self.test_set,
            workers=100,
            max_queue_size=100,
            validation_steps=10,
            verbose=1,
            use_multiprocessing=False)
        self.possible_to_run = True


    def make_prediction_on_model(self, path):

        self.new_image = self.load_image(path)

        # check prediction
        self.pred = self.classifier.predict(self.new_image)

        print(self.pred)


    def make_pie_chart(self,filename):
        self.labels = ['Danaus plexippus', 'Heliconius charitonius', 'Heliconius erato', 'Junonia coenia', 'Lycaena phlaeas',
                  'Nymphalis antiopa', 'Papilio cresphontes', 'Pieris rapae',
                  'Vanessa atalanta', 'Vanessa cardui']

        self.colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'cyan', 'crimson', 'pink', 'sienna', 'olive',
                  'lime']

        self.patches, texts = plt.pie(self.pred[0], colors=self.colors, shadow=True, startangle=90)
        plt.legend(self.patches, self.labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('static/results/output_'+ filename +'.png',bbox_inches='tight')

    def load_image(self, img_path, show=False):
        img = image.load_img(img_path, target_size=(64, 64))
        img_tensor = image.img_to_array(img)  # (height, width, channels)
        img_tensor = np.expand_dims(img_tensor,
                                        axis=0)  # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
        img_tensor /= 255.  # imshow expects values in the range [0, 1]

        if show:
            plt.imshow(img_tensor[0])
            plt.axis('off')
            plt.show()

        return img_tensor

    def run_train(self,numEpoch,path):
        self.conv_pool_layers()
        self.flattening()
        self.full_connection()
        self.gen_train_test()
        self.fit_data_to_model(numEpoch)
        self.save_model("Models/"+path+".h5")
        plot_model(self.classifier, to_file="model.png")
        clear_session()
        
        

if __name__ == '__main__':
    nnet = NNet()
    # nnet.make_prediction_on_model("3.jpg")
    # nnet.run_train()