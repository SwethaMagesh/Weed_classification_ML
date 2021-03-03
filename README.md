# Weed_classification_ML

- This is a part of innovation practices laboratory
- To classify weeds from images present.
  ![image](https://user-images.githubusercontent.com/43994542/106354528-7cdaa180-6318-11eb-9709-53a915ed86cd.png)

## Sample tutorial

[Coursera sample to classify man or horse](https://github.com/lmoroney/dlaicourse/blob/master/Horse-or-Human-WithDropouts.ipynb)

## Introduction

- Machine learning methods are normally applied for the final step of classification. **_Examples are Bayesian classification, support vector machines, self-organising maps, random
  forest algorithms, and artificial neural networks._**

- With the advent of deep learning techniques, feature extraction step and classification step are merged. Convolutional Neural
  Networks (CNN) perform feature extraction automatically before classification and detection tasks.
## Data augmentation and rescaling techniques
- **Data augmentation**: *a technique to increase the diversity of your training set by applying random (but realistic) transformations such as image rotation*
- Image data should probably be centered by subtracting the per-channel mean pixel values calculated on the training dataset.
- Training data augmentation should probably involve random rescaling, horizontal flips, perturbations to brightness, contrast, and color, as well as random cropping.
- Test-time augmentation should probably involve both a mixture of multiple rescaling of each image as well as predictions for multiple different systematic crops of each rescaled version of the image.
- ***Rescaling***: [0,255] to [0,1] or [-1,1] using 1./255 or 1./127.5 with offset -1
- ***Resizing***: Resize to standard square say 180x180 
## Image Segmentation basics:

- Two types of segmentation
  1. Bounding boxes - easy labelling
  1. Classifying object pixels - difficult to label and draw contours(boundary), but better accuracy in mapping
- Second type - Semantic segmentation: pixel wise classification not used in agriculture because of **_unavailability of labelled images at pixel level_**
- Paper (canola) - 2 step manual labelling, semantic segmentation followed by VGG16 and ResNET50 for feature extraction, UNET, segnet as metaarchitecture

### Notable points

- Segmentation converts image to binary image (0/1) - black / white - foreground/ background
- Thresholding:
  - if pixel intensity greater than threshold, it is foreground(white)
  - else background(black)
- Autothresholding:
  - it may not be always possible to specify manual threshold
  - Best ways of autothresholding : otsu's method
- **_Image thresholding vs Segmentation_**
  - ![image](https://user-images.githubusercontent.com/43994542/109449610-e3b1be80-7a6e-11eb-99b8-58acc84583ca.png)
  - Thresholding is a simple possible segmentation technique, dividing into foreground, background
  - Image thresholding is of two types:
  1. LOCAL
  1. GLOBAL
  - Local thresholding uses different thresholds for diff parts of image, based on some local characteristics, eg. contrast
  - Global thresholding is use of single threshold globally for entire image.
    Eg. OTSU's Algorithm
- OTSU's algorithm
  - Otsu’s method is a means of automatically finding an optimal threshold based on the observed distribution of pixel values
  - **Automatic global thresholding algorithms steps:**
  1. Process the input image
  1. Obtain image histogram (distribution of pixels)
  1. Compute the threshold value T
  1. Replace image pixels into white in those regions, where saturation is greater than T and into the black in the opposite cases.
- **_Note: variations are in step 3 for different algorithms_**
- Otsu's - used for bimodal images
- its histogram has 2 clearly expressed peaks.
- CONCEPT: **_minimise variance on each class in histogram_** (can minimise within-class var or maximise between-class var)
- Lot of math available for the variance calculation
- **_Application of OTSU_**
  - complex solutions, robotic mapping eg( underwater localisation)
- Lots of example images result plus code for otsu's available here in link
  [Courtesy: learnopencv.com](https://learnopencv.com/otsu-thresholding-with-opencv/)
---

## RESNET architecture (Residual Network) and VGG16 for feature extraction
### RESNET
- Winner of ImageNET 2015 challenge
- Can train extremely deep neural networks without the problem of vanishing gradients
- Competitors: *AlexNet, VGG, Inception (GoogleNet) *
- Starting point for transfer learning - standard for backbone model in CV
- We can't simply stack layers together because of **vanishing gradients** which backpropagate to early layers
- SKIP CONNNECTION along with stacking.  [MEDIUM](https://towardsdatascience.com/understanding-and-coding-a-resnet-in-keras-446d7ff84d33#:~:text=The%20ResNet%2D50%20model%20consists,over%2023%20million%20trainable%20parameters.&text=Our%20ResNet%2D50%20gets%20to,in%2025%20epochs%20of%20training.)
- Matrix dimension when adding the input again to outer layer has to be taken care
- RESNET Skip connection used in FCN (Fully convNet), UNET
- These pass info from downsampling to upsampling layers
- Used in image classification, segmentation, localisation
- *Image classification involves predicting the class of one object in an image. Object localization refers to identifying the location of one or more objects in an image and drawing abounding box around their extent. Object detection localizes and classifies one or more objects in an image (combines both)*
- ![image](https://user-images.githubusercontent.com/43994542/109458808-8ffda000-7a83-11eb-8899-b032b5a74526.png)
- Pretrained image net weights??
- [Code for inbuilt resnet using KERAS and self developed RESNET](https://github.com/priya-dwivedi/Deep-Learning/tree/master/resnet_keras)

---
### VGG 16

---
## UNET and SEGNET for segmentation
- [Code](https://github.com/milesial/Pytorch-UNet/blob/67bf11b4db4c5f2891bd7e8e7f58bcde8ee2d2db/unet/unet_model.py#L8)

## UPSAMPLING
- 
## BATCHNORM
-
## TRANSFER LEARNING FOR object detection
- 
## YOLO 
- You Only Look Once: Unified, Real-Time Object Detection
- [machinelearningmastery explanation](https://machinelearningmastery.com/object-recognition-with-deep-learning/#:~:text=Object%20localization%20refers%20to%20identifying,more%20objects%20in%20an%20image.)
## Evaluate accuracy
- For pixel-level classification, the most commonly used evaluation indicators are Pixel Accuracy (pixel accuracy) and Mean Inetersection over Union (average intersection and union ratio), both of which are calculated based on confusion Matrix-based-PA, MPA, MioU, FWIoU (Frequency, Power ratio based)
- [Courtesy](https://www.programmersought.com/article/51757204725/)
- [Code](https://github.com/jfzhang95/pytorch-deeplab-xception/blob/master/utils/metrics.py)

## Related repos:
- (check if related n useful)
- [Pytorch deeplab xception](https://github.com/jfzhang95/pytorch-deeplab-xception)
- [UNET](https://github.com/milesial/Pytorch-UNet/blob/67bf11b4db4c5f2891bd7e8e7f58bcde8ee2d2db/unet/unet_model.py#L8)
- [RESNET](https://github.com/priya-dwivedi/Deep-Learning/tree/master/resnet_keras)
- [Object detection](https://github.com/NikhilJeikar/Object-detection)