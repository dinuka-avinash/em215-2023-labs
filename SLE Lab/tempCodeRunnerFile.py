
# #Task 1

# A = np.array = ([5,10,3,1],
#                 [6,7,20,-1],
#                 [12,2,3,-30],
#                 [15,-1,1,1])

# B = np.array = ([6.7],
#                 [5.8],
#                 [4.3],
#                 [2.1])

# A_1 = np.linalg.inv(A)

# #print("det(A) is" , np.linalg.det(A))

# #solution using matrix

# x = np.dot(A_1,B)
# #print("X = \n" , x) 

# #Task 2

# '''
# #initial guesses
# x1_k = 0
# x2_k = 0
# x3_k = 0
# x4_k = 0


# answers = []
# answers.append((x1_k,x2_k,x3_k,x4_k))

# #calculation loop
# decimal_points = 5 #change this to change the precision decimal points in the answer
# number_of_interations = 20 #change this to change the number of iterations

# i = 1
# while i<=number_of_interations:

#     x1_k1 = (6.7 - 10*x2_k - 3*x3_k - x4_k)/5
#     x2_k1 = (5.8 - 6*x1_k - 20*x3_k + x4_k)/7
#     x3_k1 = (4.3 - 12*x1_k - 2*x2_k + 30*x4_k)/3
#     x4_k1 = (2.1 - 15*x1_k + x2_k - x3_k)

#     answers.append((round(x1_k1,decimal_points),round(x2_k1,decimal_points),round(x3_k1,decimal_points),round(x4_k1,decimal_points)))

#     x1_k = x1_k1
#     x2_k = x2_k1
#     x3_k = x3_k1
#     x4_k = x4_k1

#     i += 1

# #results printing
# k = 0
# while k<=number_of_interations:

#     print(k , answers[k])
#     k += 1

# #since the system is not diagonally dominant, the answer is not converging
# '''
# #Task 3

# """ 
# #initial guesses
# x1_k = 5
# x2_k = -3
# x3_k = 5
# x4_k = 0


# answers = []
# answers.append((x1_k,x2_k,x3_k,x4_k))


# decimal_points = 5 #change this to change the precision decimal points in the answer

# #stopping criteria setting
# number_of_interations = 20 #change this to change the number of iterations
# tolerance = 0.00001 #change this to change the tolerance value of the norm

# #calculation loop
# i = 1
# while True:

#     #equations
#     x1_k1 = (2.1 + x2_k - x3_k - x4_k)/15
#     x2_k1 = (6.7 - 5*x1_k - 3*x3_k - x4_k)/10
#     x3_k1 = (5.8 - 6*x1_k - 7*x2_k + x4_k)/20
#     x4_k1 = (4.3 - 12*x1_k - 2*x2_k - 3*x3_k)/-30

#     answers.append((round(x1_k1,decimal_points),round(x2_k1,decimal_points),round(x3_k1,decimal_points),round(x4_k1,decimal_points)))

#     norm = math.sqrt((x1_k1-x1_k)**2 + (x2_k1-x2_k)**2 + (x3_k1-x3_k)**2 + (x4_k1-x4_k)**2) 
    
#     #stopping criteria check and exit 
#     if ((i==number_of_interations) or (norm <= tolerance)):
#         break

#     #if not stopped, prep for next iteration
#     x1_k = x1_k1
#     x2_k = x2_k1
#     x3_k = x3_k1
#     x4_k = x4_k1

#     i += 1

# print("Number of iterations : " , i)
# #results printing
# k = 0
# while k<=i:

#     print(k , answers[k])
#     k += 1  """

# #Task 4 - task 1 should be uncommented

# #tenth_power = [0,1,2,3,4,5,6,7,8,9,10]
# #tenth_power = np.arange(0,11,1)
# tenth_power = range(11)
# number_of_iterations = []

# for i in range(11):

#     #initial guesses
#     x1_k = x[0]*(10**i)
#     x2_k = x[1]*(10**i)
#     x3_k = x[2]*(10**i)
#     x4_k = x[3]*(10**i)

 
#     decimal_points = 5 #change this to change the precision decimal points in the answer

#     #stopping criteria setting
#     #number_of_interations = 20 #change this to change the number of iterations
#     tolerance = 10e-8 #change this to change the tolerance value of the norm

#     #calculation loop
#     j = 1
#     while True:

#         #equations
#         x1_k1 = (2.1 + x2_k - x3_k - x4_k)/15
#         x2_k1 = (6.7 - 5*x1_k - 3*x3_k - x4_k)/10
#         x3_k1 = (5.8 - 6*x1_k - 7*x2_k + x4_k)/20
#         x4_k1 = (4.3 - 12*x1_k - 2*x2_k - 3*x3_k)/-30

#         #answers.append((round(x1_k1,decimal_points),round(x2_k1,decimal_points),round(x3_k1,decimal_points),round(x4_k1,decimal_points)))

#         norm = math.sqrt((x1_k1-x1_k)**2 + (x2_k1-x2_k)**2 + (x3_k1-x3_k)**2 + (x4_k1-x4_k)**2) 
        
#         #stopping criteria check and exit 
#         if (norm <= tolerance):
#             break

#         #if not stopped, prep for next iteration
#         x1_k = x1_k1
#         x2_k = x2_k1
#         x3_k = x3_k1
#         x4_k = x4_k1

#         j += 1

#     number_of_iterations.append(j)
# """
# print(type(number_of_iterations))
# print(type(tenth_power))
# """

# print(list(tenth_power))
# print(number_of_iterations)

# #graph plotting
# #plt.plot(list(tenth_power), number_of_iterations)

# #plt.legend("Numerical","Analytical")
# #plt.xlabel("Tenth Power of Initial guess")
# #plt.ylabel("Number of iterations")
# #plt.show()

