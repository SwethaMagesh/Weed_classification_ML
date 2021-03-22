## Weed classification 
- The proposed work plans on detecting the weeds in sugarbeet fields. 
- Sugar beet was choosen because the beet is underground, so weed and leaves are often confusing to identify. The weeds in sugar beet are different during different stages of growth. And also perennial weed control is not efficient because the weedicide also affects the crops
- Aim of the project is to identify the exact location of weeds so as to reduce the herbicide usage and to help use precision agriculture to use robotic arms for weed removal

---
## Sample output:
-![image](https://github.com/SwethaMagesh/Weed_classification_ML/blob/main/NOTES/ss.JPG)

- Here First image is input field, Second is Located weeds by the model, Third is the ground evidence

---
## Model used
- UNET ARCHITECTURE
  - It has 2 phases: 1. DOWNSAMPLING 2. UPSAMPLING
  1. Downsampling has Convolution and Maxpooling layers repeated
    - These are repeated 4 times in our model
    - CCPCCPCCPCCP
    - Aim is to reduce the resolution of images to detect the feature
  1. Upsampling has Convolution and Upsampling layers repeated
    - These are repeated 4 times in our model
    - CCUCCUCCUCCU
  1. Finally there are convolutional and single dense layer with sigmoid activation 
  1. *NOTE: Hidden layer activation is relu*


- DATASET:
  - [Synthetic images of sugar beet and random weeds] ()
  - Size of data:376 MB (compressed tar.gz file)
  - No of images: 1252
  - Annotation type: Semantic segmentation
  - ![image](https://user-images.githubusercontent.com/43994542/111937543-f6f3ff00-8aed-11eb-9478-7309191a5a49.png)
#### Also used:
- [Kaggle dataset] ()
- Having 120 images with xml annotation with bounded box

### CODE
- [VIEW code and comments](https://github.com/SwethaMagesh/Weed_classification_ML/blob/main/ModelUNET.ipynb)

