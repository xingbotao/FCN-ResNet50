#!/usr/bin/env python
import matplotlib.pylab as plt
import numpy as np
import types
x=[]
y=[]
with open('iter.txt','r') as f:
	for strr in f.readlines():
		x.append(float("".join(strr.split())))

with open('loss.txt','r') as f:
	for strr in f.readlines():
		y.append(float("".join(strr.split())))

plt.plot(x, y)
plt.show()
