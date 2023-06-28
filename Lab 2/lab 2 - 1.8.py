#Ex 1.8 

from tabulate import tabulate


def f_x_equation(var_x): #f(x) equation

    answer = -0.1*(var_x)**4 - 0.5*(var_x)**2 - 0.5*(var_x) + 1.2

    return answer

f_x_first_derivative = -1.050

""" def f_x_first_derivative (var_x): #f`(x) first derivative equation 

    answer = -0.4*var_x**3 - var_x - 0.5  

    return answer  """

head = ["h","x(i+1)","x(i-1)","f(x(i+1))","f(x(i-1))","f`(x(i))","|Et|"]

x_ = 0.5 #varible used for finding derivative

h = 1 #step size -initial value

data_table=[]

for i in range(10):

    x_i_minus_1 = x_ - h

    x_i_plus_1 = x_ + h

    #calculating the first derivtive using the centered difference approximation
    f_der_using_c_d_approx = (f_x_equation(x_i_plus_1) - f_x_equation(x_i_minus_1)) / 2*h 

    #calculating the first derivative using equation

    #error calculation
    Et = abs(f_x_first_derivative - f_der_using_c_d_approx)

    #data adding for 

    data_table.append([h,x_i_plus_1,x_i_minus_1,f_x_equation(x_i_plus_1),f_x_equation(x_i_minus_1),f_der_using_c_d_approx,Et])

    h = h/10

print(tabulate(data_table,headers=head))