import numpy as np
from tagger import Tagger
import scipy.misc
from colours import *


class FilterGenerator:

    def __init__(self,description_list):
        self.description_list = description_list
    
    def find_background_colour(self):
        for element in self.description_list:
            if 'wings'in element:
                self.background_description = element
        
        self.background_colour = self.background_description.replace(' ','').replace('wings','')
        self.background_colour = self.set_colour(self.background_colour)

        print(self.background_colour)

    def set_background(self, colour):
        self.img = np.zeros([7,7,3],dtype=np.uint8)

        for i in range(0,7):
            for j in range(0,7):
                self.img[i][j] = colour

    
    def find_fore_features(self):
        for element in self.description_list:

            if 'spot'in element:
                self.draw_spot(element)
            elif 'stripe' in element:
                self.draw_stripe(element)
            elif 'fringe' in element:
                self.draw_fringe(element)
            

    def set_colour(self,phrase):
        colour_text = phrase

        if colour_text == 'white':
            colour = WHITES
        elif colour_text == 'blue':
            colour = BLUES
        elif colour_text == 'green':
            colour = GREENS
        elif colour_text == 'red':
            colour = REDS
        elif colour_text == 'purple':
            colour = PURPLES
        elif colour_text == 'brown':
            colour = BROWNS
        elif colour_text == 'black':
            colour = BLACKS
        elif colour_text == 'orange':
            colour = ORANGES
        elif colour_text == 'yellow':
            colour = YELLOWS
        else:
            colour = [[255,255,255]]

        return colour

    def draw_spot(self,spot_call):
        
        colour_text = spot_call.replace(" ","").replace("spots","").replace("spot","")
        colour = self.set_colour(colour_text)        

        for l in range(0,len(self.background_colour)):
            
            self.set_background(self.background_colour[l])

            colour_len = len(colour)

            for k in range(0,colour_len):
                self.img[0][2:5] = colour[k]
                self.img[2][0] = colour[k]
                self.img[3][0] = colour[k]
                self.img[4][0] = colour[k]
                self.img[6][2:5] = colour[k]
                self.img[2][6] = colour[k]
                self.img[3][6] = colour[k]
                self.img[4][6] = colour[k]
                self.img[1][1] = colour[k]
                self.img[5][1] = colour[k]
                self.img[1][5] = colour[k]
                self.img[5][5] = colour[k]

                for i in range(1,6):
                    for j in range(1,6):
                        self.img[i][j] = colour[k]

                scipy.misc.toimage(self.img, cmin=0.0, cmax=255.0).save('spots/spot' + str(l) + str(k) + '.png')

    def draw_stripe(self,stripe_call):
        colour_text = stripe_call.replace(" ","").replace("stripes","").replace("stripe","")
        colour = self.set_colour(colour_text)        

        for l in range(0,len(self.background_colour)):
            
            self.set_background(self.background_colour[l])

            colour_len = len(colour)

            for k in range(0,colour_len):
                for i in range(2,4):
                    for j in range(1,6):
                        self.img[i][j] = colour[k]
                
                self.img[3][0] = colour[k]
                self.img[2][6] = colour[k]

                scipy.misc.toimage(self.img, cmin=0.0, cmax=255.0).save('stripes/stripe'+ str(l) + str(k) +'.png')

    def draw_fringe(self,fringe_call):
        
        colour_text = fringe_call.replace(" ","").replace("fringes","").replace("fringe","")
        colour = self.set_colour(colour_text)        

        for l in range(0,len(self.background_colour)):
            self.set_background(self.background_colour[l])

            colour_len = len(colour)
            for k in range(0,colour_len):
                self.img[1][0] = colour[k]
                self.img[1][1] = colour[k]
                self.img[1][2] = colour[k]
                self.img[2][3] = colour[k]
                self.img[3][4] = colour[k]
                self.img[4][5] = colour[k]
                self.img[5][5] = colour[k]
                self.img[6][5] = colour[k]

                for r in range (0,4):
                    copied = np.rot90(self.img, r)
                    scipy.misc.toimage(copied, cmin=0.0, cmax=255.0).save('fringes/fringe'+ str(r)+str(l) + str(k) + '.png')

if __name__ == '__main__':
    newtagger = Tagger("This is a new , test sentence. The butterfly in question has a set of blue wings, black stripes and brown fringes .")
    newtagger.tokenise_text()
    newtagger.tag_text()
    words = newtagger.identify_uses()
    filtergen = FilterGenerator(words)
    filtergen.find_background_colour()
    filtergen.find_fore_features()
    