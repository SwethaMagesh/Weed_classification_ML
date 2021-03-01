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

## RESNET architecture (Residual Network) and VGG16 for feature extraction
## UNET and SEGNET for segmentation
## Evaluate accuracy
- For pixel-level classification, the most commonly used evaluation indicators are Pixel Accuracy (pixel accuracy) and Mean Inetersection over Union (average intersection and union ratio), both of which are calculated based on confusion Matrix-based-PA, MPA, MioU, FWIoU (Frequency, Power ratio based)
- [Courtesy](https://www.programmersought.com/article/51757204725/)
- [Code](https://github.com/jfzhang95/pytorch-deeplab-xception/blob/master/utils/metrics.py)

## Related repos:
- (check if related n useful)
- [Pytorch deeplab xception](https://github.com/jfzhang95/pytorch-deeplab-xception)

