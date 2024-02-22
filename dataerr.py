# Elias Works, 2024/2/22
# Basic program to calculate average, standard deviation, standard error, and total error from a set of data.
# Might've messed up standard deviation.

#dependancies
import math
import numpy as np

#saving user data input
numdata = int(input('How many data points?\n'))
data = np.array([])

i=0
while i < numdata:
    x = float(input('Input data value: '))

    data = np.append(data, x)

    i = i  + 1
    
#calculating average
avg = 0.0

for x in data:
    avg = x + avg
avg = avg / numdata
print('Average is: ' + str(avg))

#calculating std. dev.
for x in data:
    std = (x - avg) * (x - avg)
std = std / (numdata - 1)
std = math.sqrt(std)
print('Standard Deviation: ' + str(std))

#calculating standard error on average
stdavg = std / (math.sqrt(numdata))
print('Standard Error on Average: ' + str(stdavg))

#input for total measurement error
isterr=float(input('Input instrument error:'))

#calculating total measurment error
toter=math.sqrt(isterr**2+stdavg**2)
print('Total measurment error: '+ str(toter))
