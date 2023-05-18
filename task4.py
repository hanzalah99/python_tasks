import argparse                #arg parse library 
import math                    #math library
import random

def pi_estimation(iterations):
    points_in_circle=0
    total_points=iterations
    for x in range(iterations):
        x=random.uniform(0,1)
        y=random.uniform(0,1)

        distance=math.sqrt(x*x+y*y)
        if distance >=1:
            points_in_circle+=1

    pi_estimated=4*(points_in_circle/total_points)
    return(pi_estimated)





def main():
    parser_pi=argparse.ArgumentParser(description='Estimation of pi using Monte Carlo Problem')  
    parser_pi.add_argument('-i','--iterations',type=int, help='Enter the number of iterations')
    args_pi=parser_pi.parse_args()

    iterations=args_pi.iterations

    pi=pi_estimation(iterations)
    print(pi)