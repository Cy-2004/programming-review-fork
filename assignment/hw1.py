# Question 1.3: I was surprised flight attendants make so much despite only requiring a high school diploma.
# Question 1.4: Software Developer, Data Scientist, Financial Analyst, Accountant, Flight Attendant, 
                # Advertising/Promotions/Marketing Managers, Lawyer, Physicians/Surgeons
                # I ranked the first 4 jobs based on all needing a bachelors degree and by most pay. 
                # I ranked flight attendant next because it pays a less but has a low entry requirement. 
                # I ranked the manager positions next because it requires previous work experience. 
                # I ranked lawyer next because it requires a professional degrees. 
                # I ranked physician last because it requires a professional degrees and more job training.

# Question 2
import numpy as np
import matplotlib.pyplot as plt

# part 1
x = np.linspace(0,1,50)
y = np.log(x)
z = np.exp(x)
plt.scatter(x,y, label='Natural Log')
plt.scatter(x,z, label='Exponential')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Natural Log and Exponential Functions")
plt.legend(loc = 'lower right')
plt.show()

# part 2
grid = np.linspace(-6.5,6.5,100)
sin = np.sin(grid)
cos = np.cos(grid)
plt.plot(grid,sin, label="Sine")
plt.plot(grid,cos, label="Cosine")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sine and Cosine Functions")
plt.legend(loc = 'lower left')
plt.show()