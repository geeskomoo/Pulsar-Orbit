# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:30:11 2023

@author: moores15
"""
import matplotlib.pyplot as plt
import numpy as np
"""
define x and y corresponds to a circle of radius 1, that correspponds to the
edge of 1 quarter of a circle
"""

circle_x = np.linspace(0,1,100)
circle_y = np.sqrt(1-circle_x**2)
"""
create graph of this figure
"""
fig1= plt.figure()
fig1.set_size_inches(5,5)
plt.plot(circle_x, circle_y)
plt.xlabel("x")
plt.ylabel("y")
"""
plot random points for pi estimation
"""
times=2000000
x = np.random.rand(times)
y= np.random.rand(times)

"""
plot the random points, using 'o' arguement to prevent straight line.
"""
fig2= plt.figure()
fig2.set_size_inches(5,5)
plt.plot(x, y, 'o', markersize=1)
plt.plot(circle_x, circle_y)
plt.xlabel("x")
plt.ylabel("y")
plt.show ()

"""
restrict the points to be within circle
"""
dist=np.sqrt(x**2+y**2)
incircle =dist <= 1
"""
obtain percentage of points within circle. Multiply this by 4 to calculate pi
"""
incircle_ratio=float(np.sum(incircle))/float(len(incircle))
pi= incircle_ratio*4
print ('The estimated value of pi is:', pi)
"""
visualising the error of our approximation of pi using cumulative sum and
standard devaition
"""
cumulative_incircle=np.cumsum(incircle)
cumulative_ratios=(cumulative_incircle/np.arange(1,times+1,dtype=float))
pis= cumulative_ratios*4

"""
plot approximate value of pi against sample size
"""
plt.figure()
approx_pis=plt.plot(pis)
pi, = plt.plot(np.repeat(np.pi, times))
"""Restrict y-axis to [3.1,3.3] sp that more detail is visible."""
plt.ylim(3.1,3.3)
plt.xlabel("samaple size")
plt.legend ([approx_pis,pi],["Approximation","Exact value"])

"""
contd. standard deviation
"""
def cummean(arr):
    return np.cumsum(arr)/np.arange(1,len(arr)+1,dtype=np.float)
def cumstd(arr):
    return np.sqrt(cummean(arr**2)-cummean(arr)**2)
plt.figure()
stdevs, = plt.plot(cumstd(pis))
plt.legend([stdevs],["Standard deivation"])
plt.xlabel("Sample size")
