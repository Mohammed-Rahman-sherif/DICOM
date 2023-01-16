#Cancer_Instance
import sys
import numpy as np
#np.set_printoptions(threshold=sys.maxsize)
#import matplotlib.pyplot as plt

data = np.load('C:\\Users\\smart\\Documents\\Datasets\\Cancer_Instance\\Part 1\\Images\\images.npy')
types = np.load('C:\\Users\\smart\\Documents\\Datasets\\Cancer_Instance\\Part 1\\Images\\types.npy')

a = np.load('C:\\Users\\smart\\Documents\\Datasets\\Cancer_Instance\\hovernet_format\\hovernet_format\\train\\train\\0.npy')

mas = np.load('C:\\Users\\smart\\Documents\\Datasets\\Cancer_Instance\\Part 1\\Masks\\masks.npy')

#plt.imshow(mas)
#plt.show()

print(a)
print(len(a))
print(len(data))
print(len(types))
print(types[0:10])
print(len(mas))
#print(types[1000::-1])
#print(mas[2500])
#np.save('mask',mas[2500])