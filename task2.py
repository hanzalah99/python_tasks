import argparse                #arg parse library 
import math                    #math library

def calc_movment(movement):  #function to calculate the distance from starting position
    x,y=0,0
    for index in range(len(movement)):
        if movement[index]=="UP":
            y=y+int(movement[index+1])     #distance covered UP is added in the y-axis
        elif movement[index]=="DOWN":
            y=y-int(movement[index+1])     #distance covered DOWN is subtracted from the y-axis
        elif movement[index]=="LEFT":
            x=x+int(movement[index+1])     #distance covered LEFT is added in the x-axis
        elif movement[index]=="RIGHT":
            x=x-int(movement[index+1])     #distance covered DOWN is subtracted from the y-axis

    total_dist=math.sqrt((x*x)+(y*y))
    return round(total_dist)        # total covered is rounded off


def main():
    parser_dist=argparse.ArgumentParser(description='Directions and distance')  
    parser_dist.add_argument('dist',nargs='+',type=str, help='Enter all movements')
    args_dist=parser_dist.parse_args()
    dist=args_dist.dist

    movement=tuple(dist)
    result=calc_movment(movement)
    print(result)
