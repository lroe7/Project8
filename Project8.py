# Lauren Roe
# CST-305
# This is my own work

import numpy as np                      # imports numpy library
import math                             # imports the math library
import matplotlib.pyplot as plt         # imports the necessary functions to plot graphs


def parta(x):                           # defines the function
    func = math.sin(x) + 1              # function for part a
    return func                         # returns the function


def partc(x):                           # defines the function
    func = math.log(x)                  # function for part c
    return func                         # returns the function


def part2(x):                           # defines the function
    func = 0.0542*x + 14.806            # function for part 2 that was found using the best fit line of the excel graph
    return func                         # returns the function


def graph(part, lobound, upbound, N):               # function that plots all of the graphs
    x = np.linspace(lobound, upbound, N + 1)        # creates the x values for the bar graph
    y = []                                          # empty array to later hold y values of the bar graph

    X = np.linspace(lobound, upbound, N * N + 1)    # creates the x values for the graph
    Y = []                                          # empty array to later hold y values of the graph

    if part == 'a':                                 # if its graphing part a, uses this
        for i in range(0, N + 1):                   # repeats while the index is within the range
            y.append(parta(x[i]))                   # finds the y values and fills the y array
        for i in range(0, N * N + 1):               # repeats while the index is within the range
            Y.append(parta(X[i]))                   # finds the Y values and fills the Y array

    if part =='c':                                  # if its graphing part c, uses this
        for i in range(0, N + 1):                   # repeats while the index is within the range
            y.append(partc(x[i]))                   # finds the y values and fills the y array
        for i in range(0, N * N + 1):               # repeats while the index is within the range
            Y.append(partc(X[i]))                   # finds the Y values and fills the Y array

    if part =='2':                                  # if its graphing part 2, uses this
        for i in range(0, N + 1):                   # repeats while the index is within the range
            y.append(part2(x[i]))                   # finds the y values and fills the y array
        for i in range(0, N * N + 1):               # repeats while the index is within the range
            Y.append(part2(X[i]))                   # finds the Y values and fills the Y array

    plt.figure(figsize=(15, 5))                     # creates the size of the graph

    plt.subplot(1, 3, 1)                            # first graph of the subplot, the left riemann sum
    plt.plot(X, Y, 'b')                             # plots the function
    xleft = x[:-1]                                  # finds the x value of the bar
    yleft = y[:-1]                                  # finds the y value of the bar
    plt.plot(xleft, yleft, 'b.', markersize=10)     # plots the points that the riemann bar lands on the function
    plt.bar(xleft, yleft, width=(upbound - lobound) / N, align='edge')      # plots the bars
    plt.title('Left Riemann Sum')                   # titles the graph

    plt.subplot(1, 3, 2)                            # second graph of the subplot, the mid riemann sum
    plt.plot(X, Y, 'b')                             # plots the function
    xmid = x[:-1]                                   # finds the x value of the bar
    ymid = y[:-1]                                   # finds the y value of the bar
    plt.plot(xmid, ymid, 'b.', markersize=10)       # plots the points that the riemann bar lands on the function
    plt.bar(xmid, ymid, width=(upbound - lobound) / N)      # plots the bars
    plt.title('Mid Riemann Sum')                    # titles the graph

    plt.subplot(1, 3, 3)                            # third graph of the subplot, the right riemann sum
    plt.plot(X, Y, 'b')                             # plots the function
    xright = x[1:]                                  # finds the x value of the bar
    yright = y[1:]                                  # finds the y value of the bar
    plt.plot(xright, yright, 'b.', markersize=10)   # plots the points that the riemann bar lands on the function
    plt.bar(xright, yright, width=-(upbound - lobound) / N, align='edge')       # plots the bars
    plt.title('Right Riemann Sum')                  # titles the graph
    plt.show()


# part 1 a
partaLB = -math.pi                  # lower bound for part a
partaUB = math.pi                   # upper bound for part a
N = 4                               # number of bins for the bar graph
graph('a', partaLB, partaUB, N)     # graphs the plots for part a

# part 1 c
partcLB = 1                         # lower bound for part c
partcUB = math.e                    # upper bound for part c
N = 20                              # number of bins for the bar graph
graph('c', partcLB, partcUB, N)     # graphs the plots for part c

# part 2
part2LB = 1                         # lower bound for part 2
part2UB = 30                        # upper bound for part 2
N = 5                               # number of bins for the bar graph
graph('2', part2LB, part2UB, N)     # graphs the plots for part 2
