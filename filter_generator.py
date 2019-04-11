import numpy as np
from tagger import Tagger
import scipy.misc


class FilterGenerator:

    def __init__(self,description_list):
        self.description_list = description_list
    
    def find_background_colour(self):
        for element in self.description_list:
            if 'wings'in element:
                self.background_description = element
        
        self.background_colour = self.background_description.replace(' ','').replace('wings','')
        print(self.background_colour)

    def set_background(self):
        self.img = np.zeros([7,7,3],dtype=np.uint8)

        for i in range(0,7):
            for j in range(0,7):
                self.img[i][j] = [0,0,255]

    
    def find_fore_features(self):
        for element in self.description_list:

            if 'spot'in element:
                self.draw_spot(element)
            


    def draw_spot(self,spot_call):

        colour_text = spot_call.replace(" ","").replace("spots","").replace("spot","")

        colour = [255,255,255]
        
        if colour_text == 'white':
            colour = [255,255,255]
        elif colour_text == 'blue':
            colour = [0,0,255]
        elif colour_text == 'green':
            colour = [0,255,0]
        elif colour_text == 'red':
            colour = [255,0,0]
        elif colour_text == 'purple':
            colour = [255,0,255]

        

        self.img[0][2:5] = colour
        self.img[2][0] = colour
        self.img[3][0] = colour
        self.img[4][0] = colour
        self.img[6][2:5] = colour
        self.img[2][6] = colour
        self.img[3][6] = colour
        self.img[4][6] = colour
        self.img[1][1] = colour
        self.img[5][1] = colour
        self.img[1][5] = colour
        self.img[5][5] = colour

        scipy.misc.toimage(self.img, cmin=0.0, cmax=255.0).save('outfile.png')

if __name__ == '__main__':
    newtagger = Tagger("This is a new , test sentence. The butterfly in question has a set of blue wings, green spots and brown edges .")
    newtagger.tokenise_text()
    newtagger.tag_text()
    words = newtagger.identify_uses()
    filtergen = FilterGenerator(words)
    filtergen.find_background_colour()
    filtergen.set_background()
    filtergen.find_fore_features()
    