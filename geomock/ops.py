import numpy as np
from shapely.affinity import translate

def recenter(geom, new_centroid):
    trns = [0,0]
    origin = np.array(geom.centroid.xy)
    new = np.array(new_centroid.xy)
    diff = new - origin
    return translate(geom, *diff) 
