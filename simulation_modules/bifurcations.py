#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np



# Don't have a clear python way of generating
# sequences so here are a few algorithms
def generate_fib(num):
    j = 0
    k = 1
    fibs = np.zeros(num, dtype=float)
    for i in range(num):
        fibs[i] = k
        temp = j
        j = k
        k = k + temp
    return fibs 

def sieve(n):
    primes=[]
    s_primes = [0 for x in range(0,n)]
    i,j=2,2
    while(i * j < n):
         s_primes[i*j] = 1
         j=j+1
         if i*j >= n:
             i,j = i+1,2
    for i in range(2,n):
         if s_primes[i] == 0:
             primes.append(i)
    return np.array(primes, dtype=float)

def generate_sieve(n):
    i = n
    while (i / np.log(i)) < n:
        i = i + 1
    arr = sieve(2 * i)
    return arr[0:n]

def naturals(n):
    return np.array([i for i in range(0, n)], dtype=float)



# An arbitrary map type
class Map:
    def __init__(self, map_type):
        self.description = map_type

    def transition(self, x, r):
        pass

    def transition_range(self, x, r, n):
        xn = x
        for i in range(n):
            xn = self.transition(x, r)
        return xn


# Extension of a map
class Logistic(Map):
    def __init__(self):
        super().__init__("Logistic Map")

    def transition(self, x, r):
        return r * x * (1 - x)

class Henon(Map):
    def __init__(self, y0, b):
        super().__init__("Henon Map")
        self.y = y0
        self.b = b

    def transition(self, x, a):
        xn = self.y + 1 - a * x**2
        self.y = self.b * xn
        return xn








# Vanilla bifurcation

##
# @brief Displays a bifurcation plot of m iterates
# within the 
#
# @param rmin Minimum r value
# @param rmax Maximum r value
# @param iterates Number of iterations per R value
# @param cut_off Starting iteration for x, algorithm starts at x0, plots cut_off number of
# @param points, then plots iterates number of points (so a total of cut_off + iterates distinct iterations are
# carried out)
# @param x0 Initial x value
# @param dr R increment
# @param map_func The mapping function should take in one number jand spit out another number
def biffurcation(rmin, rmax, iterates, x0, mapping: Map, cut_off=0, dr=0.01):
    
    r_vals = np.arange(rmin, rmax, dr, dtype=np.float64)

    # Array to hold outputs (only sized iterates)
    xarr = np.zeros(iterates, dtype=np.float64)
    
    

    for i in range(r_vals.shape[0]):

        x = x0
        for j in range(cut_off):
            x = mapping.transition(x, r_vals[i])


        for j in range(iterates):
            x = mapping.transition(x, r_vals[i])
            xarr[j] = x

        plt.scatter([r_vals[i] for r in range(iterates)], xarr, c="black", s=0.0003)

    plt.xlabel('R Value')
    plt.ylabel(f'x_n (iterations (m), cut_off (l) = {iterates, cut_off}')
    plt.title(f'Bifuracation Diagram for the {mapping.description} x0 = {x0}')


# Domain bifurcation
# In retrospect, this is equivalent to simply scaling the axis by the sequence, but the diagram still looks cool
def biffurcation_seq(rmin, rmax, iterates, x0, mapping: Map, cut_off=0, funcitterator=naturals):
    
    r_vals = funcitterator(iterates)
    print(r_vals)
    np.delete(r_vals, np.where(r_vals == 0)[0])
    maxim = np.max(r_vals)
    minim = np.min(r_vals)

    # Map all elements into r range
    for i in range(r_vals.shape[0]):
        print(i)
        r_vals[i] = (r_vals[i] - minim) / (maxim - minim) * (rmax - rmin) + rmin

    print(r_vals)


    # Array to hold outputs (only sized iterates)
    xarr = np.zeros(iterates, dtype=np.float64)
    
    for i in range(iterates):

        x = x0
        for j in range(cut_off):
            x = mapping.transition(x, r_vals[i])


        for j in range(iterates):
            x = mapping.transition(x, r_vals[i])
            xarr[j] = x

        plt.scatter([r_vals[i] for r in range(iterates)], xarr, c="black", s=0.0003)

    plt.xlabel('R Value')
    plt.ylabel(f'x_n (iterations (m), cut_off (l) = {iterates, cut_off}')
    plt.title(f'Bifuracation Diagram for the {mapping.description} x0 = {x0}')





if __name__ == '__main__':
    
    log = Logistic()
    henon = Henon(0.3, 0.3)

    biffurcation_seq(rmin=2.8, rmax=4.0, x0=0.5, cut_off=500, iterates=600, mapping = log, funcitterator=generate_sieve)
    #  biffurcation(rmin=0, rmax=2, x0=0.5, cut_off=500, iterates=600, dr=0.0005, mapping = henon)
    #
    #
    #
    max_r = 2
    min_r = 0
    x0 = 0.5
    cut_off = 500
    iterates = 600
    dr = 0.000001
    mapping = log

    #  max_r = 3.57
    #  min_r = 2.8
    #  x0 = 0.5
    #  cut_off = 500
    #  iterates = 600
    #  dr = 0.0001
    #  mapping = log

    print("here")
    #  plt.xticks( np.arange(min_r, max_r, dr) )


    plt.show()










