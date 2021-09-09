import matplotlib.pyplot as plt 

import numpy as np
import pandas as pd

print('HACKATHON-SHELL')
df=pd.read_csv(r'../Shell_Hackathon Dataset/turbine_loc_test.csv')

# plotting points as a scatter plot 
plt.scatter(df['x'], df['y'], label= "stars", color= "green", 
			marker= "*", s=30) 

# x-axis label 
plt.xlabel('x - axis') 
# frequency label 
plt.ylabel('y - axis') 
# plot title 
plt.title('My wind plot!') 
# showing legend 
plt.legend() 

# function to show the plot 
plt.show() 
