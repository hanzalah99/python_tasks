import argparse
import math

def calc_movment(movement):
    x,y=0,0
    for index in range(len(movement)):
        if movement[index]=="UP":
            y=y+int(movement[index+1])
        elif movement[index]=="DOWN":
            y=y-int(movement[index+1])
        elif movement[index]=="LEFT":
            x=x+int(movement[index+1])
        elif movement[index]=="RIGHT":
            x=x-int(movement[index+1])

    total_dist=math.sqrt((x*x)+abs(y*y))
    return round(total_dist)



parser_dist=argparse.ArgumentParser(description='Directions and distance')
parser_dist.add_argument('dist',nargs='+',type=str, help='Enter all movements')
args_dist=parser_dist.parse_args()
dist=args_dist.dist


movement=tuple(dist)
result=calc_movment(movement)
print(result)
