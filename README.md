# SkyrimFaceFinder
Simple Neural Network Identifier for Skyrim Vanilla Pregens.

### Business Understanding
Skyrim recently had a re-release, and has a slider-based character build system.  Sometimes you want to make a character that looks like someone, i.e. you want to make yourself, a celebrity, a specific piece of art, etc.  The goal of this project is to use tensorflow to create a Neural Network that will find the closest pregen character to a given photograph/picture.

**Constraints**
In order to limit this project (and allow a quick 'win' for me), I will make the following limitations.  If you want to borrow this code to go beyond that, please do.
* *Human Only* - This will be so that the author can find the closest pregen to their own face.
* *Specific pose* - This allows a regular neural net (with creepy eigenfaces) and avoids the need for a CNN, which I'd doing plenty of over in my [Dog Classifier](https://github.com/NeverForged/DogClassifier), which at the time of this writing is still a WIP.

### Data Understanding
Since my laptop cannot run graphics-intensive games, and my only game system is an xbox 360, I will stick to the standard pregens.  This is good, since it limits the data.  I found a decent source of picture [here](https://levelskip.com/rpgs/skyrimthebestrace).  This of course means I will need to play around with these images.

These give me literally 1 image for each pregen.  I will need to manipulate these to make multiple versions of each of these pictures, likely by scalling up or down by a pixel

### Data Preparation
Again, stealing a bit from my [Dog Classifier](https://github.com/NeverForged/DogClassifier), I can build a little python code that will manipulate these images.
Mostly just offsetting them by 1-2 pixels in each direction, which also resizes them to make them 100 x 100.

### Modeling
This is where I make a Neural Network...
![Network](https://github.com/NeverForged/DogClassifier/blob/master/Source/WebImages/fully_connected.png)
