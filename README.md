**Action Recognition using Dense Trajectory**

---

### Project Overview:

This project presents a computer vision system for computing video descriptors employing a combination of Histogram of Oriented Gradients (HOG), Histogram of Optical Flow (HOF), and Motion Boundary Histograms (MBH) techniques. The main innovation lies in the extraction and description of dense trajectories from videos, providing a robust representation of motion patterns compared to previous trajectory approaches. Additionally, the MBH descriptor effectively distinguishes relevant foreground motion from background camera motion in videos. The implementation is in Python 3.10.12.

Implementation of code is based on the paper *"Dense trajectories and motion boundary descriptors for action recognition"* by Wang et al (2013).

[Link to the paper](#) (Insert Link)

### Execution Requirements:

**To execute this project, follow these steps:**

1. **Install Dependencies:**
   - Python (3.10.12)
   - OpenCV (4.9.0)
   - NumPy (1.26.4)
   - Scikit-Learn (1.4.1.post1)
   - Pandas (2.2.1)
   - Matplotlib (3.8.3)
   - Seaborn (0.13.2)

2. **Ensure Hardware Requirements:**
   - More than 4GB of RAM
   - At least 30GB of disk space

### Input Parameters:

- **Video Path:** Path to the video file for which descriptors need to be computed.

### Usage Example:

**To run the code, follow these steps:**

1. Navigate to the `DenseTrajectory` directory using the command: 
   ```
   cd DenseTrajectory
   ```

2. Execute the `run.py` file using the command: 
   ```
   python3 run.py
   ```

3. **Note:** Before running `run.py`, ensure `already computed descriptors = False` in the main function to compute your own descriptors based on input videos. The UCF-sport dataset has been used for descriptor computation.

4. If finding difficulties in understanding the code, debug the code using `demo.ipynb` file.

### Output:

The system processes the video and computes descriptors, which are then saved in the `DenseTrajectory/out` directory.

### Note:

- The `train.txt` file should contain paths to training videos along with their corresponding labels for model training.
- The `test.txt` file should contain paths to testing videos along with their corresponding labels for model evaluation.

---

Feel free to modify and enhance this readme file according to your project's specific needs and preferences.

You can access the project by clicking on the following drive link: [Project Link](https://drive.google.com/drive/folders/139dfr8O6bWTTdhVcwGr3n0kleJ3icO72?usp=drive_link)
if any issue mail me riddhishmahajan143@gmail.com
