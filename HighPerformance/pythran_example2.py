#pythran export arc_dist(float[], float[], float[], float[])

import numpy as np

def arc_dist(theta1, phi1, theta2, phi2):
    temp = (np.sin((theta2-theta1)/2)**2 + 
           (np.cos(theta1)*np.cos(theta2)) * np.sin((phi2-phi1)/2)**2)
    return 2 * np.arctan2(np.sqrt(temp), np.sqrt(1-temp))
