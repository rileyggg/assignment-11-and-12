import numpy as np
import matplotlib
matplotlib.use('Agg') # This is only required to use matplotlib on Cloud9
import matplotlib.pyplot as plt
import pymongo
from pymongo import MongoClient
x = np.linspace(0,10,11) # This creates an evenly spaced array from 0 to 10 
y = x**2 # This our y array, equals to x squared
print(x)
print(y)
figure, axis = plt.subplots(1, 1) # This create a figure with 1 axis
axis.plot(x, y)
figure.savefig("x_squared.svg")
axis.plot(x, y)
figure.savefig("x_squared.svg")
