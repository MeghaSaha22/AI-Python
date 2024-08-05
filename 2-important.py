import matplotlib.pyplot as plt
#Changing Default Plot Size
print(plt.rcParams.get('figure.figsize'))  

fig_size = plt.rcParams["figure.figsize"]  
fig_size[0] = 5  
fig_size[1] = 3  
plt.rcParams["figure.figsize"] = fig_size 

###############################
print("Line Plot") 
import matplotlib.pyplot as plt  
import numpy as np

x = np.linspace(-10, 9, 20)

y = x ** 3

plt.plot(x, y, 'b')  
plt.xlabel('X axis')  
plt.ylabel('Y axis')  
plt.title('Cube Function')  
plt.show()  
print("#########################")
print("#####Creating Multiple Plots######")
import matplotlib.pyplot as plt  
import numpy as np  
x = np.linspace(-10, 9, 20)

y = x ** 3

plt.subplot(2,2,1)  
plt.plot(x, y, 'b*-')  
plt.subplot(2,2,2)  
plt.plot(x, y, 'y--')  
plt.subplot(2,2,3)  
plt.plot(x, y, 'b*-')  
plt.subplot(2,2,4)  
plt.plot(x, y, 'y--') 
print("###############################")
print("###Plotting in Object-Oriented Way####")
import matplotlib.pyplot as plt  
import numpy as np

x = np.linspace(-10, 9, 20)

y = x ** 3

figure = plt.figure()

axes = figure.add_axes([0.2, 0.2, 0.8, 0.8])  

print("#####################################")
print("###Cube Function#############")
import matplotlib.pyplot as plt  
import numpy as np

x = np.linspace(-10, 9, 20)

y = x ** 3

figure = plt.figure()

axes = figure.add_axes([0.2, 0.2, 0.8, 0.8])

axes.plot(x, y, 'b')  
axes.set_xlabel('X Axis')  
axes.set_ylabel('Y Axis')  
axes.set_title('Cube function') 
print("###############################")
print("####INSET VISUALISATION############")
import matplotlib.pyplot as plt  
import numpy as np

x = np.linspace(-10, 9, 20)

y = x ** 3

z = x ** 2

figure = plt.figure()

axes = figure.add_axes([0.0, 0.0, 0.9, 0.9])  
axes2 = figure.add_axes([0.07, 0.55, 0.35, 0.3]) # inset axes

axes.plot(x, y, 'b')  
axes.set_xlabel('X Axis')  
axes.set_ylabel('Y Axis')  
axes.set_title('Cube function')

axes2.plot(x, z, 'r')  
axes2.set_xlabel('X Axis')  
axes2.set_ylabel('Y Axis')  
axes2.set_title('Square function')  
print("############################")
print("Adding Legends##################")
import matplotlib.pyplot as plt  
import numpy as np

x = np.linspace(-10, 9, 20)

y = x ** 3

z = x ** 2

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x, z, label="Square Function")  
axes.plot(x, y, label="Cube Function")  
axes.legend()  
print("################################")
