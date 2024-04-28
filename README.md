Sure, here's a README file template based on the information you provided:

---

# Dense Trajectory Computer Vision System

This project implements a computer vision system for computing video descriptors utilizing a combination of Histogram of Oriented Gradients (HOG), Histogram of Optical Flow (HOF), and Motion Boundary Histograms (MBH) techniques. The main innovation lies in the extraction and description of dense trajectories from videos, providing a robust representation of motion patterns compared to previous trajectory approaches. Additionally, the MBH descriptor effectively distinguishes relevant foreground motion from background camera motion in videos.

The implementation is based on the paper **"Dense trajectories and motion boundary descriptors for action recognition"** by Wang et al (2013), and it is coded in Python 3.10.12.

## Code Implementation on GitHub

For detailed code implementation, please visit the [GitHub repository](https://github.com/riddhish143/Dense-Trajectory).

## Dataset Preparation

1. Download the dataset from the provided link [UCF Sports Action Dataset](https://www.crcv.ucf.edu/data/UCF_Sports_Action.php) and place it in the appropriate directory within the project.

## Execution Requirements

### To execute this project, follow these steps:

1. **Install Dependencies**:
   ```
   Python (3.10.12)
   OpenCV (4.9.0)
   NumPy (1.26.4)
   Scikit-Learn (1.4.1.post1)
   Pandas (2.2.1)
   Matplotlib (3.8.3)
   Seaborn (0.13.2)
   ```

2. **Ensure Hardware Requirements**:
   ```
   More than 4GB of RAM
   At least 30GB of disk space
   ```

## File Structure

1. Load the UCF Sport dataset into your local system.
2. Write a code to extract all the avi video files into a folder named `extracted`.
3. Split avi files into train and test splits with labels in `train.txt` and `test.txt` files in the `data` folder.

Folder structure must look like this:

```
data
    |--- extracted
    |       |--- first.avi
    |       |--- second.avi
    |       |--- third.avi
    |            .
    |            .
    |       |--- last.avi
    |--- train.txt
    |--- test.txt
```

## Input Parameters

- **Video Path**: Path to the video file for which descriptors need to be computed.

## Usage Example

### To run the code, follow these steps:

1. Navigate to the `DenseTrajectory` directory using the command: 
   ```
   cd DenseTrajectory
   ```
   
2. Execute the `run.py` file using the command: 
   ```
   python3 run.py
   ```

   **Note**: Before running `run.py`, ensure `already computed descriptors = False` in the main function to compute your own descriptors based on input videos. The UCF-sport dataset has been used for descriptor computation.

3. If finding difficulties in understanding the code, debug the code using `demo.ipynb` file.

### Output

The system processes the video and computes descriptors, which are then saved in the `DenseTrajectory/out` directory.

## Note

- The `train.txt` file should contain paths to training videos along with their corresponding labels for model training.
- The `test.txt` file should contain paths to testing videos along with their corresponding labels for model evaluation.

---
