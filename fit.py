# Elias Works, 2024/2/22
# Program to take file or manual data and fit a linear line and error to the points

#dependancies
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
#using an if segment to let the user choose a method of data entry
inp = input("Type 'file' to input a tab-delimited file (with 4 columns of data) named input.txt as data, or 'manual' to manually enter data.")
if inp == "file":
    usrx=np.loadtxt("input.txt",dtype='float',usecols=[0])
    usry=np.loadtxt("input.txt",dtype='float',usecols=[1])
    usrxerr=np.loadtxt("input.txt",dtype='float',usecols=[2])
    usryerr=np.loadtxt("input.txt",dtype='float',usecols=[3])
    print("x =",usrx,str("\n"),"y =",usry,str("\n"),"x-error=",userxerr,str("\n"),"y-error =",usryerr,str("\n"))
#segment for ODR line fitting for text file data
    data = RealData(usrx, usry, sy=usryerr)
    odr = ODR(data, model=unilinear)
    output = odr.run()
    slope, intercept = output.beta
    output.pprint()
    def linear_func(p, x):
       m, c = p
       return m*x + c
    linear_model = Model(linear_func)
    x_fit = np.linspace(usrx[0], usrx[-1])
    y_fit = linear_func(output.beta, x_fit)
    #plots fitted data on a graph with a trendline
    plt.scatter(usrx,usry)
    plt.errorbar(usrx, usry, yerr = usryerr, fmt ='o')
    plt.plot(x_fit, y_fit)
    print("Trendline: y="+str(slope)+"x+"+str(intercept))
    plt.show()
elif inp == "manual":
#translates three user inputs of data into three seperate arrays for data conversion and fitting 
    usrx = np.array(input("Input X values: (int32 seperated by spaces)").split(), dtype='float')
    print("x = "+str(usrx))
    usry = np.array(input("Input Y values: (int32 seperated by spaces)").split(), dtype='float')
    print("y = "+str(usry))
    usrxerr = np.array(input("Input X-error values: (int32 seperated by spaces)").split(), dtype='float')
    print("dx = "+str(usrxerr))
    usryerr = np.array(input("Input Y-error values: (int32 seperated by spaces)").split(), dtype='float')
    print("dy = "+str(usryerr))
#segment for ODR line fitting for input data
    data = RealData(usrx, usry, sx=usrxerr, sy=usryerr)
    odr = ODR(data, model=unilinear)
    output = odr.run()
    slope, intercept = output.beta
    output.pprint()
#translates ODR output into usable format
    def linear_func(p, x):
       m, c = p
       return m*x + c
    linear_model = Model(linear_func)
    x_fit = np.linspace(usrx[0], usrx[-1])
    y_fit = linear_func(output.beta, x_fit)
    #plots fitted data on a graph with a trendline
    plt.scatter(usrx,usry)
    plt.errorbar(usrx, usry, xerr = usrxerr, yerr = usryerr, fmt ='o')
    plt.plot(x_fit, y_fit)
    print("Trendline: y="+str(slope)+"x+"+str(intercept))
    plt.xlabel(str(input("Input x-label: ")))
    plt.ylabel(str(input("Input y-label: ")))
    plt.show()
#error segment for nonaccepted input
else:
   print('Error! Please type either "file" or "manual"')
