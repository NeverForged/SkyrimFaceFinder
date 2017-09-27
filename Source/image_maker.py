import os
from PIL import Image
from PIL import ImageOps
import numpy as np
from sklearn.model_selection import train_test_split

def cut_images():
    '''
    Turns the three Images from the website into the base images for my thing.
    '''
    if not os.path.exists('../Data'):
        os.makedirs('../Data')

    # cut images and make directories for them
    for image in os.listdir('../Downloads/'):
        dimg = Image.open('../Downloads/' + image).convert('RGB')
        w, h = dimg.size
        ws = int(w/5)
        hs = int(h/4)
        # make a directory...
        race = image.replace('.jpg','')
        pix_old = dimg.load()
        for i in range(5):
            for j in range(4):
                n = i + 5*j  # race name number
                img = Image.new( dimg.mode, (ws, hs))
                pix_new = img.load()
                for x in range(ws):
                    for y in range(hs):
                        pix_new[x, y] = pix_old[i*ws + x, j*hs + y]
                # check dir
                if not os.path.exists('../Images/' + race + str(n)):
                    os.makedirs('../Images/' + race + str(n))
                # now save
                img.save('../Images/' + race + str(n) + '/base.png')
                # resize_1
                for ii in range(-2, 2, 1):
                    for jj in range(-2, 2, 1):
                        timg = Image.new('RGB',
                                        (ws+abs(ii), hs+abs(jj)),
                                        (255, 255, 255))
                        offset = (int((ws - ws - ii) / 2),
                                  int((hs - hs - jj) / 2))
                        timg.paste(img, offset)
                        timg.save('../Images/' + race + str(n) +
                                 '/image{}.png'.format(ii*100 + jj))


class SkyrimImages(object):
    '''
    Class to manage files of images of presets, of different sizes and offsets,
    with the images split into teset and training sets.
    '''

    def __init__(self, root='../Data', limit='None'):
        '''Create an object of the class.
        Parameters:
        ----------
        racenames: list of strings of dog names; these should match folder name
        root:      directory to store the image files
        '''

        self.root = root
        self.image_id = 0
        self.imagesize = 100
        self.counter = 0
        self.tt_split = 0.3
        lst = [a[0].replace('../Images\\','') for a in os.walk('../Images')]
        self.racenames = []
        for a in lst[1:]:
            try:
                int(a[-2:])
                if limit != 'male':
                    self.racenames.append(a)
            except:
                if limit != 'female':
                    self.racenames.append(a)

    def _make_img(self, dimg, directory):
        '''
        This is where I do all the fun things....
        '''
        # basic
        width, height = dimg.size
        img = Image.new('RGB',
                        (self.imagesize, self.imagesize),
                        (255, 255, 255))
        offset = (int((self.imagesize - width) / 2),
                  int((self.imagesize - height) / 2))
        img.paste(dimg, offset)
        img.save(directory + '/image{}.png'.format(self.imageid))
        self.imageid += 1
        img = ImageOps.mirror(img)
        img.save(directory + '/image{}.png'.format(self.imageid))
        self.imageid += 1


    def _make_imgs(self, directory):
        '''
        '''
        # First, create directories if they don't exist
        print(directory)
        for newdir in [directory +'/' + name for name in self.racenames]:
            if not os.path.exists(newdir):
                os.makedirs(newdir)
                os.makedirs(newdir + '/train')
                os.makedirs(newdir + '/test')

        for racename in self.racenames:
            print('\r{}'.format(racename), end='')
            racedir = directory + '/' + racename
            for image in os.listdir("../Images/" + racename):
                dimg = Image.open('../Images/' + racename + '/' + image)
                w, h = dimg.size
                if w >= self.imagesize or h >= self.imagesize:
                    big = h
                    if w >= h:
                        big = w
                    img = Image.new('RGB',
                                    (big, big),
                                    (255, 255, 255))
                    offset = (int((big - w) / 2),
                              int((big - h) / 2))
                    img.paste(dimg, offset)
                    dimg = img.resize((self.imagesize,self.imagesize),
                                        Image.ANTIALIAS)
                if (self.train_cnt == 0 or self.test_cnt/self.train_cnt
                    >= self.tt_split):
                    self._make_img(dimg, racedir + '/train')
                    self.train_cnt += 1
                else:
                    self._make_img(dimg, racedir + '/test')
                    self.test_cnt += 1

    def generate_img_files(self):
        '''
        '''
        self.imageid = 0
        self.train_cnt = 0
        self.test_cnt = 0
        self._make_imgs(self.root)

    def _get_filenames(self, testtrain, racename):
        '''Get full names of all image files to be loaded
        Parameters:
        ----------
        testtrain: either 'test' or 'train', depending on whence to load the file
        '''
        base = self.root + '/' + racename + '/' + testtrain + '/'
        return [ base+directory for directory in os.listdir(base) ]

    def load_images(self, testtrain):
        '''Load the images files already created into arrays return two numpy
        arrays, one of shape (n, p), the other of shape (n, f), where n=number
        of data points, p=number of pixels, f=number of fonts Parameters:
        ----------
        testtrain: either 'test' or 'train', depending on whence to
        load the file
        '''
        imagedict = {}
        for racename in self.racenames:
            imagedict[racename] = self._get_filenames(testtrain, racename)
        n = sum([len(imagedict[racename]) for racename in self.racenames])
        p = self.imagesize * self.imagesize * 3
        f = len(self.racenames)
        ximages = np.zeros((n,p))
        yimages = np.zeros((n,f))
        i = 0
        for yi, racename in enumerate(self.racenames):
            for imagename in imagedict[racename]:
                ximages[i,:] = np.array(Image.open(imagename)).reshape((-1,))
                yimages[i,yi] = 1
                i += 1
        return ximages, yimages


if __name__ == '__main__':
    cut_images()
