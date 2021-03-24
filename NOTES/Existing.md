### SOYA BEAN
#### Files 
1. UNZIP
1. os - 3 folders - train, test, val each having 4 folders
1. DATASET from kaggle == file is copied from src to dest (split as test, val, train) using ***shutil***
---
#### MODEL definition
1. Conv2D, MaxPooling, Flatten, Dropout, Dense
1. Compile the model
---
#### Augmentation and rescaling
- Resize
- Rescale
- Random Contrast
- Random Crop
- Random Zoom
1. Train data - ImageDataGenerator(all possible augmentations)
1. Test and Validation - ImageDataGenerator(Only rescale)
1. Output will be batches of data
*Note parameters: dir, target size, color mode, batch size(no of images), class_mode*
---
#### Training
- **model.fit_generator** not model.fit (we have to specify X,Y)
- DOUBT: Augmentation happens how many times ? Once? Infinitely?
- **Steps per epochs** - no of batches - ceil(n/batchsize)
- Specify parameters -
    - Epochs
    - Val data
    - Steps per epoch
- Draw a graph and interpret
---
#### Testing 
- Evaluate n find accuracy
---
#### Prediction
- DIDNT UNDERSTAND
---
#### CODE in github

- [SOYABEAN](https://github.com/carlavm/Weed-and-Crop-detection-CNN/blob/master/Weed%20detection%20CNN.ipynb)
- [Link for colab](https://colab.research.google.com/drive/1Pe9_4JG80J94L1HxVBm9IJf2J43pgr6Q#scrollTo=05OhIjytzEFr)


### WEED DETECTION AND SEGMENTATION
## Basic Steps
1. Input image
1. Cropping into Square immage and normalization
1. Feature Extraction
1. Classifier
1. op - if false return
1. else pass into unet architecture and dense CRF
1. op- **Segmented Image**

## Augmentation and Pre Processing
- For changing color space of image - cvtColor(src,dest)
- square center crop 
- To  normalize, First take squared center crop and resize it(*cv2.resize()*) and convert into numpy array and normalize it.

## Classification
- Read all files and label them
- Separate the files( train set and validation set)
- Training Generator ( batch iages converted to binary class matrix)
- inceptionV3 archi is used
- one global polling and dense layer is created
*(NOTE : Inception v3  has 48 layers)*
- Compile the  model(loss is *binary_crossentropy* and optimizer is *adamax()*) and load the model
- Different classifiers are used say ** SVM,Random Forest Classifier,Decsion Tree Classifier,Softmax***

# SVM
- Objective : to return best fit to categorize our data
1. 
