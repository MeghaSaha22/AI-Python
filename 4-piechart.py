import matplotlib.pyplot as plt
import pandas as pd
goal_types =['Penalties','Field Goals','Free Kicks']
goals = [12,38,7]  
mycolors = ['y','r','b']

plt.pie(goals, labels = goal_types, colors=mycolors ,
       shadow =False, explode = (0.0, 0.0, 0.1),
         autopct = '%.2f%%'
      ) 
plt.show() 

