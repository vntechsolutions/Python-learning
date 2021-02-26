# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:44:36 2021

@author: TINH LE
"""


'''
First I am going to inspect the dataset, which include all stock codes in Vietnam.
My purpose is to group (cluster) stock codes that move together, using Unsupervised learning techniques.

How many clusters?

hnx = []

The dataset is exported from the Amitrader.


You are given an array points of size 300x2, where each row gives the (x, y) co-ordinates of a point on a map. Make a scatter plot of these points, and use the scatter plot to guess how many clusters there are.
matplotlib.pyplot has already been imported as plt. In the IPython Shell:
Create an array called xs that contains the values of points[:,0] - that is, column 0 of points.
Create an array called ys that contains the values of points[:,1] - that is, column 1 of points.
Make a scatter plot by passing xs and ys to the plt.scatter() function.
Call the plt.show() function to show your plot.
How many clusters do you see?
'''
xs = points[:,0]

ys = points[:,1]

plt.scatter(xs, ys)

In [4]: plt.show()