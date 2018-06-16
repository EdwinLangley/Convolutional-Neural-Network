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


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor


if not os.path.isfile('model.h5'):
  # Initialising the CNN
  classifier = Sequential()

  # Step 1 - Convolution
  classifier.add(Convolution2D(32, ( 3, 3) , input_shape = (64, 64, 3), activation = 'relu'))

  # Step 2 - Pooling
  classifier.add(MaxPooling2D(pool_size = (2, 2)))

  # Adding a second convolutional layer
  classifier.add(Convolution2D(64, (3, 3), activation="relu"))
  classifier.add(MaxPooling2D(pool_size = (2, 2)))

  classifier.add(Convolution2D(128, (3, 3), activation="relu"))
  classifier.add(MaxPooling2D(pool_size = (2, 2)))

  classifier.add(Convolution2D(256, (3, 3), activation="relu"))
  classifier.add(MaxPooling2D(pool_size = (2, 2)))

  # Step 3 - Flattening
  classifier.add(Flatten())

  # Step 4 - Full connection
  classifier.add(Dense(activation="relu", units=128))
  classifier.add(Dense(activation="softmax", units=10))

  # Compiling the CNN
  classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

  # Part 2 - Fitting the CNN to the images

  from keras.preprocessing.image import ImageDataGenerator

  train_datagen = ImageDataGenerator(samplewise_center=True,
                                    samplewise_std_normalization=True,
                                    rescale = 1./255,
                                    shear_range = 0.2,
                                    zoom_range = 0.2,
                                    horizontal_flip = True)

  test_datagen = ImageDataGenerator(samplewise_center=True,
                                    samplewise_std_normalization=True,
                                    rescale = 1./255)

  training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                   target_size = (64, 64),
                                                   batch_size = 16,
                                                   class_mode = 'sparse')

  test_set = test_datagen.flow_from_directory('dataset/test_set',
                                              target_size = (64, 64),
                                              batch_size = 16,
                                              class_mode = 'sparse')

  classifier.fit_generator(
                           training_set,
                           steps_per_epoch = 80,
                           epochs = 25,
                           validation_data = test_set,
                           workers=100,
                           max_queue_size = 100,
                           validation_steps = 10,
                           verbose=1,
                           use_multiprocessing=False)

  classifier.save('model.h5')

else:
  classifier = load_model('model.h5')
 

img_path = 'dataset/new/3.jpg'

new_image = load_image(img_path)

# check prediction
pred = classifier.predict(new_image)

print(pred)


labels = ['Danaus plexippus', 'Heliconius charitonius', 'Heliconius erato', 'Junonia coenia', 'Lycaena phlaeas', 'Nymphalis antiopa', 'Papilio cresphontes', 'Pieris rapae',
         'Vanessa atalanta', 'Vanessa cardui']

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'cyan', 'crimson', 'pink', 'sienna', 'olive', 'lime']

patches, texts = plt.pie(pred[0], colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()