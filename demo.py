import numpy as np
import os
from os.path import join
from trajectory import Trajectory
from settings import *
from visualize import *
from matplotlib import pyplot as plt

def trajectories_from_video(path, vis_flow=False, vis_trajectories=False,
                            W=W,  # sampling grid spacing
                            L=L,  # maximum length of a trajectory
                            static_displacement_thresh=static_displacement_thresh,  # static if the sum of all displacements' norms is lower
                            max_single_displacement=max_single_displacement,  # max percentage a single displacement has in a trajectory
                            ):
    # read the video at 'path' frame by frame
    capture = cv.VideoCapture(path)
    r, current_frame = capture.read()
    current_frame = cv.cvtColor(current_frame, cv.COLOR_BGR2GRAY)
    height, width = current_frame.shape  # video resolution
    print(f'Height:{height} Width:{width}')
    flow = None
    flow_list = []
    print("flow_list", flow_list)
    grid_xs = list(range(0, width, W))
    grid_ys = list(range(0, height, W))
    frame_i = 0
    trajectories = []
    complete_trajectories = []
    shape_descriptors = []
    print(f'{path}: extracting trajectories')
    while True:
        # pad the frame for extracting tubes around the borders
        gx = cv.Sobel(current_frame, cv.CV_32F, 1, 0)
        gy = cv.Sobel(current_frame, cv.CV_32F, 0, 1)
        # print(gx.shape)
        # print(gy.shape)
        # Normalize the gradients for visualization
        # gx = cv.normalize(gx, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
        # gy = cv.normalize(gy, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)

        # # Display the gradients using imshow
        # plt.figure(figsize=(12, 6))
        # plt.subplot(1, 2, 1)
        # plt.imshow(gx, cmap='gray')
        # plt.title('Sobel Gradient X')
        # plt.axis('off')

        # plt.subplot(1, 2, 2)
        # plt.imshow(gy, cmap='gray')
        # plt.title('Sobel Gradient Y')
        # plt.axis('off')

        # plt.show()
        r, next_frame = capture.read()
        if r:
            next_frame = cv.cvtColor(next_frame, cv.COLOR_BGR2GRAY)
            flow = cv.calcOpticalFlowFarneback(current_frame, next_frame, flow, pyr_scale=None, levels=1,
                                               winsize=of_winsize, iterations=10, poly_n=5, poly_sigma=1.1,
                                               flags=None)  # same values
            # round the values so each pixel is 'moving' to a particular pixel in the next frame
            flow = np.round(flow)
            print(flow.shape)
        break

trajectories_from_video(r"/home/riddhish143/Downloads/Dense Tracjectory Updated/Dense Track/dense-trajectories-action-recognition/data/Extracted/2_1.avi")