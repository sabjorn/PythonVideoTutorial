import numpy as np

def imagefilter(frame):
    img = np.copy(frame) # make editable

    # do something with the frame
    #Replace Red layer with Green layer
    img[:,:,0] = frame[:,:,1]

    #Replace Green layer with Blue layer
    img[:,:,1] = frame[:,:,2]

    #Replace Blue layer with Red layer
    img[:,:,2] = frame[:,:,0]

    return img
