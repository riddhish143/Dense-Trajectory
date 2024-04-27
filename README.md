# Dense Trajectory 

1. Dense trajectories are extracted by tracking densely sampled points using optical flow fields. This gives a much denser sampling of trajectories compared to previous methods that tracked sparse interest points.

2. Motion boundary histograms (MBH) are computed along the dense trajectories to encode relative motion between pixels. This descriptor is robust to camera motion and highlights foreground motion.

3. Other descriptors like trajectory shape, HOG for appearance, and HOF for optical flow are also computed along the dense trajectories.

4. The dense trajectory features are encoded using a bag-of-features approach and classified with SVMs.

5. The dense trajectories and MBH descriptors achieve state-of-the-art results on four challenging action recognition datasets: KTH, YouTube, Hollywood2, and UCF sports.

The main novelty is extracting and describing dense trajectories from videos, which provides a more robust representation of motion patterns compared to previous trajectory approaches. The MBH descriptor is also effective at separating relevant foreground motion from background camera motion in videos.

## Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)

## Project Description

An implementation of the paper ["Dense trajectories and motion boundary descriptors for action recognition" by Wang et al (2013)](https://hal.inria.fr/hal-00803241/document).

## Installation

```pip install matplotlib , scikit-learn , opencv-python , numpy```

## Usage

* Command to run : ```python3 run.py```
* if finding difficulities running the code debug the code using below file
* Check each line of code by running : ```demo.ipynb``` file

## Accessing the Project

You can access the project by clicking on the following drive link: [Project Link](https://drive.google.com/drive/folders/139dfr8O6bWTTdhVcwGr3n0kleJ3icO72?usp=drive_link)
if any issue mail me riddhishmahajan143@gmail.com
