import json
import sys
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from matrix import get_intrinsic







def extrinsics_camera_detection(input_data):

    input_str = open(input_data)
    input = json.loads(input_str.read())


    extrins = []

    for f in input["frames"]:
        extrinsic = np.array(f["extrinsic_matrix"])
        extrins += [extrinsic]

    R = extrinsic[:3, :3] # rotation matrix
    t = extrinsic[:3, 3] # translation vector

    camera_center = -(R.inv()) @ t

    print("Rotation:\n",R)
    print("Translation:\n",t)
    print("Cam:\n",camera_center)

    intrinsic = get_intrinsic()
    
    


    
    
    

