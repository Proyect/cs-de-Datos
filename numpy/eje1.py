import numpy as np
import matplotlib.pyplot as plt 
import math

def info():
    version = np.__version__
    print("version:"+version)
    np.show_config()
    print("info:" + np.__doc__)

Z = np.zeros(10)
print(Z)

Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))