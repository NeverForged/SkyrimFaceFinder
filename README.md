# SkyrimFaceFinder
Simple Neural Network Identifier for Skyrim Vanilla Pregens.

### Business Understanding
Skyrim recently had a re-release, and has a slider-based character build system.  Sometimes you want to make a character that looks like someone, i.e. you want to make yourself, a celebrity, a specific piece of art, etc.  The goal of this project is to use tensorflow to create a Neural Network that will find the closest pregen character to a given photograph/picture.

**Constraints**
In order to limit this project (and allow a quick 'win' for me), I will make the following limitations.  If you want to borrow this code to go beyond that, please do.
* *Human Only* - This will be so that the author can find the closest pregen to their own face.
* *Specific pose* - This allows a regular neural net (with creepy eigenfaces) and avoids the need for a CNN, which I'd doing plenty of over in my [Dog Classifier](https://github.com/NeverForged/DogClassifier), which at the time of this writing is still a WIP.
* *Reduced to three* to save on memory/runtime.  

### Data Understanding
Since my laptop cannot run graphics-intensive games, and my only game system is an xbox 360, I will stick to the standard pregens.  This is good, since it limits the data.  I found a decent source of picture [here](https://levelskip.com/rpgs/skyrimthebestrace).  This of course means I will need to play around with these images.

These give me literally 1 image for each pregen.  I will need to manipulate these to make multiple versions of each of these pictures, likely by scalling up or down by a pixel

### Data Preparation
Again, stealing a bit from my [Dog Classifier](https://github.com/NeverForged/DogClassifier), I can build a little python code that will manipulate these images.
Mostly just offsetting them by 1-2 pixels in each direction, which also resizes them to make them 100 x 100.

### Modeling
![Network](https://github.com/NeverForged/DogClassifier/blob/master/Source/WebImages/fully_connected.png)
The network above should do the job.

### Evaluation
Showing how well it did on my face.
I included the female faces, and since it's a simple 1-layer network, it seems to focus on beards (or the lack thereof).  Since I'm clean-shaven, it labels me female often.
I asked on facebook (always a great source of information) for some volunteer faces.
See [The Project Itself](https://github.com/NeverForged/SkyrimFaceFinder/blob/master/Source/SkyrimFaceFinder.ipynb).

Full disclosure: I'm using my test set more like a validation set, but it's a one-off project for fun that I spent maybe 3 hours on, so.  Also, good to see accuracies hit 100%... of course it's just the same picture offset slightly, but still.


**Examples:**
![No Filter](https://github.com/NeverForged/SkyrimFaceFinder/blob/master/Evaluation/none.png)
![Male Filter](https://github.com/NeverForged/SkyrimFaceFinder/blob/master/Evaluation/male.png)
![Female Filter](https://github.com/NeverForged/SkyrimFaceFinder/blob/master/Evaluation/female.png)

Never expected Redguard (figured Imperial, given my heritage) but I totally see it in the facial structure.


### Deployment
This was a one-off project, so I have no plans to deploy it.  Feel free to clone it and run it yourself.  Instructions below for people not proficient in python/github

If you want to run it yourself, all you need is:
* a **github account** (if you don't have one but are looking at this anyway)
* **[Anaconda python version 3](https://www.anaconda.com/download/)**
* Run **python 3.5** (open command Prompt: "conda install python=3.5.0")
* **Tensorflow** In command prompt: 'pip install tensorflow'
* 'git clone' **this repo** (click 'clone or download', copy the https url, then type 'git clone (url)' in the folder you want this folder in)
* Place a 100 x 100 picture where your face is roughly in the same location as the rest in the 'Input' folder
* 'jupyter notebook' into **SkyrimFaceFinder.ipynb** and *Kernal->Restart and Run All*
It will give you your face and your Skyrim face.
