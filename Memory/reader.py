import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ruptures as rpt
import pickle
from mpl_toolkits.mplot3d import Axes3D

memory_path = "/home/imr/CoBT/Memory/Memory_Cube2.pkl"
with open(memory_path, 'rb') as f:
    memory = pickle.load(f)

print(memory.keys())

ee_dataset = memory['Dataset'][:,1:8]
segments = np.array(memory['Post_conditions'], dtype=int)[:,-1]
print(segments)
# 3d plot
fig = plt.figure()
ax = fig.gca(projection='3d')
line1 = ax.plot3D(ee_dataset[:,0], ee_dataset[:,1], ee_dataset[:,2], 'green', label='EE trajectory')
ax.scatter(ee_dataset[segments,0], ee_dataset[segments,1], ee_dataset[segments,2], c='blue', label='Segmented Points')
ax.scatter(0, 0, 0, c='red', label='Robot Base')
ax.scatter(ee_dataset[segments[0],0], ee_dataset[segments[0],1], ee_dataset[segments[0],2], c='black', label='Start')
ax.scatter(ee_dataset[segments[-1],0], ee_dataset[segments[-1],1], ee_dataset[segments[-1],2], c='pink', label='End')
ax.set_title('EE plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
