from __future__ import absolute_import
import sys
sys.path.append("/home/arscontrol/catkin_cisc_it/scripts")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ruptures as rpt
import pickle

def Moving_average(object, window_size):
    i = 0
    moving_averages = []
    while i < len(object) - window_size + 1:
        window_average = round(np.sum(object[i:i+window_size]) / window_size, 1)
        moving_averages.append(window_average)
        i += 1
    avg = np.array(moving_averages)
    return avg

def Data_segmentation(memory):
    print("Preparing data for segmentation")
    dataset = memory['Dataset']
    bag_time = dataset[:,0]
    Dtraj_x = dataset[:,1]
    Dtraj_y = dataset[:,2]
    Dtraj_z = dataset[:,3]
    Grip = dataset[:,8]

    execution_time = (bag_time[-1] - bag_time[0])
    print(execution_time)
    dt = execution_time/(len(Dtraj_x))
    linear_V_x= np.empty(len(Dtraj_x))
    linear_V_y= np.empty(len(Dtraj_y))
    linear_V_z= np.empty(len(Dtraj_z))
    iii=0
    for iii in range (len(Dtraj_x)):
        linear_V_x[iii]= (Dtraj_x[iii]-Dtraj_x[iii-1])/dt
        linear_V_y[iii]= (Dtraj_y[iii]-Dtraj_y[iii-1])/dt
        linear_V_z[iii]= (Dtraj_z[iii]-Dtraj_z[iii-1])/dt
    
    linear_V = np.abs(linear_V_x) + np.abs(linear_V_y) + np.abs(linear_V_z)
    avg = Moving_average(linear_V, 20)
    linear_V_nz= np.empty(len(avg))
    ii=0
    indexes = np.argwhere(avg > 0)

    while ii in range(len(indexes)):
        ind = indexes[ii]
        linear_V_nz [ind]= 1
        ii = ii+1
    print("Data prepared")
    return linear_V_nz, linear_V, Grip

object = 'Insert'
path = "/home/imr/CoBT/Memory/Memory_"+object+".pkl"
with open(path, 'rb') as f:
    memory = pickle.load(f)

_, data, _ = Data_segmentation(memory)
segments_sorted = np.array(memory['Post_conditions'])
# print((segments_sorted))


rpt.display(data[1:], segments_sorted[:,5])
# plt.figure(dpi=1200)
plt.savefig('/home/imr/CoBT/Segmentation_graphs/Segmented_graph_'+object+".png", dpi = 1200)
plt.show() 
# # plt.savefig('/home/arscontrol/catkin_cisc_it/scripts/Offline_learning/my_plot.png')