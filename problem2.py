def f(x):
    return x**4 * 0.05+ x**3 * 0.1 + x**2 * 0.5 + x*10 +5

def f_d(x):
    return x**3 * 0.05*4+ x**2 * 0.1*3 + x * 0.5*2 + 10 

def f_d2(x):
    return x**2 * 0.05*4*3+ x * 0.1*3*2 +  0.5*2 

x_min=float(input("give an initial x_min value: "))
iter_num=int(input("give the number of iterations to make: "))

for i in range(iter_num):
    x_min=round(x_min-(f_d(x_min)/f_d2(x_min)),3)
    print("Estimated value of x_min after iteration {0}: {1} ".format(i,x_min))

print(""" x_min = {0} 
  y_min = {1}""".format(x_min,round(f(x_min),3)))
