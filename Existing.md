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