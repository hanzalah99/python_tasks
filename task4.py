import argparse                #arg parse library 
import math                    #math library
import random

def pi_estimation(iterations):
    points_in_circle=0
    total_points=iterations
    for x in range(iterations):
        x=random.uniform(0,1)
        y=random.uniform(0,1)

        distance=x*x+y*y
        if distance <=1:
            points_in_circle=points_in_circle+1

    print(points_in_circle)
    pi_estimated=4*(points_in_circle/total_points)
    print(pi_estimated)
    return(pi_estimated)


def main():
    parser_pi=argparse.ArgumentParser(description='Estimation of pi using Monte Carlo Problem')  
    parser_pi.add_argument('-i','--iterations',type=int, help='Enter the number of iterations')
    args_pi=parser_pi.parse_args()

    iterations=args_pi.iterations

    pi=pi_estimation(iterations)
    print(pi)
           
if __name__ == "__main__":
    main()