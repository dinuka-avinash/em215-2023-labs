import math
import matplotlib.pyplot as plt

x = -20
final_e_x = 0

number_of_terms = 100

value_for_terms =[]

for i in range(number_of_terms):
        
    e_x = x**i/math.factorial(i)
    value_for_terms.append(e_x)

    

plt.plot(range(0,number_of_terms),value_for_terms)
plt.title("e^-20 calculation")
plt.xlabel("number of terms added")
plt.ylabel("e^x")
plt.show()