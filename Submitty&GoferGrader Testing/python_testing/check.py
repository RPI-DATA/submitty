# This is a first cut at using my own python script to check a student file
import numpy as np
import sys

# load the student array
y = np.load('product.npy')
ytrue = np.load('true_product.npy')

# output shape, but do not proceed if the shapes do not match
print(y.shape)
if y.shape != ytrue.shape:
    sys.exit()

for i in range(ytrue.shape[0]):
    if abs(y[i] - ytrue[i]) > 1e-14:
        print("Element ",i," is incorrect: error = ",abs(y[i] - ytrue[i]))
    else:
        print("Element ",i," is correct")
