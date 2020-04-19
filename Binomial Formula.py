import matplotlib.pyplot as plt
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def combination(a, b):
    return int(factorial(a)/(factorial(b)*factorial(a-b)))
#x successes from n trials with the success of p
def binomial_success(n, x, p):
    q = 1-p
    return combination(n, x)*(p**x)*(q**(n-x))
#print(binomial_success(3, 1, 0.05))
#I will create a bar graph for success of 6 trials with success of 0.3
#number_of_success = [i for i in range(7)]
#P_x = []
#for i in number_of_success:
#    succ_prob = binomial_success(6, i, 0.3)
#    P_x.append(succ_prob)
#plt.bar(number_of_success, P_x)
#plt.show()
#mean and standard deviation of a binomial distributions with total n trials and probability of success p
def meanBinDist(n, p):
    return n*p
def stdBinDist(n, p):
    q = 1-p
    return (n*p*q)**0.5

##############################################################################################################
##############################################################################################################
##############################################################################################################

#Hypergeometric Probability Distribution for population number N,r population successes,n trials and
#x successful trials

def hypergeometric(N, r, n, x):
    return  (combination(r, x) * combination(N-r, n-x)/combination(N, n))
#print(hypergeometric(12, 7, 3, 3)) #it works well

###################################################################################################################
#####################################################################################################################
#################################################################################################################
#poisson probability distribution
import math
def poisson(x, y):
    e = math.e
    return ((y**x)/((e**y)*factorial(x)))


print(poisson(6, 9.5))












