# coding:utf-8

import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return x**x

if __name__ == "__main__":
	_x = np.linspace(0.0001, 1.3, 101)
	_y = f(_x)
	plt.plot(_x, _y, 'g-', label = 'x^x', linewidth = 2)
	plt.grid()
	plt.legend(loc = 'upper left')
	plt.show()
