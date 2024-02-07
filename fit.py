#dependancies
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
def fitline():   
    #using an if segment to let the user choose a method of data entry
    inp = input("Type 'file' to input a file named input.txt as data, or 'manual' to manually enter data.")
    if inp == "file":
        usrx=np.loadtxt("C:/Users/Oran1/OneDrive - University of Kansas/Research/input.txt",dtype='float',usecols=[0])
        usry=np.loadtxt("C:/Users/Oran1/OneDrive - University of Kansas/Research/input.txt",dtype='float',usecols=[1])
        usryerr=np.loadtxt("C:/Users/Oran1/OneDrive - University of Kansas/Research/input.txt",dtype='float',usecols=[2])
        print("x =",usrx,str("\n"),"y =",usry,str("\n"),"y-error =",usryerr,str("\n"))
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
        usryerr = np.array(input("Input Y-error values: (int32 seperated by spaces)").split(), dtype='float')
        print("dy = "+str(usryerr))
    #segment for ODR line fitting for input data
        data = RealData(usrx, usry, sy=usryerr)
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
        plt.errorbar(usrx, usry, yerr = usryerr, fmt ='o')
        plt.plot(x_fit, y_fit)
        print("Trendline: y="+str(slope)+"x+"+str(intercept))
        plt.show()
    #error segment for nonaccepted input
    else:
       print('Error! Please type either "file" or "manual"')